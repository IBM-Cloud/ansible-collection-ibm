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
    - IBM-Cloud terraform-provider-ibm v1.4.0
    - Terraform v0.12.20

options:
    storage_groups:
        description:
            - NA
        required: False
        type: list
        elements: dict
    public_vlan_id:
        description:
            - NA
        required: False
        type: int
    block_storage_ids:
        description:
            - NA
        required: False
        type: list
        elements: int
    image_template_id:
        description:
            - NA
        required: False
        type: int
    hourly_billing:
        description:
            - NA
        required: False
        type: bool
        default: True
    public_bandwidth:
        description:
            - NA
        required: False
        type: int
    datacenter:
        description:
            - NA
        required: False
        type: str
    gpu_key_name:
        description:
            - NA
        required: False
        type: str
    disk_key_names:
        description:
            - NA
        required: False
        type: list
        elements: str
    redundant_power_supply:
        description:
            - NA
        required: False
        type: bool
    private_vlan_id:
        description:
            - NA
        required: False
        type: int
    secondary_ip_addresses:
        description:
            - NA
        required: False
        type: list
        elements: str
    domain:
        description:
            - (Required for new resource) NA
        required: False
        type: str
    ssh_key_ids:
        description:
            - NA
        required: False
        type: list
        elements: int
    network_speed:
        description:
            - NA
        required: False
        type: int
        default: 100
    public_subnet:
        description:
            - NA
        required: False
        type: str
    private_subnet:
        description:
            - NA
        required: False
        type: str
    global_identifier:
        description:
            - The unique global identifier of the bare metal server
        required: False
        type: str
    tcp_monitoring:
        description:
            - NA
        required: False
        type: bool
        default: False
    software_guard_extensions:
        description:
            - NA
        required: False
        type: bool
        default: False
    extended_hardware_testing:
        description:
            - NA
        required: False
        type: bool
        default: False
    redundant_network:
        description:
            - NA
        required: False
        type: bool
        default: False
    restricted_network:
        description:
            - NA
        required: False
        type: bool
        default: False
    memory:
        description:
            - NA
        required: False
        type: int
    quote_id:
        description:
            - NA
        required: False
        type: int
    private_ipv4_address_id:
        description:
            - NA
        required: False
        type: int
    file_storage_ids:
        description:
            - NA
        required: False
        type: list
        elements: int
    tags:
        description:
            - NA
        required: False
        type: list
        elements: str
    gpu_secondary_key_name:
        description:
            - NA
        required: False
        type: str
    ipv6_enabled:
        description:
            - NA
        required: False
        type: bool
        default: False
    ipv6_address:
        description:
            - NA
        required: False
        type: str
    ipv6_static_enabled:
        description:
            - NA
        required: False
        type: bool
        default: False
    os_key_name:
        description:
            - NA
        required: False
        type: str
    private_ipv4_address:
        description:
            - NA
        required: False
        type: str
    user_metadata:
        description:
            - NA
        required: False
        type: str
    private_network_only:
        description:
            - NA
        required: False
        type: bool
        default: False
    package_key_name:
        description:
            - NA
        required: False
        type: str
    fixed_config_preset:
        description:
            - NA
        required: False
        type: str
    os_reference_code:
        description:
            - NA
        required: False
        type: str
    process_key_name:
        description:
            - NA
        required: False
        type: str
    secondary_ip_count:
        description:
            - NA
        required: False
        type: int
    hostname:
        description:
            - NA
        required: False
        type: str
    notes:
        description:
            - NA
        required: False
        type: str
    post_install_script_uri:
        description:
            - NA
        required: False
        type: str
    ipv6_address_id:
        description:
            - NA
        required: False
        type: int
    unbonded_network:
        description:
            - NA
        required: False
        type: bool
        default: False
    public_ipv4_address:
        description:
            - NA
        required: False
        type: str
    public_ipv4_address_id:
        description:
            - NA
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
    ('domain', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'storage_groups',
    'public_vlan_id',
    'block_storage_ids',
    'image_template_id',
    'hourly_billing',
    'public_bandwidth',
    'datacenter',
    'gpu_key_name',
    'disk_key_names',
    'redundant_power_supply',
    'private_vlan_id',
    'secondary_ip_addresses',
    'domain',
    'ssh_key_ids',
    'network_speed',
    'public_subnet',
    'private_subnet',
    'global_identifier',
    'tcp_monitoring',
    'software_guard_extensions',
    'extended_hardware_testing',
    'redundant_network',
    'restricted_network',
    'memory',
    'quote_id',
    'private_ipv4_address_id',
    'file_storage_ids',
    'tags',
    'gpu_secondary_key_name',
    'ipv6_enabled',
    'ipv6_address',
    'ipv6_static_enabled',
    'os_key_name',
    'private_ipv4_address',
    'user_metadata',
    'private_network_only',
    'package_key_name',
    'fixed_config_preset',
    'os_reference_code',
    'process_key_name',
    'secondary_ip_count',
    'hostname',
    'notes',
    'post_install_script_uri',
    'ipv6_address_id',
    'unbonded_network',
    'public_ipv4_address',
    'public_ipv4_address_id',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    storage_groups=dict(
        required=False,
        elements='',
        type='list'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    image_template_id=dict(
        required=False,
        type='int'),
    hourly_billing=dict(
        default=True,
        type='bool'),
    public_bandwidth=dict(
        required=False,
        type='int'),
    datacenter=dict(
        required=False,
        type='str'),
    gpu_key_name=dict(
        required=False,
        type='str'),
    disk_key_names=dict(
        required=False,
        elements='',
        type='list'),
    redundant_power_supply=dict(
        required=False,
        type='bool'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    secondary_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    domain=dict(
        required=False,
        type='str'),
    ssh_key_ids=dict(
        required=False,
        elements='',
        type='list'),
    network_speed=dict(
        default=100,
        type='int'),
    public_subnet=dict(
        required=False,
        type='str'),
    private_subnet=dict(
        required=False,
        type='str'),
    global_identifier=dict(
        required=False,
        type='str'),
    tcp_monitoring=dict(
        default=False,
        type='bool'),
    software_guard_extensions=dict(
        default=False,
        type='bool'),
    extended_hardware_testing=dict(
        default=False,
        type='bool'),
    redundant_network=dict(
        default=False,
        type='bool'),
    restricted_network=dict(
        default=False,
        type='bool'),
    memory=dict(
        required=False,
        type='int'),
    quote_id=dict(
        required=False,
        type='int'),
    private_ipv4_address_id=dict(
        required=False,
        type='int'),
    file_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    gpu_secondary_key_name=dict(
        required=False,
        type='str'),
    ipv6_enabled=dict(
        default=False,
        type='bool'),
    ipv6_address=dict(
        required=False,
        type='str'),
    ipv6_static_enabled=dict(
        default=False,
        type='bool'),
    os_key_name=dict(
        required=False,
        type='str'),
    private_ipv4_address=dict(
        required=False,
        type='str'),
    user_metadata=dict(
        required=False,
        type='str'),
    private_network_only=dict(
        default=False,
        type='bool'),
    package_key_name=dict(
        required=False,
        type='str'),
    fixed_config_preset=dict(
        required=False,
        type='str'),
    os_reference_code=dict(
        required=False,
        type='str'),
    process_key_name=dict(
        required=False,
        type='str'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    hostname=dict(
        required=False,
        type='str'),
    notes=dict(
        required=False,
        type='str'),
    post_install_script_uri=dict(
        required=False,
        type='str'),
    ipv6_address_id=dict(
        required=False,
        type='int'),
    unbonded_network=dict(
        default=False,
        type='bool'),
    public_ipv4_address=dict(
        required=False,
        type='str'),
    public_ipv4_address_id=dict(
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
        ibm_provider_version='1.4.0',
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
