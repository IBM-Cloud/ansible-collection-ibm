#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_vm_instance
short_description: Configure IBM Cloud 'ibm_compute_vm_instance' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_compute_vm_instance' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.4.0
    - Terraform v0.12.20

options:
    public_ipv6_subnet_id:
        description:
            - NA
        required: False
        type: str
    secondary_ip_addresses:
        description:
            - NA
        required: False
        type: list
        elements: str
    notes:
        description:
            - NA
        required: False
        type: str
    image_id:
        description:
            - NA
        required: False
        type: int
    os_reference_code:
        description:
            - NA
        required: False
        type: str
    flavor_key_name:
        description:
            - Flavor key name used to provision vm.
        required: False
        type: str
    transient:
        description:
            - NA
        required: False
        type: bool
    ipv4_address_private:
        description:
            - NA
        required: False
        type: str
    public_bandwidth_limited:
        description:
            - NA
        required: False
        type: int
    dedicated_acct_host_only:
        description:
            - NA
        required: False
        type: bool
    public_security_group_ids:
        description:
            - NA
        required: False
        type: list
        elements: int
    ipv6_address:
        description:
            - NA
        required: False
        type: str
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    private_network_only:
        description:
            - NA
        required: False
        type: bool
        default: False
    secondary_ip_count:
        description:
            - NA
        required: False
        type: int
    public_bandwidth_unlimited:
        description:
            - NA
        required: False
        type: bool
        default: False
    evault:
        description:
            - NA
        required: False
        type: int
    domain:
        description:
            - NA
        required: False
        type: str
    memory:
        description:
            - NA
        required: False
        type: int
    public_interface_id:
        description:
            - NA
        required: False
        type: int
    ssh_key_ids:
        description:
            - NA
        required: False
        type: list
        elements: int
    private_subnet:
        description:
            - NA
        required: False
        type: str
    private_security_group_ids:
        description:
            - NA
        required: False
        type: list
        elements: int
    local_disk:
        description:
            - NA
        required: False
        type: bool
        default: True
    ipv6_static_enabled:
        description:
            - NA
        required: False
        type: bool
        default: False
    block_storage_ids:
        description:
            - NA
        required: False
        type: list
        elements: int
    cores:
        description:
            - NA
        required: False
        type: int
    dedicated_host_name:
        description:
            - NA
        required: False
        type: str
    public_vlan_id:
        description:
            - NA
        required: False
        type: int
    public_subnet:
        description:
            - NA
        required: False
        type: str
    private_interface_id:
        description:
            - NA
        required: False
        type: int
    network_speed:
        description:
            - NA
        required: False
        type: int
        default: 100
    user_metadata:
        description:
            - NA
        required: False
        type: str
    hostname:
        description:
            - NA
        required: False
        type: str
    private_vlan_id:
        description:
            - NA
        required: False
        type: int
    public_ipv6_subnet:
        description:
            - NA
        required: False
        type: str
    private_subnet_id:
        description:
            - NA
        required: False
        type: int
    ip_address_id:
        description:
            - NA
        required: False
        type: int
    placement_group_id:
        description:
            - The placement group id
        required: False
        type: int
    ipv6_address_id:
        description:
            - NA
        required: False
        type: int
    post_install_script_uri:
        description:
            - NA
        required: False
        type: str
    disks:
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
    bulk_vms:
        description:
            - NA
        required: False
        type: list
        elements: dict
    datacenter:
        description:
            - NA
        required: False
        type: str
    placement_group_name:
        description:
            - The placement group name
        required: False
        type: str
    dedicated_host_id:
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
    ip_address_id_private:
        description:
            - NA
        required: False
        type: int
    wait_time_minutes:
        description:
            - NA
        required: False
        type: int
        default: 90
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    datacenter_choice:
        description:
            - The user provided datacenter options
        required: False
        type: list
        elements: dict
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance
        required: False
        type: str
    public_subnet_id:
        description:
            - NA
        required: False
        type: int
    ipv4_address:
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
    file_storage_ids:
        description:
            - NA
        required: False
        type: list
        elements: int
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
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'public_ipv6_subnet_id',
    'secondary_ip_addresses',
    'notes',
    'image_id',
    'os_reference_code',
    'flavor_key_name',
    'transient',
    'ipv4_address_private',
    'public_bandwidth_limited',
    'dedicated_acct_host_only',
    'public_security_group_ids',
    'ipv6_address',
    'resource_status',
    'private_network_only',
    'secondary_ip_count',
    'public_bandwidth_unlimited',
    'evault',
    'domain',
    'memory',
    'public_interface_id',
    'ssh_key_ids',
    'private_subnet',
    'private_security_group_ids',
    'local_disk',
    'ipv6_static_enabled',
    'block_storage_ids',
    'cores',
    'dedicated_host_name',
    'public_vlan_id',
    'public_subnet',
    'private_interface_id',
    'network_speed',
    'user_metadata',
    'hostname',
    'private_vlan_id',
    'public_ipv6_subnet',
    'private_subnet_id',
    'ip_address_id',
    'placement_group_id',
    'ipv6_address_id',
    'post_install_script_uri',
    'disks',
    'tags',
    'bulk_vms',
    'datacenter',
    'placement_group_name',
    'dedicated_host_id',
    'hourly_billing',
    'ip_address_id_private',
    'wait_time_minutes',
    'resource_name',
    'datacenter_choice',
    'resource_controller_url',
    'public_subnet_id',
    'ipv4_address',
    'ipv6_enabled',
    'file_storage_ids',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    public_ipv6_subnet_id=dict(
        required=False,
        type='str'),
    secondary_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    notes=dict(
        required=False,
        type='str'),
    image_id=dict(
        required=False,
        type='int'),
    os_reference_code=dict(
        required=False,
        type='str'),
    flavor_key_name=dict(
        required=False,
        type='str'),
    transient=dict(
        required=False,
        type='bool'),
    ipv4_address_private=dict(
        required=False,
        type='str'),
    public_bandwidth_limited=dict(
        required=False,
        type='int'),
    dedicated_acct_host_only=dict(
        required=False,
        type='bool'),
    public_security_group_ids=dict(
        required=False,
        elements='',
        type='list'),
    ipv6_address=dict(
        required=False,
        type='str'),
    resource_status=dict(
        required=False,
        type='str'),
    private_network_only=dict(
        default=False,
        type='bool'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    public_bandwidth_unlimited=dict(
        default=False,
        type='bool'),
    evault=dict(
        required=False,
        type='int'),
    domain=dict(
        required=False,
        type='str'),
    memory=dict(
        required=False,
        type='int'),
    public_interface_id=dict(
        required=False,
        type='int'),
    ssh_key_ids=dict(
        required=False,
        elements='',
        type='list'),
    private_subnet=dict(
        required=False,
        type='str'),
    private_security_group_ids=dict(
        required=False,
        elements='',
        type='list'),
    local_disk=dict(
        default=True,
        type='bool'),
    ipv6_static_enabled=dict(
        default=False,
        type='bool'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    cores=dict(
        required=False,
        type='int'),
    dedicated_host_name=dict(
        required=False,
        type='str'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    public_subnet=dict(
        required=False,
        type='str'),
    private_interface_id=dict(
        required=False,
        type='int'),
    network_speed=dict(
        default=100,
        type='int'),
    user_metadata=dict(
        required=False,
        type='str'),
    hostname=dict(
        required=False,
        type='str'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    public_ipv6_subnet=dict(
        required=False,
        type='str'),
    private_subnet_id=dict(
        required=False,
        type='int'),
    ip_address_id=dict(
        required=False,
        type='int'),
    placement_group_id=dict(
        required=False,
        type='int'),
    ipv6_address_id=dict(
        required=False,
        type='int'),
    post_install_script_uri=dict(
        required=False,
        type='str'),
    disks=dict(
        required=False,
        elements='',
        type='list'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    bulk_vms=dict(
        required=False,
        elements='',
        type='list'),
    datacenter=dict(
        required=False,
        type='str'),
    placement_group_name=dict(
        required=False,
        type='str'),
    dedicated_host_id=dict(
        required=False,
        type='int'),
    hourly_billing=dict(
        default=True,
        type='bool'),
    ip_address_id_private=dict(
        required=False,
        type='int'),
    wait_time_minutes=dict(
        default=90,
        type='int'),
    resource_name=dict(
        required=False,
        type='str'),
    datacenter_choice=dict(
        required=False,
        elements='',
        type='list'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    public_subnet_id=dict(
        required=False,
        type='int'),
    ipv4_address=dict(
        required=False,
        type='str'),
    ipv6_enabled=dict(
        default=False,
        type='bool'),
    file_storage_ids=dict(
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
        resource_type='ibm_compute_vm_instance',
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
