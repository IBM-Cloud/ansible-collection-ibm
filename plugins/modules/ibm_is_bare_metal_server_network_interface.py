#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_bare_metal_server_network_interface
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_bare_metal_server_network_interface

short_description: Configure IBM Cloud 'ibm_is_bare_metal_server_network_interface' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_bare_metal_server_network_interface' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.51.0
    - Terraform v0.12.20

options:
    vlan:
        description:
            - Indicates the 802.1Q VLAN ID tag that must be used for all traffic on this interface
        required: False
        type: int
    bare_metal_server:
        description:
            - (Required for new resource) Bare metal server identifier
        required: True
        type: str
    interface_type:
        description:
            - The network interface type: [ pci, vlan, hipersocket ]
        required: False
        type: str
    primary_ip:
        description:
            - title: IPv4, The IP address.
        required: False
        type: list
        elements: dict
    security_groups:
        description:
            - Collection of security groups ids
        required: False
        type: list
        elements: str
    allowed_vlans:
        description:
            - Indicates what VLAN IDs (for VLAN type only) can use this physical (PCI type) interface. A given VLAN can only be in the allowed_vlans array for one PCI type adapter per bare metal server.
        required: False
        type: list
        elements: int
    allow_ip_spoofing:
        description:
            - Indicates whether source IP spoofing is allowed on this interface. If false, source IP spoofing is prevented on this interface. If true, source IP spoofing is allowed on this interface.
        required: False
        type: bool
    enable_infrastructure_nat:
        description:
            - If true, the VPC infrastructure performs any needed NAT operations. If false, the packet is passed unmodified to/from the network interface, allowing the workload to perform any needed NAT operations.
        required: False
        type: bool
    allow_interface_to_float:
        description:
            - Indicates if the interface can float to any other server within the same resource_group. The interface will float automatically if the network detects a GARP or RARP on another bare metal server in the resource group. Applies only to vlan type interfaces.
        required: False
        type: bool
    subnet:
        description:
            - (Required for new resource) The id of the associated subnet
        required: True
        type: str
    hard_stop:
        description:
            - Only used for PCI network interfaces, whether to hard/immediately stop server
        required: False
        type: bool
        default: True
    name:
        description:
            - The user-defined name for this network interface
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
    ('bare_metal_server', 'str'),
    ('subnet', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'vlan',
    'bare_metal_server',
    'interface_type',
    'primary_ip',
    'security_groups',
    'allowed_vlans',
    'allow_ip_spoofing',
    'enable_infrastructure_nat',
    'allow_interface_to_float',
    'subnet',
    'hard_stop',
    'name',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('network_interface', 'str'),
    ('bare_metal_server', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'network_interface',
    'bare_metal_server',
]

TL_CONFLICTS_MAP = {
    'vlan': ['allowed_vlans'],
    'allowed_vlans': ['allow_interface_to_float', 'vlan'],
    'allow_interface_to_float': ['allowed_vlans'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    vlan=dict(
        required=False,
        type='int'),
    bare_metal_server=dict(
        required=False,
        type='str'),
    interface_type=dict(
        required=False,
        type='str'),
    primary_ip=dict(
        required=False,
        elements='',
        type='list'),
    security_groups=dict(
        required=False,
        elements='',
        type='list'),
    allowed_vlans=dict(
        required=False,
        elements='',
        type='list'),
    allow_ip_spoofing=dict(
        required=False,
        type='bool'),
    enable_infrastructure_nat=dict(
        required=False,
        type='bool'),
    allow_interface_to_float=dict(
        required=False,
        type='bool'),
    subnet=dict(
        required=False,
        type='str'),
    hard_stop=dict(
        required=False,
        type='bool'),
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
        resource_type='ibm_is_bare_metal_server_network_interface',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.51.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_bare_metal_server_network_interface',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.51.0',
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
