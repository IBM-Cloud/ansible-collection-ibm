#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_cluster
short_description: Configure IBM Cloud 'ibm_container_cluster' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_cluster' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.9.0
    - Terraform v0.12.20

options:
    disk_encryption:
        description:
            - disc encryption done, if set to true.
        required: False
        type: bool
        default: True
    no_subnet:
        description:
            - Boolean value set to true when subnet creation is not required.
        required: False
        type: bool
        default: False
    is_trusted:
        description:
            - None
        required: False
        type: bool
    subnet_id:
        description:
            - List of subnet IDs
        required: False
        type: list
        elements: str
    worker_num:
        description:
            - Number of worker nodes
        required: False
        type: int
        default: 0
    machine_type:
        description:
            - Machine type
        required: False
        type: str
    hardware:
        description:
            - (Required for new resource) Hardware type
        required: True
        type: str
    webhook:
        description:
            - None
        required: False
        type: list
        elements: dict
    private_vlan_id:
        description:
            - Private VLAN ID
        required: False
        type: str
    account_guid:
        description:
            - The bluemix account guid this cluster belongs to
        required: False
        type: str
    update_all_workers:
        description:
            - Updates all the woker nodes if sets to true
        required: False
        type: bool
        default: False
    billing:
        description:
            - None
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The cluster name
        required: True
        type: str
    space_guid:
        description:
            - The bluemix space guid this cluster belongs to
        required: False
        type: str
    wait_time_minutes:
        description:
            - None
        required: False
        type: int
    datacenter:
        description:
            - (Required for new resource) The datacenter where this cluster will be deployed
        required: True
        type: str
    default_pool_size:
        description:
            - The size of the default worker pool
        required: False
        type: int
        default: 1
    public_vlan_id:
        description:
            - Public VLAN ID
        required: False
        type: str
    entitlement:
        description:
            - Entitlement option reduces additional OCP Licence cost in Openshift Clusters
        required: False
        type: str
    org_guid:
        description:
            - The bluemix organization guid this cluster belongs to
        required: False
        type: str
    gateway_enabled:
        description:
            - Set true for gateway enabled clusters
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
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('hardware', 'str'),
    ('name', 'str'),
    ('datacenter', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'disk_encryption',
    'no_subnet',
    'is_trusted',
    'subnet_id',
    'worker_num',
    'machine_type',
    'hardware',
    'webhook',
    'private_vlan_id',
    'account_guid',
    'update_all_workers',
    'billing',
    'name',
    'space_guid',
    'wait_time_minutes',
    'datacenter',
    'default_pool_size',
    'public_vlan_id',
    'entitlement',
    'org_guid',
    'gateway_enabled',
]

# Params for Data source 
TL_REQUIRED_PARAMETERS_DS = [
    ('cluster_name_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'cluster_name_id',
]

TL_CONFLICTS_MAP = {
    'worker_num':  ['workers'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    disk_encryption=dict(
        required= False,
        type='bool'),
    no_subnet=dict(
        required= False,
        type='bool'),
    is_trusted=dict(
        required= False,
        type='bool'),
    subnet_id=dict(
        required= False,
        elements='',
        type='list'),
    worker_num=dict(
        required= False,
        type='int'),
    machine_type=dict(
        required= False,
        type='str'),
    hardware=dict(
        required= False,
        type='str'),
    webhook=dict(
        required= False,
        elements='',
        type='list'),
    private_vlan_id=dict(
        required= False,
        type='str'),
    account_guid=dict(
        required= False,
        type='str'),
    update_all_workers=dict(
        required= False,
        type='bool'),
    billing=dict(
        required= False,
        type='str'),
    name=dict(
        required= False,
        type='str'),
    space_guid=dict(
        required= False,
        type='str'),
    wait_time_minutes=dict(
        required= False,
        type='int'),
    datacenter=dict(
        required= False,
        type='str'),
    default_pool_size=dict(
        required= False,
        type='int'),
    public_vlan_id=dict(
        required= False,
        type='str'),
    entitlement=dict(
        required= False,
        type='str'),
    org_guid=dict(
        required= False,
        type='str'),
    gateway_enabled=dict(
        required= False,
        type='bool'),
    id=dict(
        required= False,
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
         module.fail_json(msg=("conflicts exists: {}".format(conflicts)))

    result_ds = ibmcloud_terraform(
        resource_type='ibm_container_cluster',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.9.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] != None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_container_cluster',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.9.0',
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
