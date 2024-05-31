#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_virtual_network_interface
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_virtual_network_interface

short_description: Configure IBM Cloud 'ibm_is_virtual_network_interface' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_virtual_network_interface' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.65.1
    - Terraform v1.5.5

options:
    auto_delete:
        description:
            - Indicates whether this virtual network interface will be automatically deleted when`target` is deleted.
        required: False
        type: bool
    primary_ip:
        description:
            - The reserved IP for this virtual network interface.
        required: False
        type: list
        elements: dict
    security_groups:
        description:
            - The security groups for this virtual network interface.
        required: False
        type: list
        elements: str
    access_tags:
        description:
            - Access management tags for the vni instance
        required: False
        type: list
        elements: str
    name:
        description:
            - The name for this virtual network interface. The name is unique across all virtual network interfaces in the VPC.
        required: False
        type: str
    allow_ip_spoofing:
        description:
            - Indicates whether source IP spoofing is allowed on this interface. If `false`, source IP spoofing is prevented on this interface. If `true`, source IP spoofing is allowed on this interface.
        required: False
        type: bool
    enable_infrastructure_nat:
        description:
            - If `true`:- The VPC infrastructure performs any needed NAT operations.- `floating_ips` must not have more than one floating IP.If `false`:- Packets are passed unchanged to/from the network interface,  allowing the workload to perform any needed NAT operations.- `allow_ip_spoofing` must be `false`.- If the virtual network interface is attached:  - The target `resource_type` must be `bare_metal_server_network_attachment`.  - The target `interface_type` must not be `hipersocket`.
        required: False
        type: bool
    tags:
        description:
            - UserTags for the vni instance
        required: False
        type: list
        elements: str
    ips:
        description:
            - The reserved IPs bound to this virtual network interface.May be empty when `lifecycle_state` is `pending`.
        required: False
        type: list
        elements: dict
    resource_group:
        description:
            - The resource group id for this virtual network interface.
        required: False
        type: str
    subnet:
        description:
            - The associated subnet id.
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
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'auto_delete',
    'primary_ip',
    'security_groups',
    'access_tags',
    'name',
    'allow_ip_spoofing',
    'enable_infrastructure_nat',
    'tags',
    'ips',
    'resource_group',
    'subnet',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('virtual_network_interface', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'virtual_network_interface',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    auto_delete=dict(
        required=False,
        type='bool'),
    primary_ip=dict(
        required=False,
        elements='',
        type='list'),
    security_groups=dict(
        required=False,
        elements='',
        type='list'),
    access_tags=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=False,
        type='str'),
    allow_ip_spoofing=dict(
        required=False,
        type='bool'),
    enable_infrastructure_nat=dict(
        required=False,
        type='bool'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    ips=dict(
        required=False,
        elements='',
        type='list'),
    resource_group=dict(
        required=False,
        type='str'),
    subnet=dict(
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
        resource_type='ibm_is_virtual_network_interface',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.65.1',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_virtual_network_interface',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.65.1',
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
