#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_instance
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance

short_description: Configure IBM Cloud 'ibm_is_instance' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_instance' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.37.1
    - Terraform v0.12.20

options:
    dedicated_host_group:
        description:
            - Unique Identifier of the Dedicated Host Group where the instance will be placed
        required: False
        type: str
    total_volume_bandwidth:
        description:
            - The amount of bandwidth (in megabits per second) allocated exclusively to instance storage volumes
        required: False
        type: int
    network_interfaces:
        description:
            - None
        required: False
        type: list
        elements: dict
    instance_template:
        description:
            - Id of the instance template
        required: False
        type: str
    wait_before_delete:
        description:
            - Enables stopping of instance before deleting and waits till deletion is complete
        required: False
        type: bool
        default: True
    auto_delete_volume:
        description:
            - Auto delete volume along with instance
        required: False
        type: bool
    primary_network_interface:
        description:
            - Primary Network interface info
        required: False
        type: list
        elements: dict
    force_recovery_time:
        description:
            - Define timeout to force the instances to start/stop in minutes.
        required: False
        type: int
    name:
        description:
            - (Required for new resource) Instance name
        required: True
        type: str
    profile:
        description:
            - Profile info
        required: False
        type: str
    zone:
        description:
            - Zone name
        required: False
        type: str
    placement_group:
        description:
            - Unique Identifier of the Placement Group for restricting the placement of the instance
        required: False
        type: str
    keys:
        description:
            - SSH key Ids for the instance
        required: False
        type: list
        elements: str
    force_action:
        description:
            - If set to true, the action will be forced immediately, and all queued actions deleted. Ignored for the start action.
        required: False
        type: bool
        default: False
    image:
        description:
            - image id
        required: False
        type: str
    resource_group:
        description:
            - Instance resource group
        required: False
        type: str
    vpc:
        description:
            - VPC id
        required: False
        type: str
    action:
        description:
            - Enables stopping of instance before deleting and waits till deletion is complete
        required: False
        type: str
    user_data:
        description:
            - User data given for the instance
        required: False
        type: str
    volumes:
        description:
            - List of volumes
        required: False
        type: list
        elements: str
    tags:
        description:
            - list of tags for the instance
        required: False
        type: list
        elements: str
    dedicated_host:
        description:
            - Unique Identifier of the Dedicated Host where the instance will be placed
        required: False
        type: str
    boot_volume:
        description:
            - None
        required: False
        type: list
        elements: dict
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
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'dedicated_host_group',
    'total_volume_bandwidth',
    'network_interfaces',
    'instance_template',
    'wait_before_delete',
    'auto_delete_volume',
    'primary_network_interface',
    'force_recovery_time',
    'name',
    'profile',
    'zone',
    'placement_group',
    'keys',
    'force_action',
    'image',
    'resource_group',
    'vpc',
    'action',
    'user_data',
    'volumes',
    'tags',
    'dedicated_host',
    'boot_volume',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'passphrase',
    'private_key',
    'name',
]

TL_CONFLICTS_MAP = {
    'dedicated_host_group': ['dedicated_host', 'placement_group'],
    'instance_template': ['boot_volume.0.snapshot'],
    'placement_group': ['dedicated_host', 'dedicated_host_group'],
    'image': ['boot_volume.0.snapshot'],
    'dedicated_host': ['dedicated_host_group', 'placement_group'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    dedicated_host_group=dict(
        required=False,
        type='str'),
    total_volume_bandwidth=dict(
        required=False,
        type='int'),
    network_interfaces=dict(
        required=False,
        elements='',
        type='list'),
    instance_template=dict(
        required=False,
        type='str'),
    wait_before_delete=dict(
        required=False,
        type='bool'),
    auto_delete_volume=dict(
        required=False,
        type='bool'),
    primary_network_interface=dict(
        required=False,
        elements='',
        type='list'),
    force_recovery_time=dict(
        required=False,
        type='int'),
    name=dict(
        required=False,
        type='str'),
    profile=dict(
        required=False,
        type='str'),
    zone=dict(
        required=False,
        type='str'),
    placement_group=dict(
        required=False,
        type='str'),
    keys=dict(
        required=False,
        elements='',
        type='list'),
    force_action=dict(
        required=False,
        type='bool'),
    image=dict(
        required=False,
        type='str'),
    resource_group=dict(
        required=False,
        type='str'),
    vpc=dict(
        required=False,
        type='str'),
    action=dict(
        required=False,
        type='str'),
    user_data=dict(
        required=False,
        type='str'),
    volumes=dict(
        required=False,
        elements='',
        type='list'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    dedicated_host=dict(
        required=False,
        type='str'),
    boot_volume=dict(
        required=False,
        elements='',
        type='list'),
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
        resource_type='ibm_is_instance',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.37.1',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_instance',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.37.1',
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
