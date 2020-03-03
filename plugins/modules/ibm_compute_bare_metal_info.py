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
    - IBM-Cloud terraform-provider-ibm v1.2.3
    - Terraform v0.12.20

options:
    ipv6_address:
        description:
            - The public IPv6 address of the bare metal server
        required: False
        type: str
    global_identifier:
        description:
            - The unique global identifier of the bare metal server
        required: False
        type: str
    network_speed:
        description:
            - The connection speed, expressed in Mbps,  for the server network components.
        required: False
        type: int
    notes:
        description:
            - Notes associated with the server.
        required: False
        type: str
    ipv6_enabled:
        description:
            - Indicates whether the public IPv6 address enabled or not
        required: False
        type: bool
    private_network_only:
        description:
            - Specifies whether the server only has access to the private network.
        required: False
        type: bool
    redundant_power_supply:
        description:
            - When the value is `true`, it indicates additional power supply is provided.
        required: False
        type: bool
    tags:
        description:
            - Tags associated with this bare metal server.
        required: False
        type: list
        elements: str
    datacenter:
        description:
            - Datacenter in which the bare metal is deployed
        required: False
        type: str
    public_ipv4_address_id:
        description:
            - None
        required: False
        type: int
    redundant_network:
        description:
            - When the value is `true`, two physical network interfaces are provided with a bonding configuration.
        required: False
        type: bool
    file_storage_ids:
        description:
            - File storage to which this computing server have access.
        required: False
        type: list
        elements: int
    ipv6_address_id:
        description:
            - None
        required: False
        type: int
    most_recent:
        description:
            - If true and multiple entries are found, the most recently created bare metal is used. If false, an error is returned
        required: False
        type: bool
        default: False
    public_subnet:
        description:
            - The public subnet used for the public network interface of the server.
        required: False
        type: int
    hourly_billing:
        description:
            - The billing type of the server.
        required: False
        type: bool
    user_metadata:
        description:
            - Arbitrary data available to the computing server.
        required: False
        type: str
    private_vlan_id:
        description:
            - The private VLAN used for the private network interface of the server.
        required: False
        type: int
    unbonded_network:
        description:
            - When the value is `true`, two physical network interfaces are provided without a bonding configuration.
        required: False
        type: bool
    os_reference_code:
        description:
            - None
        required: False
        type: str
    private_subnet:
        description:
            - The private subnet used for the private network interface of the server.
        required: False
        type: int
    memory:
        description:
            - The amount of memory in gigabytes, for the server.
        required: False
        type: int
    secondary_ip_addresses:
        description:
            - The public secondary IPv4 addresses of the bare metal server.
        required: False
        type: list
        elements: str
    domain:
        description:
            - The domain of the bare metal server
        required: False
        type: str
    public_bandwidth:
        description:
            - The amount of public network traffic, allowed per month.
        required: False
        type: int
    public_ipv4_address:
        description:
            - The public IPv4 address of the bare metal server.
        required: False
        type: str
    public_vlan_id:
        description:
            - The public VLAN used for the public network interface of the server.
        required: False
        type: int
    block_storage_ids:
        description:
            - Block storage to which this computing server have access.
        required: False
        type: list
        elements: int
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
    private_ipv4_address:
        description:
            - The private IPv4 address of the bare metal server.
        required: False
        type: str
    private_ipv4_address_id:
        description:
            - None
        required: False
        type: int
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be provided
              via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'ipv6_address',
    'global_identifier',
    'network_speed',
    'notes',
    'ipv6_enabled',
    'private_network_only',
    'redundant_power_supply',
    'tags',
    'datacenter',
    'public_ipv4_address_id',
    'redundant_network',
    'file_storage_ids',
    'ipv6_address_id',
    'most_recent',
    'public_subnet',
    'hourly_billing',
    'user_metadata',
    'private_vlan_id',
    'unbonded_network',
    'os_reference_code',
    'private_subnet',
    'memory',
    'secondary_ip_addresses',
    'domain',
    'public_bandwidth',
    'public_ipv4_address',
    'public_vlan_id',
    'block_storage_ids',
    'secondary_ip_count',
    'hostname',
    'private_ipv4_address',
    'private_ipv4_address_id',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    ipv6_address=dict(
        required=False,
        type='str'),
    global_identifier=dict(
        required=False,
        type='str'),
    network_speed=dict(
        required=False,
        type='int'),
    notes=dict(
        required=False,
        type='str'),
    ipv6_enabled=dict(
        required=False,
        type='bool'),
    private_network_only=dict(
        required=False,
        type='bool'),
    redundant_power_supply=dict(
        required=False,
        type='bool'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    datacenter=dict(
        required=False,
        type='str'),
    public_ipv4_address_id=dict(
        required=False,
        type='int'),
    redundant_network=dict(
        required=False,
        type='bool'),
    file_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    ipv6_address_id=dict(
        required=False,
        type='int'),
    most_recent=dict(
        default=False,
        type='bool'),
    public_subnet=dict(
        required=False,
        type='int'),
    hourly_billing=dict(
        required=False,
        type='bool'),
    user_metadata=dict(
        required=False,
        type='str'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    unbonded_network=dict(
        required=False,
        type='bool'),
    os_reference_code=dict(
        required=False,
        type='str'),
    private_subnet=dict(
        required=False,
        type='int'),
    memory=dict(
        required=False,
        type='int'),
    secondary_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    domain=dict(
        required=False,
        type='str'),
    public_bandwidth=dict(
        required=False,
        type='int'),
    public_ipv4_address=dict(
        required=False,
        type='str'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    hostname=dict(
        required=False,
        type='str'),
    private_ipv4_address=dict(
        required=False,
        type='str'),
    private_ipv4_address_id=dict(
        required=False,
        type='int'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south')
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_compute_bare_metal',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.2.3',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
