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
    albs:
        description:
            - None
        required: False
        type: list
        elements: dict
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    disk_encryption:
        description:
            - disc encryption done, if set to true.
        required: False
        type: bool
        default: True
    public_vlan_id:
        description:
            - Public VLAN ID
        required: False
        type: str
    webhook:
        description:
            - None
        required: False
        type: list
        elements: dict
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster
        required: False
        type: str
    datacenter:
        description:
            - (Required for new resource) The datacenter where this cluster will be deployed
        required: True
        type: str
    gateway_enabled:
        description:
            - Set true for gateway enabled clusters
        required: False
        type: bool
        default: False
    worker_pools:
        description:
            - None
        required: False
        type: list
        elements: dict
    no_subnet:
        description:
            - Boolean value set to true when subnet creation is not required.
        required: False
        type: bool
        default: False
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    ingress_hostname:
        description:
            - None
        required: False
        type: str
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
    private_service_endpoint_url:
        description:
            - None
        required: False
        type: str
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
    public_service_endpoint:
        description:
            - None
        required: False
        type: bool
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The cluster name
        required: True
        type: str
    workers_info:
        description:
            - The IDs of the worker node
        required: False
        type: list
        elements: dict
    entitlement:
        description:
            - Entitlement option reduces additional OCP Licence cost in Openshift Clusters
        required: False
        type: str
    private_service_endpoint:
        description:
            - None
        required: False
        type: bool
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    default_pool_size:
        description:
            - The size of the default worker pool
        required: False
        type: int
        default: 1
    update_all_workers:
        description:
            - Updates all the woker nodes if sets to true
        required: False
        type: bool
        default: False
    hardware:
        description:
            - (Required for new resource) Hardware type
        required: True
        type: str
    private_vlan_id:
        description:
            - Private VLAN ID
        required: False
        type: str
    server_url:
        description:
            - None
        required: False
        type: str
    crn:
        description:
            - CRN of resource instance
        required: False
        type: str
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    kube_version:
        description:
            - Kubernetes version info
        required: False
        type: str
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
    'albs',
    'resource_group_name',
    'disk_encryption',
    'public_vlan_id',
    'webhook',
    'resource_controller_url',
    'datacenter',
    'gateway_enabled',
    'worker_pools',
    'no_subnet',
    'resource_group_id',
    'ingress_hostname',
    'tags',
    'public_service_endpoint_url',
    'private_service_endpoint_url',
    'ingress_secret',
    'subnet_id',
    'public_service_endpoint',
    'resource_status',
    'name',
    'workers_info',
    'entitlement',
    'private_service_endpoint',
    'resource_name',
    'default_pool_size',
    'update_all_workers',
    'hardware',
    'private_vlan_id',
    'server_url',
    'crn',
    'resource_crn',
    'kube_version',
    'machine_type',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    albs=dict(
        required= False,
        elements='',
        type='list'),
    resource_group_name=dict(
        required= False,
        type='str'),
    disk_encryption=dict(
        default=True,
        type='bool'),
    public_vlan_id=dict(
        required= False,
        type='str'),
    webhook=dict(
        required= False,
        elements='',
        type='list'),
    resource_controller_url=dict(
        required= False,
        type='str'),
    datacenter=dict(
        required= False,
        type='str'),
    gateway_enabled=dict(
        default=False,
        type='bool'),
    worker_pools=dict(
        required= False,
        elements='',
        type='list'),
    no_subnet=dict(
        default=False,
        type='bool'),
    resource_group_id=dict(
        required= False,
        type='str'),
    ingress_hostname=dict(
        required= False,
        type='str'),
    tags=dict(
        required= False,
        elements='',
        type='list'),
    public_service_endpoint_url=dict(
        required= False,
        type='str'),
    private_service_endpoint_url=dict(
        required= False,
        type='str'),
    ingress_secret=dict(
        required= False,
        type='str'),
    subnet_id=dict(
        required= False,
        elements='',
        type='list'),
    public_service_endpoint=dict(
        required= False,
        type='bool'),
    resource_status=dict(
        required= False,
        type='str'),
    name=dict(
        required= False,
        type='str'),
    workers_info=dict(
        required= False,
        elements='',
        type='list'),
    entitlement=dict(
        required= False,
        type='str'),
    private_service_endpoint=dict(
        required= False,
        type='bool'),
    resource_name=dict(
        required= False,
        type='str'),
    default_pool_size=dict(
        default=1,
        type='int'),
    update_all_workers=dict(
        default=False,
        type='bool'),
    hardware=dict(
        required= False,
        type='str'),
    private_vlan_id=dict(
        required= False,
        type='str'),
    server_url=dict(
        required= False,
        type='str'),
    crn=dict(
        required= False,
        type='str'),
    resource_crn=dict(
        required= False,
        type='str'),
    kube_version=dict(
        required= False,
        type='str'),
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
