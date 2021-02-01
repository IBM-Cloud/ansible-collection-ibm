#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_subnet
short_description: Configure IBM Cloud 'ibm_is_subnet' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_subnet' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.16.1
    - Terraform v0.12.20

options:
    ipv4_cidr_block:
        description:
            - IPV4 subnet - CIDR block
        required: False
        type: str
    vpc:
        description:
            - (Required for new resource) VPC instance ID
        required: True
        type: str
    zone:
        description:
            - (Required for new resource) Subnet zone info
        required: True
        type: str
    total_ipv4_address_count:
        description:
            - The total number of IPv4 addresses in this subnet.
        required: False
        type: int
    ip_version:
        description:
            - The IP version(s) to support for this subnet.
        required: False
        type: str
        default: ipv4
    resource_group:
        description:
            - The resource group for this subnet
        required: False
        type: str
    name:
        description:
            - (Required for new resource) Subnet name
        required: True
        type: str
    network_acl:
        description:
            - The network ACL for this subnet
        required: False
        type: str
    public_gateway:
        description:
            - Public Gateway of the subnet
        required: False
        type: str
    routing_table:
        description:
            - routing table id that is associated with the subnet
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
    ('vpc', 'str'),
    ('zone', 'str'),
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'ipv4_cidr_block',
    'vpc',
    'zone',
    'total_ipv4_address_count',
    'ip_version',
    'resource_group',
    'name',
    'network_acl',
    'public_gateway',
    'routing_table',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
    'identifier',
    'name',
]

TL_CONFLICTS_MAP = {
    'ipv4_cidr_block': ['total_ipv4_address_count'],
    'total_ipv4_address_count': ['ipv4_cidr_block'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    ipv4_cidr_block=dict(
        required=False,
        type='str'),
    vpc=dict(
        required=False,
        type='str'),
    zone=dict(
        required=False,
        type='str'),
    total_ipv4_address_count=dict(
        required=False,
        type='int'),
    ip_version=dict(
        required=False,
        type='str'),
    resource_group=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    network_acl=dict(
        required=False,
        type='str'),
    public_gateway=dict(
        required=False,
        type='str'),
    routing_table=dict(
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
        resource_type='ibm_is_subnet',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.16.1',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_subnet',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.16.1',
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
