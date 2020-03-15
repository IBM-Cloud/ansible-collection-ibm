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
    - IBM-Cloud terraform-provider-ibm v1.2.4
    - Terraform v0.12.20

options:
    private_subnet:
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
    disks:
        description:
            - None
        required: False
        type: list
        elements: int
    ipv6_static_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    secondary_ip_count:
        description:
            - None
        required: False
        type: int
    os_reference_code:
        description:
            - None
        required: False
        type: str
    ipv4_address:
        description:
            - None
        required: False
        type: str
    public_ipv6_subnet_id:
        description:
            - None
        required: False
        type: str
    image_id:
        description:
            - None
        required: False
        type: int
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    hostname:
        description:
            - None
        required: False
        type: str
    ipv6_address_id:
        description:
            - None
        required: False
        type: int
    post_install_script_uri:
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
    notes:
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
    evault:
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
    public_subnet:
        description:
            - None
        required: False
        type: str
    private_interface_id:
        description:
            - None
        required: False
        type: int
    cores:
        description:
            - None
        required: False
        type: int
    public_vlan_id:
        description:
            - None
        required: False
        type: int
    private_subnet_id:
        description:
            - None
        required: False
        type: int
    bulk_vms:
        description:
            - None
        required: False
        type: list
        elements: dict
    private_security_group_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    wait_time_minutes:
        description:
            - None
        required: False
        type: int
        default: 90
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance
        required: False
        type: str
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    private_network_only:
        description:
            - None
        required: False
        type: bool
        default: False
    placement_group_id:
        description:
            - The placement group id
        required: False
        type: int
    dedicated_acct_host_only:
        description:
            - None
        required: False
        type: bool
    flavor_key_name:
        description:
            - Flavor key name used to provision vm.
        required: False
        type: str
    local_disk:
        description:
            - None
        required: False
        type: bool
        default: True
    dedicated_host_name:
        description:
            - None
        required: False
        type: str
    public_security_group_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    ipv6_address:
        description:
            - None
        required: False
        type: str
    public_ipv6_subnet:
        description:
            - None
        required: False
        type: str
    public_bandwidth_limited:
        description:
            - None
        required: False
        type: int
    domain:
        description:
            - None
        required: False
        type: str
    placement_group_name:
        description:
            - The placement group name
        required: False
        type: str
    memory:
        description:
            - None
        required: False
        type: int
    public_bandwidth_unlimited:
        description:
            - None
        required: False
        type: bool
        default: False
    datacenter:
        description:
            - None
        required: False
        type: str
    dedicated_host_id:
        description:
            - None
        required: False
        type: int
    ipv4_address_private:
        description:
            - None
        required: False
        type: str
    ip_address_id_private:
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
    transient:
        description:
            - None
        required: False
        type: bool
    public_interface_id:
        description:
            - None
        required: False
        type: int
    public_subnet_id:
        description:
            - None
        required: False
        type: int
    ip_address_id:
        description:
            - None
        required: False
        type: int
    file_storage_ids:
        description:
            - None
        required: False
        type: list
        elements: int
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
    datacenter_choice:
        description:
            - The user provided datacenter options
        required: False
        type: list
        elements: dict
    private_vlan_id:
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
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'private_subnet',
    'ssh_key_ids',
    'disks',
    'ipv6_static_enabled',
    'secondary_ip_count',
    'os_reference_code',
    'ipv4_address',
    'public_ipv6_subnet_id',
    'image_id',
    'resource_status',
    'hostname',
    'ipv6_address_id',
    'post_install_script_uri',
    'network_speed',
    'notes',
    'tags',
    'evault',
    'hourly_billing',
    'public_subnet',
    'private_interface_id',
    'cores',
    'public_vlan_id',
    'private_subnet_id',
    'bulk_vms',
    'private_security_group_ids',
    'wait_time_minutes',
    'resource_controller_url',
    'resource_name',
    'private_network_only',
    'placement_group_id',
    'dedicated_acct_host_only',
    'flavor_key_name',
    'local_disk',
    'dedicated_host_name',
    'public_security_group_ids',
    'ipv6_address',
    'public_ipv6_subnet',
    'public_bandwidth_limited',
    'domain',
    'placement_group_name',
    'memory',
    'public_bandwidth_unlimited',
    'datacenter',
    'dedicated_host_id',
    'ipv4_address_private',
    'ip_address_id_private',
    'secondary_ip_addresses',
    'transient',
    'public_interface_id',
    'public_subnet_id',
    'ip_address_id',
    'file_storage_ids',
    'user_metadata',
    'block_storage_ids',
    'datacenter_choice',
    'private_vlan_id',
    'ipv6_enabled',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    private_subnet=dict(
        required=False,
        type='str'),
    ssh_key_ids=dict(
        required=False,
        elements='',
        type='list'),
    disks=dict(
        required=False,
        elements='',
        type='list'),
    ipv6_static_enabled=dict(
        default=False,
        type='bool'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    os_reference_code=dict(
        required=False,
        type='str'),
    ipv4_address=dict(
        required=False,
        type='str'),
    public_ipv6_subnet_id=dict(
        required=False,
        type='str'),
    image_id=dict(
        required=False,
        type='int'),
    resource_status=dict(
        required=False,
        type='str'),
    hostname=dict(
        required=False,
        type='str'),
    ipv6_address_id=dict(
        required=False,
        type='int'),
    post_install_script_uri=dict(
        required=False,
        type='str'),
    network_speed=dict(
        default=100,
        type='int'),
    notes=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    evault=dict(
        required=False,
        type='int'),
    hourly_billing=dict(
        default=True,
        type='bool'),
    public_subnet=dict(
        required=False,
        type='str'),
    private_interface_id=dict(
        required=False,
        type='int'),
    cores=dict(
        required=False,
        type='int'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    private_subnet_id=dict(
        required=False,
        type='int'),
    bulk_vms=dict(
        required=False,
        elements='',
        type='list'),
    private_security_group_ids=dict(
        required=False,
        elements='',
        type='list'),
    wait_time_minutes=dict(
        default=90,
        type='int'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    resource_name=dict(
        required=False,
        type='str'),
    private_network_only=dict(
        default=False,
        type='bool'),
    placement_group_id=dict(
        required=False,
        type='int'),
    dedicated_acct_host_only=dict(
        required=False,
        type='bool'),
    flavor_key_name=dict(
        required=False,
        type='str'),
    local_disk=dict(
        default=True,
        type='bool'),
    dedicated_host_name=dict(
        required=False,
        type='str'),
    public_security_group_ids=dict(
        required=False,
        elements='',
        type='list'),
    ipv6_address=dict(
        required=False,
        type='str'),
    public_ipv6_subnet=dict(
        required=False,
        type='str'),
    public_bandwidth_limited=dict(
        required=False,
        type='int'),
    domain=dict(
        required=False,
        type='str'),
    placement_group_name=dict(
        required=False,
        type='str'),
    memory=dict(
        required=False,
        type='int'),
    public_bandwidth_unlimited=dict(
        default=False,
        type='bool'),
    datacenter=dict(
        required=False,
        type='str'),
    dedicated_host_id=dict(
        required=False,
        type='int'),
    ipv4_address_private=dict(
        required=False,
        type='str'),
    ip_address_id_private=dict(
        required=False,
        type='int'),
    secondary_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    transient=dict(
        required=False,
        type='bool'),
    public_interface_id=dict(
        required=False,
        type='int'),
    public_subnet_id=dict(
        required=False,
        type='int'),
    ip_address_id=dict(
        required=False,
        type='int'),
    file_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    user_metadata=dict(
        required=False,
        type='str'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    datacenter_choice=dict(
        required=False,
        elements='',
        type='list'),
    private_vlan_id=dict(
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
        resource_type='ibm_compute_vm_instance',
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
