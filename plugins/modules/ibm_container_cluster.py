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

requirements:
    - IBM-Cloud terraform-provider-ibm v1.8.1
    - Terraform v0.12.20

options:
    account_guid:
        description:
            - The bluemix account guid this cluster belongs to
        required: False
        type: str
    default_pool_size:
        description:
            - The size of the default worker pool
        required: False
        type: int
        default: 1
    no_subnet:
        description:
            - Boolean value set to true when subnet creation is not required.
        required: False
        type: bool
        default: False
    wait_time_minutes:
        description:
            - None
        required: False
        type: int
    disk_encryption:
        description:
            - disc encryption done, if set to true.
        required: False
        type: bool
        default: True
    subnet_id:
        description:
            - List of subnet IDs
        required: False
        type: list
        elements: str
    datacenter:
        description:
            - (Required for new resource) The datacenter where this cluster will be deployed
        required: True
        type: str
    org_guid:
        description:
            - The bluemix organization guid this cluster belongs to
        required: False
        type: str
    worker_num:
        description:
            - Number of worker nodes
        required: False
        type: int
        default: 0
    space_guid:
        description:
            - The bluemix space guid this cluster belongs to
        required: False
        type: str
    billing:
        description:
            - None
        required: False
        type: str
    public_vlan_id:
        description:
            - Public VLAN ID
        required: False
        type: str
    is_trusted:
        description:
            - None
        required: False
        type: bool
    gateway_enabled:
        description:
            - Set true for gateway enabled clusters
        required: False
        type: bool
        default: False
    private_vlan_id:
        description:
            - Private VLAN ID
        required: False
        type: str
    webhook:
        description:
            - None
        required: False
        type: list
        elements: dict
    name:
        description:
            - (Required for new resource) The cluster name
        required: True
        type: str
    entitlement:
        description:
            - Entitlement option reduces additional OCP Licence cost in Openshift Clusters
        required: False
        type: str
    hardware:
        description:
            - (Required for new resource) Hardware type
        required: True
        type: str
    update_all_workers:
        description:
            - Updates all the woker nodes if sets to true
        required: False
        type: bool
        default: False
    machine_type:
        description:
            - Machine type
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
    ('datacenter', 'str'),
    ('name', 'str'),
    ('hardware', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'account_guid',
    'default_pool_size',
    'no_subnet',
    'wait_time_minutes',
    'disk_encryption',
    'subnet_id',
    'datacenter',
    'org_guid',
    'worker_num',
    'space_guid',
    'billing',
    'public_vlan_id',
    'is_trusted',
    'gateway_enabled',
    'private_vlan_id',
    'webhook',
    'name',
    'entitlement',
    'hardware',
    'update_all_workers',
    'machine_type',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    account_guid=dict(
        required= False,
        type='str'),
    default_pool_size=dict(
        default=1,
        type='int'),
    no_subnet=dict(
        default=False,
        type='bool'),
    wait_time_minutes=dict(
        required= False,
        type='int'),
    disk_encryption=dict(
        default=True,
        type='bool'),
    subnet_id=dict(
        required= False,
        elements='',
        type='list'),
    datacenter=dict(
        required= False,
        type='str'),
    org_guid=dict(
        required= False,
        type='str'),
    worker_num=dict(
        default=0,
        type='int'),
    space_guid=dict(
        required= False,
        type='str'),
    billing=dict(
        required= False,
        type='str'),
    public_vlan_id=dict(
        required= False,
        type='str'),
    is_trusted=dict(
        required= False,
        type='bool'),
    gateway_enabled=dict(
        default=False,
        type='bool'),
    private_vlan_id=dict(
        required= False,
        type='str'),
    webhook=dict(
        required= False,
        elements='',
        type='list'),
    name=dict(
        required= False,
        type='str'),
    entitlement=dict(
        required= False,
        type='str'),
    hardware=dict(
        required= False,
        type='str'),
    update_all_workers=dict(
        default=False,
        type='bool'),
    machine_type=dict(
        required= False,
        type='str'),
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

    result = ibmcloud_terraform(
        resource_type='ibm_container_cluster',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.8.1',
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
