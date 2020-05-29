#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_bare_metal_info
short_description: Retrieve IBM Cloud 'ibm_compute_bare_metal' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_compute_bare_metal' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.7.0
    - Terraform v0.12.20

options:
    public_vlan_id:
        description:
            - The public VLAN used for the public network interface of the server.
        required: False
        type: int
    private_vlan_id:
        description:
            - The private VLAN used for the private network interface of the server.
        required: False
        type: int
    private_subnet:
        description:
            - The private subnet used for the private network interface of the server.
        required: False
        type: int
    hourly_billing:
        description:
            - The billing type of the server.
        required: False
        type: bool
    os_reference_code:
        description:
            - None
        required: False
        type: str
    ipv6_address:
        description:
            - The public IPv6 address of the bare metal server
        required: False
        type: str
    secondary_ip_count:
        description:
            - The number of secondary IPv4 addresses of the bare metal server.
        required: False
        type: int
    hostname:
        description:
            - The hostname of the bare metal server
        required: False
        type: str
    secondary_ip_addresses:
        description:
            - The public secondary IPv4 addresses of the bare metal server.
        required: False
        type: list
        elements: str
    public_ipv4_address:
        description:
            - The public IPv4 address of the bare metal server.
        required: False
        type: str
    private_ipv4_address:
        description:
            - The private IPv4 address of the bare metal server.
        required: False
        type: str
    tags:
        description:
            - Tags associated with this bare metal server.
        required: False
        type: list
        elements: str
    ipv6_address_id:
        description:
            - None
        required: False
        type: int
    global_identifier:
        description:
            - The unique global identifier of the bare metal server
        required: False
        type: str
    private_network_only:
        description:
            - Specifies whether the server only has access to the private network.
        required: False
        type: bool
    notes:
        description:
            - Notes associated with the server.
        required: False
        type: str
    block_storage_ids:
        description:
            - Block storage to which this computing server have access.
        required: False
        type: list
        elements: int
    most_recent:
        description:
            - If true and multiple entries are found, the most recently created bare metal is used. If false, an error is returned
        required: False
        type: bool
        default: False
    datacenter:
        description:
            - Datacenter in which the bare metal is deployed
        required: False
        type: str
    network_speed:
        description:
            - The connection speed, expressed in Mbps,  for the server network components.
        required: False
        type: int
    private_ipv4_address_id:
        description:
            - None
        required: False
        type: int
    public_subnet:
        description:
            - The public subnet used for the public network interface of the server.
        required: False
        type: int
    user_metadata:
        description:
            - Arbitrary data available to the computing server.
        required: False
        type: str
    redundant_power_supply:
        description:
            - When the value is `true`, it indicates additional power supply is provided.
        required: False
        type: bool
    redundant_network:
        description:
            - When the value is `true`, two physical network interfaces are provided with a bonding configuration.
        required: False
        type: bool
    unbonded_network:
        description:
            - When the value is `true`, two physical network interfaces are provided without a bonding configuration.
        required: False
        type: bool
    domain:
        description:
            - The domain of the bare metal server
        required: False
        type: str
    file_storage_ids:
        description:
            - File storage to which this computing server have access.
        required: False
        type: list
        elements: int
    ipv6_enabled:
        description:
            - Indicates whether the public IPv6 address enabled or not
        required: False
        type: bool
    public_ipv4_address_id:
        description:
            - None
        required: False
        type: int
    memory:
        description:
            - The amount of memory in gigabytes, for the server.
        required: False
        type: int
    public_bandwidth:
        description:
            - The amount of public network traffic, allowed per month.
        required: False
        type: int
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
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
    'public_vlan_id',
    'private_vlan_id',
    'private_subnet',
    'hourly_billing',
    'os_reference_code',
    'ipv6_address',
    'secondary_ip_count',
    'hostname',
    'secondary_ip_addresses',
    'public_ipv4_address',
    'private_ipv4_address',
    'tags',
    'ipv6_address_id',
    'global_identifier',
    'private_network_only',
    'notes',
    'block_storage_ids',
    'most_recent',
    'datacenter',
    'network_speed',
    'private_ipv4_address_id',
    'public_subnet',
    'user_metadata',
    'redundant_power_supply',
    'redundant_network',
    'unbonded_network',
    'domain',
    'file_storage_ids',
    'ipv6_enabled',
    'public_ipv4_address_id',
    'memory',
    'public_bandwidth',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    public_vlan_id=dict(
        required=False,
        type='int'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    private_subnet=dict(
        required=False,
        type='int'),
    hourly_billing=dict(
        required=False,
        type='bool'),
    os_reference_code=dict(
        required=False,
        type='str'),
    ipv6_address=dict(
        required=False,
        type='str'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    hostname=dict(
        required=False,
        type='str'),
    secondary_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    public_ipv4_address=dict(
        required=False,
        type='str'),
    private_ipv4_address=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    ipv6_address_id=dict(
        required=False,
        type='int'),
    global_identifier=dict(
        required=False,
        type='str'),
    private_network_only=dict(
        required=False,
        type='bool'),
    notes=dict(
        required=False,
        type='str'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    most_recent=dict(
        default=False,
        type='bool'),
    datacenter=dict(
        required=False,
        type='str'),
    network_speed=dict(
        required=False,
        type='int'),
    private_ipv4_address_id=dict(
        required=False,
        type='int'),
    public_subnet=dict(
        required=False,
        type='int'),
    user_metadata=dict(
        required=False,
        type='str'),
    redundant_power_supply=dict(
        required=False,
        type='bool'),
    redundant_network=dict(
        required=False,
        type='bool'),
    unbonded_network=dict(
        required=False,
        type='bool'),
    domain=dict(
        required=False,
        type='str'),
    file_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    ipv6_enabled=dict(
        required=False,
        type='bool'),
    public_ipv4_address_id=dict(
        required=False,
        type='int'),
    memory=dict(
        required=False,
        type='int'),
    public_bandwidth=dict(
        required=False,
        type='int'),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
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

    result = ibmcloud_terraform(
        resource_type='ibm_compute_bare_metal',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.7.0',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
