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
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.21.2
    - Terraform v0.12.20

options:
    domain:
        description:
            - None
        required: False
        type: str
    os_reference_code:
        description:
            - None
        required: False
        type: str
    placement_group_name:
        description:
            - The placement group name
        required: False
        type: str
    public_subnet:
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
    post_install_script_uri:
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
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    user_metadata:
        description:
            - None
        required: False
        type: str
    hostname:
        description:
            - None
        required: False
        type: str
    memory:
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
    ipv6_static_enabled:
        description:
            - None
        required: False
        type: bool
        default: False
    ipv6_enabled:
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
    private_subnet:
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
    bulk_vms:
        description:
            - None
        required: False
        type: list
        elements: dict
    dedicated_host_name:
        description:
            - None
        required: False
        type: str
    private_security_group_ids:
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
    dedicated_host_id:
        description:
            - None
        required: False
        type: int
    public_vlan_id:
        description:
            - None
        required: False
        type: int
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
    notes:
        description:
            - None
        required: False
        type: str
    private_network_only:
        description:
            - None
        required: False
        type: bool
        default: False
    datacenter_choice:
        description:
            - The user provided datacenter options
        required: False
        type: list
        elements: dict
    dedicated_acct_host_only:
        description:
            - None
        required: False
        type: bool
    file_storage_ids:
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
    public_bandwidth_limited:
        description:
            - None
        required: False
        type: int
    transient:
        description:
            - None
        required: False
        type: bool
    secondary_ip_count:
        description:
            - None
        required: False
        type: int
    cores:
        description:
            - None
        required: False
        type: int
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
    'domain',
    'os_reference_code',
    'placement_group_name',
    'public_subnet',
    'ssh_key_ids',
    'post_install_script_uri',
    'local_disk',
    'tags',
    'user_metadata',
    'hostname',
    'memory',
    'public_security_group_ids',
    'ipv6_static_enabled',
    'ipv6_enabled',
    'public_bandwidth_unlimited',
    'private_subnet',
    'block_storage_ids',
    'bulk_vms',
    'dedicated_host_name',
    'private_security_group_ids',
    'hourly_billing',
    'datacenter',
    'network_speed',
    'placement_group_id',
    'flavor_key_name',
    'dedicated_host_id',
    'public_vlan_id',
    'private_vlan_id',
    'disks',
    'notes',
    'private_network_only',
    'datacenter_choice',
    'dedicated_acct_host_only',
    'file_storage_ids',
    'image_id',
    'public_bandwidth_limited',
    'transient',
    'secondary_ip_count',
    'cores',
    'evault',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('hostname', 'str'),
    ('domain', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'hostname',
    'most_recent',
    'domain',
]

TL_CONFLICTS_MAP = {
    'domain': ['bulk_vms'],
    'os_reference_code': ['image_id'],
    'placement_group_name': ['datacenter_choice', 'dedicated_acct_host_only', 'dedicated_host_name', 'dedicated_host_id', 'placement_group_id'],
    'hostname': ['bulk_vms'],
    'memory': ['flavor_key_name'],
    'public_bandwidth_unlimited': ['private_network_only', 'public_bandwidth_limited'],
    'bulk_vms': ['hostname', 'domain'],
    'dedicated_host_name': ['dedicated_acct_host_only', 'dedicated_host_id', 'placement_group_name', 'placement_group_id'],
    'datacenter': ['datacenter_choice'],
    'placement_group_id': ['datacenter_choice', 'dedicated_acct_host_only', 'dedicated_host_name', 'dedicated_host_id', 'placement_group_name'],
    'flavor_key_name': ['cores', 'memory'],
    'dedicated_host_id': ['dedicated_acct_host_only', 'dedicated_host_name', 'placement_group_name', 'placement_group_id'],
    'public_vlan_id': ['datacenter_choice'],
    'private_vlan_id': ['datacenter_choice'],
    'datacenter_choice': ['datacenter', 'public_vlan_id', 'private_vlan_id', 'placement_group_name', 'placement_group_id'],
    'dedicated_acct_host_only': ['dedicated_host_name', 'dedicated_host_id', 'placement_group_id', 'placement_group_name'],
    'image_id': ['os_reference_code'],
    'public_bandwidth_limited': ['private_network_only', 'public_bandwidth_unlimited'],
    'transient': ['dedicated_acct_host_only', 'dedicated_host_name', 'dedicated_host_id', 'cores', 'memory', 'public_bandwidth_limited', 'public_bandwidth_unlimited'],
    'cores': ['flavor_key_name'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    domain=dict(
        required=False,
        type='str'),
    os_reference_code=dict(
        required=False,
        type='str'),
    placement_group_name=dict(
        required=False,
        type='str'),
    public_subnet=dict(
        required=False,
        type='str'),
    ssh_key_ids=dict(
        required=False,
        elements='',
        type='list'),
    post_install_script_uri=dict(
        required=False,
        type='str'),
    local_disk=dict(
        required=False,
        type='bool'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    user_metadata=dict(
        required=False,
        type='str'),
    hostname=dict(
        required=False,
        type='str'),
    memory=dict(
        required=False,
        type='int'),
    public_security_group_ids=dict(
        required=False,
        elements='',
        type='list'),
    ipv6_static_enabled=dict(
        required=False,
        type='bool'),
    ipv6_enabled=dict(
        required=False,
        type='bool'),
    public_bandwidth_unlimited=dict(
        required=False,
        type='bool'),
    private_subnet=dict(
        required=False,
        type='str'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    bulk_vms=dict(
        required=False,
        elements='',
        type='list'),
    dedicated_host_name=dict(
        required=False,
        type='str'),
    private_security_group_ids=dict(
        required=False,
        elements='',
        type='list'),
    hourly_billing=dict(
        required=False,
        type='bool'),
    datacenter=dict(
        required=False,
        type='str'),
    network_speed=dict(
        required=False,
        type='int'),
    placement_group_id=dict(
        required=False,
        type='int'),
    flavor_key_name=dict(
        required=False,
        type='str'),
    dedicated_host_id=dict(
        required=False,
        type='int'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    disks=dict(
        required=False,
        elements='',
        type='list'),
    notes=dict(
        required=False,
        type='str'),
    private_network_only=dict(
        required=False,
        type='bool'),
    datacenter_choice=dict(
        required=False,
        elements='',
        type='list'),
    dedicated_acct_host_only=dict(
        required=False,
        type='bool'),
    file_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    image_id=dict(
        required=False,
        type='int'),
    public_bandwidth_limited=dict(
        required=False,
        type='int'),
    transient=dict(
        required=False,
        type='bool'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    cores=dict(
        required=False,
        type='int'),
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
        ibm_provider_version='1.21.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_compute_vm_instance',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.21.2',
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
