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
    datacenter:
        description:
            - (Required for new resource) The datacenter where this cluster will be deployed
        required: True
        type: str
    billing:
        description:
            - None
        required: False
        type: str
    is_trusted:
        description:
            - None
        required: False
        type: bool
    account_guid:
        description:
            - The bluemix account guid this cluster belongs to
        required: False
        type: str
    region:
        description:
            - The cluster region
        required: False
        type: str
    ingress_hostname:
        description:
            - None
        required: False
        type: str
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    albs:
        description:
            - None
        required: False
        type: list
        elements: dict
    update_all_workers:
        description:
            - Updates all the woker nodes if sets to true
        required: False
        type: bool
        default: False
    ingress_secret:
        description:
            - None
        required: False
        type: str
    subnet_id:
        description:
            - List of subnet IDs
        required: False
        type: list
        elements: str
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    entitlement:
        description:
            - Entitlement option reduces additional OCP Licence cost in Openshift Clusters
        required: False
        type: str
    private_service_endpoint_url:
        description:
            - None
        required: False
        type: str
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
    name:
        description:
            - (Required for new resource) The cluster name
        required: True
        type: str
    default_pool_size:
        description:
            - The size of the default worker pool
        required: False
        type: int
        default: 1
    disk_encryption:
        description:
            - disc encryption done, if set to true.
        required: False
        type: bool
        default: True
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    hardware:
        description:
            - (Required for new resource) Hardware type
        required: True
        type: str
    public_vlan_id:
        description:
            - Public VLAN ID
        required: False
        type: str
    private_service_endpoint:
        description:
            - None
        required: False
        type: bool
    webhook:
        description:
            - None
        required: False
        type: list
        elements: dict
    org_guid:
        description:
            - The bluemix organization guid this cluster belongs to
        required: False
        type: str
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster
        required: False
        type: str
    kube_version:
        description:
            - Kubernetes version info
        required: False
        type: str
    private_vlan_id:
        description:
            - Private VLAN ID
        required: False
        type: str
    no_subnet:
        description:
            - Boolean value set to true when subnet creation is not required.
        required: False
        type: bool
        default: False
    server_url:
        description:
            - None
        required: False
        type: str
    worker_pools:
        description:
            - None
        required: False
        type: list
        elements: dict
    public_service_endpoint:
        description:
            - None
        required: False
        type: bool
    workers_info:
        description:
            - The IDs of the worker node
        required: False
        type: list
        elements: dict
    machine_type:
        description:
            - Machine type
        required: False
        type: str
    space_guid:
        description:
            - The bluemix space guid this cluster belongs to
        required: False
        type: str
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    worker_num:
        description:
            - Number of worker nodes
        required: False
        type: int
        default: 0
    wait_time_minutes:
        description:
            - None
        required: False
        type: int
    tags:
        description:
            - Tags for the resource
        required: False
        type: list
        elements: str
    public_service_endpoint_url:
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
    'datacenter',
    'billing',
    'is_trusted',
    'account_guid',
    'region',
    'ingress_hostname',
    'resource_crn',
    'albs',
    'update_all_workers',
    'ingress_secret',
    'subnet_id',
    'resource_group_id',
    'entitlement',
    'private_service_endpoint_url',
    'gateway_enabled',
    'crn',
    'name',
    'default_pool_size',
    'disk_encryption',
    'resource_name',
    'hardware',
    'public_vlan_id',
    'private_service_endpoint',
    'webhook',
    'org_guid',
    'resource_controller_url',
    'kube_version',
    'private_vlan_id',
    'no_subnet',
    'server_url',
    'worker_pools',
    'public_service_endpoint',
    'workers_info',
    'machine_type',
    'space_guid',
    'resource_status',
    'resource_group_name',
    'worker_num',
    'wait_time_minutes',
    'tags',
    'public_service_endpoint_url',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    datacenter=dict(
        required= False,
        type='str'),
    billing=dict(
        required= False,
        type='str'),
    is_trusted=dict(
        required= False,
        type='bool'),
    account_guid=dict(
        required= False,
        type='str'),
    region=dict(
        required= False,
        type='str'),
    ingress_hostname=dict(
        required= False,
        type='str'),
    resource_crn=dict(
        required= False,
        type='str'),
    albs=dict(
        required= False,
        elements='',
        type='list'),
    update_all_workers=dict(
        default=False,
        type='bool'),
    ingress_secret=dict(
        required= False,
        type='str'),
    subnet_id=dict(
        required= False,
        elements='',
        type='list'),
    resource_group_id=dict(
        required= False,
        type='str'),
    entitlement=dict(
        required= False,
        type='str'),
    private_service_endpoint_url=dict(
        required= False,
        type='str'),
    gateway_enabled=dict(
        default=False,
        type='bool'),
    crn=dict(
        required= False,
        type='str'),
    name=dict(
        required= False,
        type='str'),
    default_pool_size=dict(
        default=1,
        type='int'),
    disk_encryption=dict(
        default=True,
        type='bool'),
    resource_name=dict(
        required= False,
        type='str'),
    hardware=dict(
        required= False,
        type='str'),
    public_vlan_id=dict(
        required= False,
        type='str'),
    private_service_endpoint=dict(
        required= False,
        type='bool'),
    webhook=dict(
        required= False,
        elements='',
        type='list'),
    org_guid=dict(
        required= False,
        type='str'),
    resource_controller_url=dict(
        required= False,
        type='str'),
    kube_version=dict(
        required= False,
        type='str'),
    private_vlan_id=dict(
        required= False,
        type='str'),
    no_subnet=dict(
        default=False,
        type='bool'),
    server_url=dict(
        required= False,
        type='str'),
    worker_pools=dict(
        required= False,
        elements='',
        type='list'),
    public_service_endpoint=dict(
        required= False,
        type='bool'),
    workers_info=dict(
        required= False,
        elements='',
        type='list'),
    machine_type=dict(
        required= False,
        type='str'),
    space_guid=dict(
        required= False,
        type='str'),
    resource_status=dict(
        required= False,
        type='str'),
    resource_group_name=dict(
        required= False,
        type='str'),
    worker_num=dict(
        default=0,
        type='int'),
    wait_time_minutes=dict(
        required= False,
        type='int'),
    tags=dict(
        required= False,
        elements='',
        type='list'),
    public_service_endpoint_url=dict(
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
