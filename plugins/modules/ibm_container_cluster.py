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
    - IBM-Cloud terraform-provider-ibm v1.4.0
    - Terraform v0.12.20

options:
    ingress_secret:
        description:
            - NA
        required: False
        type: str
    no_subnet:
        description:
            - NA
        required: False
        type: bool
        default: False
    webhook:
        description:
            - NA
        required: False
        type: list
        elements: dict
    public_service_endpoint_url:
        description:
            - NA
        required: False
        type: str
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    ingress_hostname:
        description:
            - NA
        required: False
        type: str
    datacenter:
        description:
            - (Required for new resource) The datacenter where this cluster will be deployed
        required: False
        type: str
    albs:
        description:
            - NA
        required: False
        type: list
        elements: dict
    public_service_endpoint:
        description:
            - NA
        required: False
        type: bool
    gateway_enabled:
        description:
            - Set true for gateway enabled clusters
        required: False
        type: bool
        default: False
    crn:
        description:
            - CRN of resource instance
        required: False
        type: str
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The cluster name
        required: False
        type: str
    private_vlan_id:
        description:
            - NA
        required: False
        type: str
    wait_time_minutes:
        description:
            - NA
        required: False
        type: int
        default: 90
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster
        required: False
        type: str
    kube_version:
        description:
            - NA
        required: False
        type: str
    subnet_id:
        description:
            - NA
        required: False
        type: list
        elements: str
    space_guid:
        description:
            - The bluemix space guid this cluster belongs to
        required: False
        type: str
    hardware:
        description:
            - (Required for new resource) NA
        required: False
        type: str
    workers_info:
        description:
            - The IDs of the worker node
        required: False
        type: list
        elements: dict
    account_guid:
        description:
            - The bluemix account guid this cluster belongs to
        required: False
        type: str
    private_service_endpoint:
        description:
            - NA
        required: False
        type: bool
    is_trusted:
        description:
            - NA
        required: False
        type: bool
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
    machine_type:
        description:
            - NA
        required: False
        type: str
    billing:
        description:
            - NA
        required: False
        type: str
    public_vlan_id:
        description:
            - NA
        required: False
        type: str
    server_url:
        description:
            - NA
        required: False
        type: str
    tags:
        description:
            - NA
        required: False
        type: list
        elements: str
    disk_encryption:
        description:
            - NA
        required: False
        type: bool
        default: True
    default_pool_size:
        description:
            - The size of the default worker pool
        required: False
        type: int
        default: 1
    update_all_workers:
        description:
            - NA
        required: False
        type: bool
        default: False
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    worker_pools:
        description:
            - NA
        required: False
        type: list
        elements: dict
    private_service_endpoint_url:
        description:
            - NA
        required: False
        type: str
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    region:
        description:
            - The cluster region
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
    'ingress_secret',
    'no_subnet',
    'webhook',
    'public_service_endpoint_url',
    'resource_crn',
    'ingress_hostname',
    'datacenter',
    'albs',
    'public_service_endpoint',
    'gateway_enabled',
    'crn',
    'resource_status',
    'name',
    'private_vlan_id',
    'wait_time_minutes',
    'resource_controller_url',
    'kube_version',
    'subnet_id',
    'space_guid',
    'hardware',
    'workers_info',
    'account_guid',
    'private_service_endpoint',
    'is_trusted',
    'org_guid',
    'worker_num',
    'machine_type',
    'billing',
    'public_vlan_id',
    'server_url',
    'tags',
    'disk_encryption',
    'default_pool_size',
    'update_all_workers',
    'resource_group_id',
    'worker_pools',
    'private_service_endpoint_url',
    'resource_name',
    'resource_group_name',
    'region',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    ingress_secret=dict(
        required=False,
        type='str'),
    no_subnet=dict(
        default=False,
        type='bool'),
    webhook=dict(
        required=False,
        elements='',
        type='list'),
    public_service_endpoint_url=dict(
        required=False,
        type='str'),
    resource_crn=dict(
        required=False,
        type='str'),
    ingress_hostname=dict(
        required=False,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    albs=dict(
        required=False,
        elements='',
        type='list'),
    public_service_endpoint=dict(
        required=False,
        type='bool'),
    gateway_enabled=dict(
        default=False,
        type='bool'),
    crn=dict(
        required=False,
        type='str'),
    resource_status=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    private_vlan_id=dict(
        required=False,
        type='str'),
    wait_time_minutes=dict(
        default=90,
        type='int'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    kube_version=dict(
        required=False,
        type='str'),
    subnet_id=dict(
        required=False,
        elements='',
        type='list'),
    space_guid=dict(
        required=False,
        type='str'),
    hardware=dict(
        required=False,
        type='str'),
    workers_info=dict(
        required=False,
        elements='',
        type='list'),
    account_guid=dict(
        required=False,
        type='str'),
    private_service_endpoint=dict(
        required=False,
        type='bool'),
    is_trusted=dict(
        required=False,
        type='bool'),
    org_guid=dict(
        required=False,
        type='str'),
    worker_num=dict(
        default=0,
        type='int'),
    machine_type=dict(
        required=False,
        type='str'),
    billing=dict(
        required=False,
        type='str'),
    public_vlan_id=dict(
        required=False,
        type='str'),
    server_url=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    disk_encryption=dict(
        default=True,
        type='bool'),
    default_pool_size=dict(
        default=1,
        type='int'),
    update_all_workers=dict(
        default=False,
        type='bool'),
    resource_group_id=dict(
        required=False,
        type='str'),
    worker_pools=dict(
        required=False,
        elements='',
        type='list'),
    private_service_endpoint_url=dict(
        required=False,
        type='str'),
    resource_name=dict(
        required=False,
        type='str'),
    resource_group_name=dict(
        required=False,
        type='str'),
    region=dict(
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
        resource_type='ibm_container_cluster',
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
