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
    - IBM-Cloud terraform-provider-ibm v1.2.4
    - Terraform v0.12.20

options:
    post_install_script_uri:
        description:
            - None
        required: False
        type: str
    os_reference_code:
        description:
            - None
        required: False
        type: str
    gpu_key_name:
        description:
            - None
        required: False
        type: str
    memory:
        description:
            - None
        required: False
        type: int
    public_ipv4_address:
        description:
            - None
        required: False
        type: str
    file_storage_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    hourly_billing:
        description:
            - None
        required: False
        type: bool
        default: True
    redundant_power_supply:
        description:
            - None
        required: False
        type: bool
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
    ipv6_address_id:
        description:
            - None
        required: False
        type: int
    ssh_key_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    network_speed:
        description:
            - None
        required: False
        type: int
        default: 100
    tcp_monitoring:
        description:
            - None
        required: False
        type: bool
        default: False
    package_key_name:
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
    ipv6_static_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    global_identifier:
        description:
            - The unique global identifier of the bare metal server
        required: False
        type: str
    user_metadata:
        description:
            - None
        required: False
        type: str
    block_storage_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    image_template_id:
        description:
            - None
        required: False
        type: int
    public_subnet:
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
    datacenter:
        description:
            - None
        required: False
        type: str
    process_key_name:
        description:
            - None
        required: False
        type: str
    os_key_name:
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
    extended_hardware_testing:
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
    private_ipv4_address_id:
        description:
            - None
        required: False
        type: int
    domain:
        description:
            - (Required for new resource) 
        required: False
        type: str
    private_network_only:
        description:
            - None
        required: False
        type: bool
        default: False
    software_guard_extensions:
        description:
            - None
        required: False
        type: bool
        default: False
    gpu_secondary_key_name:
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
    secondary_ip_addresses:
        description:
            - None
        required: False
        type: list
        elements: str
    ipv6_address:
        description:
            - None
        required: False
        type: str
    notes:
        description:
            - None
        required: False
        type: str
    public_bandwidth:
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
    secondary_ip_count:
        description:
            - None
        required: False
        type: int
    ipv6_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
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
            - The API Key used for authentification. This can also be 
              provided via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone 
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
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
    'post_install_script_uri',
    'os_reference_code',
    'gpu_key_name',
    'memory',
    'public_ipv4_address',
    'file_storage_ids',
    'hourly_billing',
    'redundant_power_supply',
    'public_vlan_id',
    'public_ipv4_address_id',
    'ipv6_address_id',
    'ssh_key_ids',
    'network_speed',
    'tcp_monitoring',
    'package_key_name',
    'redundant_network',
    'ipv6_static_enabled',
    'global_identifier',
    'user_metadata',
    'block_storage_ids',
    'image_template_id',
    'public_subnet',
    'tags',
    'fixed_config_preset',
    'datacenter',
    'process_key_name',
    'os_key_name',
    'disk_key_names',
    'extended_hardware_testing',
    'private_subnet',
    'private_ipv4_address_id',
    'domain',
    'private_network_only',
    'software_guard_extensions',
    'gpu_secondary_key_name',
    'unbonded_network',
    'restricted_network',
    'hostname',
    'quote_id',
    'private_vlan_id',
    'private_ipv4_address',
    'secondary_ip_addresses',
    'ipv6_address',
    'notes',
    'public_bandwidth',
    'storage_groups',
    'secondary_ip_count',
    'ipv6_enabled',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    post_install_script_uri=dict(
        required=False,
        type='str'),
    os_reference_code=dict(
        required=False,
        type='str'),
    gpu_key_name=dict(
        required=False,
        type='str'),
    memory=dict(
        required=False,
        type='int'),
    public_ipv4_address=dict(
        required=False,
        type='str'),
    file_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    hourly_billing=dict(
        default=True,
        type='bool'),
    redundant_power_supply=dict(
        required=False,
        type='bool'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    public_ipv4_address_id=dict(
        required=False,
        type='int'),
    ipv6_address_id=dict(
        required=False,
        type='int'),
    ssh_key_ids=dict(
        required=False,
        elements='',
        type='list'),
    network_speed=dict(
        default=100,
        type='int'),
    tcp_monitoring=dict(
        default=False,
        type='bool'),
    package_key_name=dict(
        required=False,
        type='str'),
    redundant_network=dict(
        default=False,
        type='bool'),
    ipv6_static_enabled=dict(
        default=False,
        type='bool'),
    global_identifier=dict(
        required=False,
        type='str'),
    user_metadata=dict(
        required=False,
        type='str'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    image_template_id=dict(
        required=False,
        type='int'),
    public_subnet=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    fixed_config_preset=dict(
        required=False,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    process_key_name=dict(
        required=False,
        type='str'),
    os_key_name=dict(
        required=False,
        type='str'),
    disk_key_names=dict(
        required=False,
        elements='',
        type='list'),
    extended_hardware_testing=dict(
        default=False,
        type='bool'),
    private_subnet=dict(
        required=False,
        type='str'),
    private_ipv4_address_id=dict(
        required=False,
        type='int'),
    domain=dict(
        required=False,
        type='str'),
    private_network_only=dict(
        default=False,
        type='bool'),
    software_guard_extensions=dict(
        default=False,
        type='bool'),
    gpu_secondary_key_name=dict(
        required=False,
        type='str'),
    unbonded_network=dict(
        default=False,
        type='bool'),
    restricted_network=dict(
        default=False,
        type='bool'),
    hostname=dict(
        required=False,
        type='str'),
    quote_id=dict(
        required=False,
        type='int'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    private_ipv4_address=dict(
        required=False,
        type='str'),
    secondary_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    ipv6_address=dict(
        required=False,
        type='str'),
    notes=dict(
        required=False,
        type='str'),
    public_bandwidth=dict(
        required=False,
        type='int'),
    storage_groups=dict(
        required=False,
        elements='',
        type='list'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    ipv6_enabled=dict(
        default=False,
        type='bool'),
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
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
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
        ibm_provider_version='1.2.4',
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
