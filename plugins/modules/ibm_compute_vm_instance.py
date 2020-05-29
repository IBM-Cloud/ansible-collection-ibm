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
    - IBM-Cloud terraform-provider-ibm v1.7.0
    - Terraform v0.12.20

options:
    post_install_script_uri:
        description:
            - None
        required: False
        type: str
    dedicated_host_name:
        description:
            - None
        required: False
        type: str
    private_subnet:
        description:
            - None
        required: False
        type: str
    ipv4_address:
        description:
            - None
        required: False
        type: str
    ipv4_address_private:
        description:
            - None
        required: False
        type: str
    domain:
        description:
            - None
        required: False
        type: str
    dedicated_acct_host_only:
        description:
            - None
        required: False
        type: bool
    private_interface_id:
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
    public_subnet:
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
    ipv6_address_id:
        description:
            - None
        required: False
        type: int
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    ip_address_id:
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
    local_disk:
        description:
            - None
        required: False
        type: bool
        default: True
    ip_address_id_private:
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
    hourly_billing:
        description:
            - None
        required: False
        type: bool
        default: True
    public_subnet_id:
        description:
            - None
        required: False
        type: int
    private_security_group_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    private_subnet_id:
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
    private_network_only:
        description:
            - None
        required: False
        type: bool
        default: False
    cores:
        description:
            - None
        required: False
        type: int
    datacenter:
        description:
            - None
        required: False
        type: str
    ipv6_address:
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
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance
        required: False
        type: str
    os_reference_code:
        description:
            - None
        required: False
        type: str
    transient:
        description:
            - None
        required: False
        type: bool
    public_vlan_id:
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
    memory:
        description:
            - None
        required: False
        type: int
    public_ipv6_subnet_id:
        description:
            - None
        required: False
        type: str
    secondary_ip_count:
        description:
            - None
        required: False
        type: int
    user_metadata:
        description:
            - None
        required: False
        type: str
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
    placement_group_id:
        description:
            - The placement group id
        required: False
        type: int
    flavor_key_name:
        description:
            - Flavor key name used to provision vm.
        required: False
        type: str
    ipv6_static_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    public_ipv6_subnet:
        description:
            - None
        required: False
        type: str
    wait_time_minutes:
        description:
            - None
        required: False
        type: int
        default: 90
    public_bandwidth_limited:
        description:
            - None
        required: False
        type: int
    public_interface_id:
        description:
            - None
        required: False
        type: int
    public_security_group_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    private_vlan_id:
        description:
            - None
        required: False
        type: int
    disks:
        description:
            - None
        required: False
        type: list
        elements: int
    placement_group_name:
        description:
            - The placement group name
        required: False
        type: str
    dedicated_host_id:
        description:
            - None
        required: False
        type: int
    notes:
        description:
            - None
        required: False
        type: str
    evault:
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
    'post_install_script_uri',
    'dedicated_host_name',
    'private_subnet',
    'ipv4_address',
    'ipv4_address_private',
    'domain',
    'dedicated_acct_host_only',
    'private_interface_id',
    'file_storage_ids',
    'hostname',
    'ssh_key_ids',
    'image_id',
    'resource_status',
    'public_subnet',
    'network_speed',
    'ipv6_address_id',
    'tags',
    'ip_address_id',
    'block_storage_ids',
    'local_disk',
    'ip_address_id_private',
    'bulk_vms',
    'hourly_billing',
    'public_subnet_id',
    'private_security_group_ids',
    'private_subnet_id',
    'public_bandwidth_unlimited',
    'private_network_only',
    'cores',
    'datacenter',
    'ipv6_address',
    'secondary_ip_addresses',
    'resource_controller_url',
    'os_reference_code',
    'transient',
    'public_vlan_id',
    'ipv6_enabled',
    'memory',
    'public_ipv6_subnet_id',
    'secondary_ip_count',
    'user_metadata',
    'resource_name',
    'datacenter_choice',
    'placement_group_id',
    'flavor_key_name',
    'ipv6_static_enabled',
    'public_ipv6_subnet',
    'wait_time_minutes',
    'public_bandwidth_limited',
    'public_interface_id',
    'public_security_group_ids',
    'private_vlan_id',
    'disks',
    'placement_group_name',
    'dedicated_host_id',
    'notes',
    'evault',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    post_install_script_uri=dict(
        required=False,
        type='str'),
    dedicated_host_name=dict(
        required=False,
        type='str'),
    private_subnet=dict(
        required=False,
        type='str'),
    ipv4_address=dict(
        required=False,
        type='str'),
    ipv4_address_private=dict(
        required=False,
        type='str'),
    domain=dict(
        required=False,
        type='str'),
    dedicated_acct_host_only=dict(
        required=False,
        type='bool'),
    private_interface_id=dict(
        required=False,
        type='int'),
    file_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    hostname=dict(
        required=False,
        type='str'),
    ssh_key_ids=dict(
        required=False,
        elements='',
        type='list'),
    image_id=dict(
        required=False,
        type='int'),
    resource_status=dict(
        required=False,
        type='str'),
    public_subnet=dict(
        required=False,
        type='str'),
    network_speed=dict(
        default=100,
        type='int'),
    ipv6_address_id=dict(
        required=False,
        type='int'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    ip_address_id=dict(
        required=False,
        type='int'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    local_disk=dict(
        default=True,
        type='bool'),
    ip_address_id_private=dict(
        required=False,
        type='int'),
    bulk_vms=dict(
        required=False,
        elements='',
        type='list'),
    hourly_billing=dict(
        default=True,
        type='bool'),
    public_subnet_id=dict(
        required=False,
        type='int'),
    private_security_group_ids=dict(
        required=False,
        elements='',
        type='list'),
    private_subnet_id=dict(
        required=False,
        type='int'),
    public_bandwidth_unlimited=dict(
        default=False,
        type='bool'),
    private_network_only=dict(
        default=False,
        type='bool'),
    cores=dict(
        required=False,
        type='int'),
    datacenter=dict(
        required=False,
        type='str'),
    ipv6_address=dict(
        required=False,
        type='str'),
    secondary_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    os_reference_code=dict(
        required=False,
        type='str'),
    transient=dict(
        required=False,
        type='bool'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    ipv6_enabled=dict(
        default=False,
        type='bool'),
    memory=dict(
        required=False,
        type='int'),
    public_ipv6_subnet_id=dict(
        required=False,
        type='str'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    user_metadata=dict(
        required=False,
        type='str'),
    resource_name=dict(
        required=False,
        type='str'),
    datacenter_choice=dict(
        required=False,
        elements='',
        type='list'),
    placement_group_id=dict(
        required=False,
        type='int'),
    flavor_key_name=dict(
        required=False,
        type='str'),
    ipv6_static_enabled=dict(
        default=False,
        type='bool'),
    public_ipv6_subnet=dict(
        required=False,
        type='str'),
    wait_time_minutes=dict(
        default=90,
        type='int'),
    public_bandwidth_limited=dict(
        required=False,
        type='int'),
    public_interface_id=dict(
        required=False,
        type='int'),
    public_security_group_ids=dict(
        required=False,
        elements='',
        type='list'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    disks=dict(
        required=False,
        elements='',
        type='list'),
    placement_group_name=dict(
        required=False,
        type='str'),
    dedicated_host_id=dict(
        required=False,
        type='int'),
    notes=dict(
        required=False,
        type='str'),
    evault=dict(
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
        resource_type='ibm_compute_vm_instance',
        tf_type='resource',
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
