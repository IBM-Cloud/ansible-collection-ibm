#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_bare_metal
short_description: Configure IBM Cloud 'ibm_compute_bare_metal' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_compute_bare_metal' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.3
    - Terraform v0.12.20

options:
    tcp_monitoring:
        description:
            - None
        required: False
        type: bool
        default: False
    private_subnet:
        description:
            - None
        required: False
        type: str
    secondary_ip_count:
        description:
            - None
        required: False
        type: int
    ipv6_static_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    file_storage_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    datacenter:
        description:
            - None
        required: False
        type: str
    network_speed:
        description:
            - None
        required: False
        type: int
        default: 100
    memory:
        description:
            - None
        required: False
        type: int
    storage_groups:
        description:
            - None
        required: False
        type: list
        elements: dict
    public_subnet:
        description:
            - None
        required: False
        type: str
    global_identifier:
        description:
            - The unique global identifier of the bare metal server
        required: False
        type: str
    domain:
        description:
            - (Required for new resource) 
        required: False
        type: str
    redundant_power_supply:
        description:
            - None
        required: False
        type: bool
    gpu_secondary_key_name:
        description:
            - None
        required: False
        type: str
    private_ipv4_address_id:
        description:
            - None
        required: False
        type: int
    secondary_ip_addresses:
        description:
            - None
        required: False
        type: list
        elements: str
    notes:
        description:
            - None
        required: False
        type: str
    post_install_script_uri:
        description:
            - None
        required: False
        type: str
    os_key_name:
        description:
            - None
        required: False
        type: str
    public_bandwidth:
        description:
            - None
        required: False
        type: int
    quote_id:
        description:
            - None
        required: False
        type: int
    private_vlan_id:
        description:
            - None
        required: False
        type: int
    private_ipv4_address:
        description:
            - None
        required: False
        type: str
    ipv6_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    user_metadata:
        description:
            - None
        required: False
        type: str
    os_reference_code:
        description:
            - None
        required: False
        type: str
    image_template_id:
        description:
            - None
        required: False
        type: int
    hourly_billing:
        description:
            - None
        required: False
        type: bool
        default: True
    package_key_name:
        description:
            - None
        required: False
        type: str
    unbonded_network:
        description:
            - None
        required: False
        type: bool
        default: False
    block_storage_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    extended_hardware_testing:
        description:
            - None
        required: False
        type: bool
        default: False
    public_vlan_id:
        description:
            - None
        required: False
        type: int
    public_ipv4_address_id:
        description:
            - None
        required: False
        type: int
    ipv6_address:
        description:
            - None
        required: False
        type: str
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    fixed_config_preset:
        description:
            - None
        required: False
        type: str
    software_guard_extensions:
        description:
            - None
        required: False
        type: bool
        default: False
    process_key_name:
        description:
            - None
        required: False
        type: str
    disk_key_names:
        description:
            - None
        required: False
        type: list
        elements: str
    restricted_network:
        description:
            - None
        required: False
        type: bool
        default: False
    hostname:
        description:
            - None
        required: False
        type: str
    ssh_key_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    private_network_only:
        description:
            - None
        required: False
        type: bool
        default: False
    gpu_key_name:
        description:
            - None
        required: False
        type: str
    redundant_network:
        description:
            - None
        required: False
        type: bool
        default: False
    public_ipv4_address:
        description:
            - None
        required: False
        type: str
    ipv6_address_id:
        description:
            - None
        required: False
        type: int
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
    ('domain', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'tcp_monitoring',
    'private_subnet',
    'secondary_ip_count',
    'ipv6_static_enabled',
    'file_storage_ids',
    'datacenter',
    'network_speed',
    'memory',
    'storage_groups',
    'public_subnet',
    'global_identifier',
    'domain',
    'redundant_power_supply',
    'gpu_secondary_key_name',
    'private_ipv4_address_id',
    'secondary_ip_addresses',
    'notes',
    'post_install_script_uri',
    'os_key_name',
    'public_bandwidth',
    'quote_id',
    'private_vlan_id',
    'private_ipv4_address',
    'ipv6_enabled',
    'user_metadata',
    'os_reference_code',
    'image_template_id',
    'hourly_billing',
    'package_key_name',
    'unbonded_network',
    'block_storage_ids',
    'extended_hardware_testing',
    'public_vlan_id',
    'public_ipv4_address_id',
    'ipv6_address',
    'tags',
    'fixed_config_preset',
    'software_guard_extensions',
    'process_key_name',
    'disk_key_names',
    'restricted_network',
    'hostname',
    'ssh_key_ids',
    'private_network_only',
    'gpu_key_name',
    'redundant_network',
    'public_ipv4_address',
    'ipv6_address_id',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    tcp_monitoring=dict(
        default=False,
        type='bool'),
    private_subnet=dict(
        required=False,
        type='str'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    ipv6_static_enabled=dict(
        default=False,
        type='bool'),
    file_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    datacenter=dict(
        required=False,
        type='str'),
    network_speed=dict(
        default=100,
        type='int'),
    memory=dict(
        required=False,
        type='int'),
    storage_groups=dict(
        required=False,
        elements='',
        type='list'),
    public_subnet=dict(
        required=False,
        type='str'),
    global_identifier=dict(
        required=False,
        type='str'),
    domain=dict(
        required=False,
        type='str'),
    redundant_power_supply=dict(
        required=False,
        type='bool'),
    gpu_secondary_key_name=dict(
        required=False,
        type='str'),
    private_ipv4_address_id=dict(
        required=False,
        type='int'),
    secondary_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    notes=dict(
        required=False,
        type='str'),
    post_install_script_uri=dict(
        required=False,
        type='str'),
    os_key_name=dict(
        required=False,
        type='str'),
    public_bandwidth=dict(
        required=False,
        type='int'),
    quote_id=dict(
        required=False,
        type='int'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    private_ipv4_address=dict(
        required=False,
        type='str'),
    ipv6_enabled=dict(
        default=False,
        type='bool'),
    user_metadata=dict(
        required=False,
        type='str'),
    os_reference_code=dict(
        required=False,
        type='str'),
    image_template_id=dict(
        required=False,
        type='int'),
    hourly_billing=dict(
        default=True,
        type='bool'),
    package_key_name=dict(
        required=False,
        type='str'),
    unbonded_network=dict(
        default=False,
        type='bool'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    extended_hardware_testing=dict(
        default=False,
        type='bool'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    public_ipv4_address_id=dict(
        required=False,
        type='int'),
    ipv6_address=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    fixed_config_preset=dict(
        required=False,
        type='str'),
    software_guard_extensions=dict(
        default=False,
        type='bool'),
    process_key_name=dict(
        required=False,
        type='str'),
    disk_key_names=dict(
        required=False,
        elements='',
        type='list'),
    restricted_network=dict(
        default=False,
        type='bool'),
    hostname=dict(
        required=False,
        type='str'),
    ssh_key_ids=dict(
        required=False,
        elements='',
        type='list'),
    private_network_only=dict(
        default=False,
        type='bool'),
    gpu_key_name=dict(
        required=False,
        type='str'),
    redundant_network=dict(
        default=False,
        type='bool'),
    public_ipv4_address=dict(
        required=False,
        type='str'),
    ipv6_address_id=dict(
        required=False,
        type='int'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
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

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_compute_bare_metal',
        tf_type='resource',
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
