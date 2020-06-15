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
    - IBM-Cloud terraform-provider-ibm v1.7.1
    - Terraform v0.12.20

options:
    private_subnet:
        description:
            - None
        required: False
        type: str
    ipv6_address:
        description:
            - None
        required: False
        type: str
    ipv6_static_enabled:
        description:
            - boolean value true if ipv6 static is enabled else false
        required: False
        type: bool
        default: False
    tags:
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
    private_vlan_id:
        description:
            - None
        required: False
        type: int
    gpu_key_name:
        description:
            - None
        required: False
        type: str
    restricted_network:
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
    global_identifier:
        description:
            - The unique global identifier of the bare metal server
        required: False
        type: str
    fixed_config_preset:
        description:
            - Fixed config preset value
        required: False
        type: str
    image_template_id:
        description:
            - OS image template ID
        required: False
        type: int
    hourly_billing:
        description:
            - Enables hourly billing
        required: False
        type: bool
        default: True
    private_ipv4_address_id:
        description:
            - None
        required: False
        type: int
    block_storage_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    gpu_secondary_key_name:
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
    public_bandwidth:
        description:
            - None
        required: False
        type: int
    public_subnet:
        description:
            - None
        required: False
        type: str
    public_ipv4_address_id:
        description:
            - None
        required: False
        type: int
    private_ipv4_address:
        description:
            - None
        required: False
        type: str
    hostname:
        description:
            - Host name
        required: False
        type: str
    user_metadata:
        description:
            - User metadata info
        required: False
        type: str
    package_key_name:
        description:
            - None
        required: False
        type: str
    quote_id:
        description:
            - Quote ID for Quote based provisioning
        required: False
        type: int
    private_network_only:
        description:
            - only private network configured if is true
        required: False
        type: bool
        default: False
    process_key_name:
        description:
            - None
        required: False
        type: str
    memory:
        description:
            - None
        required: False
        type: int
    os_reference_code:
        description:
            - OS refernece code value
        required: False
        type: str
    datacenter:
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
    os_key_name:
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
    ssh_key_ids:
        description:
            - SSH KEY IDS list
        required: False
        type: list
        elements: int
    notes:
        description:
            - Optional notes info
        required: False
        type: str
    post_install_script_uri:
        description:
            - None
        required: False
        type: str
    redundant_power_supply:
        description:
            - None
        required: False
        type: bool
    redundant_network:
        description:
            - None
        required: False
        type: bool
        default: False
    ipv6_address_id:
        description:
            - None
        required: False
        type: int
    domain:
        description:
            - (Required for new resource) Domain name
        required: False
        type: str
    file_storage_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    tcp_monitoring:
        description:
            - TCP monitoring enabled if set as true
        required: False
        type: bool
        default: False
    secondary_ip_count:
        description:
            - Secondary IP addresses count
        required: False
        type: int
    secondary_ip_addresses:
        description:
            - None
        required: False
        type: list
        elements: str
    ipv6_enabled:
        description:
            - Boolean value true if IPV6 ia enabled or false
        required: False
        type: bool
        default: False
    network_speed:
        description:
            - Network speed in MBPS
        required: False
        type: int
        default: 100
    storage_groups:
        description:
            - None
        required: False
        type: list
        elements: dict
    public_ipv4_address:
        description:
            - None
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
    'private_subnet',
    'ipv6_address',
    'ipv6_static_enabled',
    'tags',
    'extended_hardware_testing',
    'private_vlan_id',
    'gpu_key_name',
    'restricted_network',
    'public_vlan_id',
    'global_identifier',
    'fixed_config_preset',
    'image_template_id',
    'hourly_billing',
    'private_ipv4_address_id',
    'block_storage_ids',
    'gpu_secondary_key_name',
    'disk_key_names',
    'public_bandwidth',
    'public_subnet',
    'public_ipv4_address_id',
    'private_ipv4_address',
    'hostname',
    'user_metadata',
    'package_key_name',
    'quote_id',
    'private_network_only',
    'process_key_name',
    'memory',
    'os_reference_code',
    'datacenter',
    'software_guard_extensions',
    'os_key_name',
    'unbonded_network',
    'ssh_key_ids',
    'notes',
    'post_install_script_uri',
    'redundant_power_supply',
    'redundant_network',
    'ipv6_address_id',
    'domain',
    'file_storage_ids',
    'tcp_monitoring',
    'secondary_ip_count',
    'secondary_ip_addresses',
    'ipv6_enabled',
    'network_speed',
    'storage_groups',
    'public_ipv4_address',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    private_subnet=dict(
        required=False,
        type='str'),
    ipv6_address=dict(
        required=False,
        type='str'),
    ipv6_static_enabled=dict(
        default=False,
        type='bool'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    extended_hardware_testing=dict(
        default=False,
        type='bool'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    gpu_key_name=dict(
        required=False,
        type='str'),
    restricted_network=dict(
        default=False,
        type='bool'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    global_identifier=dict(
        required=False,
        type='str'),
    fixed_config_preset=dict(
        required=False,
        type='str'),
    image_template_id=dict(
        required=False,
        type='int'),
    hourly_billing=dict(
        default=True,
        type='bool'),
    private_ipv4_address_id=dict(
        required=False,
        type='int'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    gpu_secondary_key_name=dict(
        required=False,
        type='str'),
    disk_key_names=dict(
        required=False,
        elements='',
        type='list'),
    public_bandwidth=dict(
        required=False,
        type='int'),
    public_subnet=dict(
        required=False,
        type='str'),
    public_ipv4_address_id=dict(
        required=False,
        type='int'),
    private_ipv4_address=dict(
        required=False,
        type='str'),
    hostname=dict(
        required=False,
        type='str'),
    user_metadata=dict(
        required=False,
        type='str'),
    package_key_name=dict(
        required=False,
        type='str'),
    quote_id=dict(
        required=False,
        type='int'),
    private_network_only=dict(
        default=False,
        type='bool'),
    process_key_name=dict(
        required=False,
        type='str'),
    memory=dict(
        required=False,
        type='int'),
    os_reference_code=dict(
        required=False,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    software_guard_extensions=dict(
        default=False,
        type='bool'),
    os_key_name=dict(
        required=False,
        type='str'),
    unbonded_network=dict(
        default=False,
        type='bool'),
    ssh_key_ids=dict(
        required=False,
        elements='',
        type='list'),
    notes=dict(
        required=False,
        type='str'),
    post_install_script_uri=dict(
        required=False,
        type='str'),
    redundant_power_supply=dict(
        required=False,
        type='bool'),
    redundant_network=dict(
        default=False,
        type='bool'),
    ipv6_address_id=dict(
        required=False,
        type='int'),
    domain=dict(
        required=False,
        type='str'),
    file_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    tcp_monitoring=dict(
        default=False,
        type='bool'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    secondary_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    ipv6_enabled=dict(
        default=False,
        type='bool'),
    network_speed=dict(
        default=100,
        type='int'),
    storage_groups=dict(
        required=False,
        elements='',
        type='list'),
    public_ipv4_address=dict(
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

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud_terraform(
        resource_type='ibm_compute_bare_metal',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.7.1',
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
