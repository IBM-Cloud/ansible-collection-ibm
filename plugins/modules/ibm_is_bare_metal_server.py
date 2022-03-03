#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_bare_metal_server
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_bare_metal_server

short_description: Configure IBM Cloud 'ibm_is_bare_metal_server' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_bare_metal_server' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.39.1
    - Terraform v0.12.20

options:
    network_interfaces:
        description:
            - None
        required: False
        type: list
        elements: dict
    action:
        description:
            - This restart/start/stops a bare metal server.
        required: False
        type: str
    keys:
        description:
            - (Required for new resource) SSH key Ids for the bare metal server
        required: True
        type: list
        elements: str
    profile:
        description:
            - (Required for new resource) profile name
        required: True
        type: str
    zone:
        description:
            - (Required for new resource) Zone name
        required: True
        type: str
    vpc:
        description:
            - The VPC the bare metal server is to be a part of
        required: False
        type: str
    primary_network_interface:
        description:
            - (Required for new resource) Primary Network interface info
        required: True
        type: list
        elements: dict
    image:
        description:
            - (Required for new resource) image id
        required: True
        type: str
    delete_type:
        description:
            - Enables stopping type of the bare metal server before deleting
        required: False
        type: str
        default: hard
    user_data:
        description:
            - User data given for the bare metal server
        required: False
        type: str
    resource_group:
        description:
            - Resource group name
        required: False
        type: str
    tags:
        description:
            - Tags for the Bare metal server
        required: False
        type: list
        elements: str
    name:
        description:
            - Bare metal server name
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    generation:
        description:
            - The generation of Virtual Private Cloud infrastructure
              that you want to use. Supported values are 1 for VPC
              generation 1, and 2 for VPC generation 2 infrastructure.
              If this value is not specified, 2 is used by default. This
              can also be provided via the environment variable
              'IC_GENERATION'.
        default: 2
        required: False
        type: int
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
        type: str
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('keys', 'list'),
    ('profile', 'str'),
    ('zone', 'str'),
    ('primary_network_interface', 'list'),
    ('image', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'network_interfaces',
    'action',
    'keys',
    'profile',
    'zone',
    'vpc',
    'primary_network_interface',
    'image',
    'delete_type',
    'user_data',
    'resource_group',
    'tags',
    'name',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
    'identifier',
    'name',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    network_interfaces=dict(
        required=False,
        elements='',
        type='list'),
    action=dict(
        required=False,
        type='str'),
    keys=dict(
        required=False,
        elements='',
        type='list'),
    profile=dict(
        required=False,
        type='str'),
    zone=dict(
        required=False,
        type='str'),
    vpc=dict(
        required=False,
        type='str'),
    primary_network_interface=dict(
        required=False,
        elements='',
        type='list'),
    image=dict(
        required=False,
        type='str'),
    delete_type=dict(
        required=False,
        type='str'),
    user_data=dict(
        required=False,
        type='str'),
    resource_group=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    generation=dict(
        type='int',
        required=False,
        fallback=(env_fallback, ['IC_GENERATION']),
        default=2),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    conflicts = {}
    if len(TL_CONFLICTS_MAP) != 0:
        for arg in TL_CONFLICTS_MAP:
            if module.params[arg]:
                for conflict in TL_CONFLICTS_MAP[arg]:
                    try:
                        if module.params[conflict]:
                            conflicts[arg] = conflict
                    except KeyError:
                        pass
    if len(conflicts):
        module.fail_json(msg=("conflicts exist: {}".format(conflicts)))

    # VPC required arguments checks
    if module.params['generation'] == 1:
        missing_args = []
        if module.params['iaas_classic_username'] is None:
            missing_args.append('iaas_classic_username')
        if module.params['iaas_classic_api_key'] is None:
            missing_args.append('iaas_classic_api_key')
        if missing_args:
            module.fail_json(msg=(
                "VPC generation=1 missing required arguments: " +
                ", ".join(missing_args)))
    elif module.params['generation'] == 2:
        if module.params['ibmcloud_api_key'] is None:
            module.fail_json(
                msg=("VPC generation=2 missing required argument: "
                     "ibmcloud_api_key"))

    result_ds = ibmcloud_terraform(
        resource_type='ibm_is_bare_metal_server',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.39.1',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_bare_metal_server',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.39.1',
            tl_required_params=TL_REQUIRED_PARAMETERS,
            tl_all_params=TL_ALL_PARAMETERS)
        if result['rc'] > 0:
            module.fail_json(
                msg=Terraform.parse_stderr(result['stderr']), **result)

        module.exit_json(**result)
    else:
        module.exit_json(**result_ds)


def main():
    run_module()


if __name__ == '__main__':
    main()
