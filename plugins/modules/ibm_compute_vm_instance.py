#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_vm_instance
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/compute_vm_instance

short_description: Configure IBM Cloud 'ibm_compute_vm_instance' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_compute_vm_instance' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.42.0
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
    datacenter_choice:
        description:
            - The user provided datacenter options
        required: False
        type: list
        elements: dict
    reserved_instance_primary_disk:
        description:
            - The primary disk of reserved instance
        required: False
        type: int
    reserved_capacity_id:
        description:
            - The reserved group id
        required: False
        type: int
    memory:
        description:
            - None
        required: False
        type: int
    dedicated_acct_host_only:
        description:
            - None
        required: False
        type: bool
    ipv6_static_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    public_bandwidth_unlimited:
        description:
            - None
        required: False
        type: bool
        default: False
    domain:
        description:
            - None
        required: False
        type: str
    placement_group_id:
        description:
            - The placement group id
        required: False
        type: int
    private_vlan_id:
        description:
            - None
        required: False
        type: int
    placement_group_name:
        description:
            - The placement group name
        required: False
        type: str
    hourly_billing:
        description:
            - None
        required: False
        type: bool
        default: True
    datacenter:
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
    bulk_vms:
        description:
            - None
        required: False
        type: list
        elements: dict
    private_network_only:
        description:
            - None
        required: False
        type: bool
        default: False
    public_subnet:
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
    cores:
        description:
            - None
        required: False
        type: int
    dedicated_host_id:
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
    network_speed:
        description:
            - None
        required: False
        type: int
        default: 100
    reserved_capacity_name:
        description:
            - The reserved group id
        required: False
        type: str
    notes:
        description:
            - None
        required: False
        type: str
    transient:
        description:
            - None
        required: False
        type: bool
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    dedicated_host_name:
        description:
            - None
        required: False
        type: str
    local_disk:
        description:
            - None
        required: False
        type: bool
        default: True
    quote_id:
        description:
            - Quote ID for Quote based provisioning
        required: False
        type: int
    public_vlan_id:
        description:
            - None
        required: False
        type: int
    private_subnet:
        description:
            - None
        required: False
        type: str
    evault:
        description:
            - None
        required: False
        type: int
    hostname:
        description:
            - None
        required: False
        type: str
    secondary_ip_count:
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
    user_metadata:
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
    ipv6_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    public_bandwidth_limited:
        description:
            - None
        required: False
        type: int
    flavor_key_name:
        description:
            - Flavor key name used to provision vm.
        required: False
        type: str
    image_id:
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
    'os_reference_code',
    'datacenter_choice',
    'reserved_instance_primary_disk',
    'reserved_capacity_id',
    'memory',
    'dedicated_acct_host_only',
    'ipv6_static_enabled',
    'public_bandwidth_unlimited',
    'domain',
    'placement_group_id',
    'private_vlan_id',
    'placement_group_name',
    'hourly_billing',
    'datacenter',
    'file_storage_ids',
    'bulk_vms',
    'private_network_only',
    'public_subnet',
    'block_storage_ids',
    'cores',
    'dedicated_host_id',
    'disks',
    'network_speed',
    'reserved_capacity_name',
    'notes',
    'transient',
    'tags',
    'dedicated_host_name',
    'local_disk',
    'quote_id',
    'public_vlan_id',
    'private_subnet',
    'evault',
    'hostname',
    'secondary_ip_count',
    'ssh_key_ids',
    'user_metadata',
    'public_security_group_ids',
    'ipv6_enabled',
    'public_bandwidth_limited',
    'flavor_key_name',
    'image_id',
    'private_security_group_ids',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('domain', 'str'),
    ('hostname', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'domain',
    'most_recent',
    'hostname',
]

TL_CONFLICTS_MAP = {
    'os_reference_code': ['image_id'],
    'datacenter_choice': ['datacenter', 'public_vlan_id', 'private_vlan_id', 'placement_group_name', 'placement_group_id', 'reserved_capacity_id', 'reserved_capacity_name'],
    'reserved_capacity_id': ['datacenter_choice', 'dedicated_acct_host_only', 'dedicated_host_name', 'dedicated_host_id', 'placement_group_name', 'placement_group_id', 'reserved_capacity_name', 'flavor_key_name', 'cores', 'memory'],
    'memory': ['flavor_key_name'],
    'dedicated_acct_host_only': ['dedicated_host_name', 'dedicated_host_id', 'placement_group_id', 'placement_group_name'],
    'public_bandwidth_unlimited': ['private_network_only', 'public_bandwidth_limited'],
    'domain': ['bulk_vms'],
    'placement_group_id': ['datacenter_choice', 'dedicated_acct_host_only', 'dedicated_host_name', 'dedicated_host_id', 'placement_group_name', 'reserved_capacity_id', 'reserved_capacity_name'],
    'private_vlan_id': ['datacenter_choice'],
    'placement_group_name': ['datacenter_choice', 'dedicated_acct_host_only', 'dedicated_host_name', 'dedicated_host_id', 'placement_group_id', 'reserved_capacity_id', 'reserved_capacity_name'],
    'datacenter': ['datacenter_choice'],
    'bulk_vms': ['hostname', 'domain'],
    'cores': ['flavor_key_name'],
    'dedicated_host_id': ['dedicated_acct_host_only', 'dedicated_host_name', 'placement_group_name', 'placement_group_id'],
    'reserved_capacity_name': ['datacenter_choice', 'dedicated_acct_host_only', 'dedicated_host_name', 'dedicated_host_id', 'placement_group_name', 'placement_group_id', 'reserved_capacity_id', 'flavor_key_name', 'cores', 'memory'],
    'transient': ['dedicated_acct_host_only', 'dedicated_host_name', 'dedicated_host_id', 'cores', 'memory', 'public_bandwidth_limited', 'public_bandwidth_unlimited'],
    'dedicated_host_name': ['dedicated_acct_host_only', 'dedicated_host_id', 'placement_group_name', 'placement_group_id'],
    'public_vlan_id': ['datacenter_choice'],
    'hostname': ['bulk_vms'],
    'public_bandwidth_limited': ['private_network_only', 'public_bandwidth_unlimited'],
    'flavor_key_name': ['cores', 'memory'],
    'image_id': ['os_reference_code'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    post_install_script_uri=dict(
        required=False,
        type='str'),
    os_reference_code=dict(
        required=False,
        type='str'),
    datacenter_choice=dict(
        required=False,
        elements='',
        type='list'),
    reserved_instance_primary_disk=dict(
        required=False,
        type='int'),
    reserved_capacity_id=dict(
        required=False,
        type='int'),
    memory=dict(
        required=False,
        type='int'),
    dedicated_acct_host_only=dict(
        required=False,
        type='bool'),
    ipv6_static_enabled=dict(
        required=False,
        type='bool'),
    public_bandwidth_unlimited=dict(
        required=False,
        type='bool'),
    domain=dict(
        required=False,
        type='str'),
    placement_group_id=dict(
        required=False,
        type='int'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    placement_group_name=dict(
        required=False,
        type='str'),
    hourly_billing=dict(
        required=False,
        type='bool'),
    datacenter=dict(
        required=False,
        type='str'),
    file_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    bulk_vms=dict(
        required=False,
        elements='',
        type='list'),
    private_network_only=dict(
        required=False,
        type='bool'),
    public_subnet=dict(
        required=False,
        type='str'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    cores=dict(
        required=False,
        type='int'),
    dedicated_host_id=dict(
        required=False,
        type='int'),
    disks=dict(
        required=False,
        elements='',
        type='list'),
    network_speed=dict(
        required=False,
        type='int'),
    reserved_capacity_name=dict(
        required=False,
        type='str'),
    notes=dict(
        required=False,
        type='str'),
    transient=dict(
        required=False,
        type='bool'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    dedicated_host_name=dict(
        required=False,
        type='str'),
    local_disk=dict(
        required=False,
        type='bool'),
    quote_id=dict(
        required=False,
        type='int'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    private_subnet=dict(
        required=False,
        type='str'),
    evault=dict(
        required=False,
        type='int'),
    hostname=dict(
        required=False,
        type='str'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    ssh_key_ids=dict(
        required=False,
        elements='',
        type='list'),
    user_metadata=dict(
        required=False,
        type='str'),
    public_security_group_ids=dict(
        required=False,
        elements='',
        type='list'),
    ipv6_enabled=dict(
        required=False,
        type='bool'),
    public_bandwidth_limited=dict(
        required=False,
        type='int'),
    flavor_key_name=dict(
        required=False,
        type='str'),
    image_id=dict(
        required=False,
        type='int'),
    private_security_group_ids=dict(
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

    result_ds = ibmcloud_terraform(
        resource_type='ibm_compute_vm_instance',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.42.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_compute_vm_instance',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.42.0',
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
