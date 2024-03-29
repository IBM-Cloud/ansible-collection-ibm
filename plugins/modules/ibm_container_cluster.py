#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_cluster
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_cluster

short_description: Configure IBM Cloud 'ibm_container_cluster' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_cluster' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.51.0
    - Terraform v0.12.20

options:
    tags:
        description:
            - Tags for the resource
        required: False
        type: list
        elements: str
    image_security_enforcement:
        description:
            - Set true to enable image security enforcement policies
        required: False
        type: bool
        default: False
    workers_info:
        description:
            - The IDs of the worker node
        required: False
        type: list
        elements: dict
    retry_patch_version:
        description:
            - Argument which helps to retry the patch version updates on worker nodes. Increment the value to retry the patch updates if the previous apply fails
        required: False
        type: int
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    taints:
        description:
            - WorkerPool Taints
        required: False
        type: list
        elements: dict
    pod_subnet:
        description:
            - Custom subnet CIDR to provide private IP addresses for pods
        required: False
        type: str
    service_subnet:
        description:
            - Custom subnet CIDR to provide private IP addresses for services
        required: False
        type: str
    hardware:
        description:
            - (Required for new resource) Hardware type
        required: True
        type: str
    private_service_endpoint:
        description:
            - None
        required: False
        type: bool
    force_delete_storage:
        description:
            - Force the removal of a cluster and its persistent storage. Deleted data cannot be recovered
        required: False
        type: bool
        default: False
    wait_till:
        description:
            - wait_till can be configured for Master Ready, One worker Ready, Ingress Ready or Normal
        required: False
        type: str
        default: IngressReady
    private_vlan_id:
        description:
            - Private VLAN ID
        required: False
        type: str
    entitlement:
        description:
            - Entitlement option reduces additional OCP Licence cost in Openshift Clusters
        required: False
        type: str
    subnet_id:
        description:
            - List of subnet IDs
        required: False
        type: list
        elements: str
    name:
        description:
            - (Required for new resource) The cluster name
        required: True
        type: str
    datacenter:
        description:
            - (Required for new resource) The datacenter where this cluster will be deployed
        required: True
        type: str
    patch_version:
        description:
            - Kubernetes patch version
        required: False
        type: str
    wait_for_worker_update:
        description:
            - Wait for worker node to update during kube version update.
        required: False
        type: bool
        default: True
    update_all_workers:
        description:
            - Updates all the woker nodes if sets to true
        required: False
        type: bool
        default: False
    gateway_enabled:
        description:
            - Set true for gateway enabled clusters
        required: False
        type: bool
        default: False
    kms_config:
        description:
            - Enables KMS on a given cluster
        required: False
        type: list
        elements: dict
    kube_version:
        description:
            - Kubernetes version info
        required: False
        type: str
    operating_system:
        description:
            - The operating system of the workers in the default worker pool.
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
    labels:
        description:
            - list of labels to the default worker pool
        required: False
        type: dict
        elements: str
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
    public_service_endpoint:
        description:
            - None
        required: False
        type: bool
    disk_encryption:
        description:
            - disc encryption done, if set to true.
        required: False
        type: bool
        default: True
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
    ('hardware', 'str'),
    ('name', 'str'),
    ('datacenter', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'tags',
    'image_security_enforcement',
    'workers_info',
    'retry_patch_version',
    'resource_group_id',
    'taints',
    'pod_subnet',
    'service_subnet',
    'hardware',
    'private_service_endpoint',
    'force_delete_storage',
    'wait_till',
    'private_vlan_id',
    'entitlement',
    'subnet_id',
    'name',
    'datacenter',
    'patch_version',
    'wait_for_worker_update',
    'update_all_workers',
    'gateway_enabled',
    'kms_config',
    'kube_version',
    'operating_system',
    'default_pool_size',
    'no_subnet',
    'labels',
    'public_vlan_id',
    'webhook',
    'public_service_endpoint',
    'disk_encryption',
    'machine_type',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
    'cluster_name_id',
    'account_guid',
    'region',
    'resource_group_id',
    'name',
    'alb_type',
    'list_bounded_services',
    'space_guid',
    'org_guid',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    tags=dict(
        required=False,
        elements='',
        type='list'),
    image_security_enforcement=dict(
        required=False,
        type='bool'),
    workers_info=dict(
        required=False,
        elements='',
        type='list'),
    retry_patch_version=dict(
        required=False,
        type='int'),
    resource_group_id=dict(
        required=False,
        type='str'),
    taints=dict(
        required=False,
        elements='',
        type='list'),
    pod_subnet=dict(
        required=False,
        type='str'),
    service_subnet=dict(
        required=False,
        type='str'),
    hardware=dict(
        required=False,
        type='str'),
    private_service_endpoint=dict(
        required=False,
        type='bool'),
    force_delete_storage=dict(
        required=False,
        type='bool'),
    wait_till=dict(
        required=False,
        type='str'),
    private_vlan_id=dict(
        required=False,
        type='str'),
    entitlement=dict(
        required=False,
        type='str'),
    subnet_id=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=False,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    patch_version=dict(
        required=False,
        type='str'),
    wait_for_worker_update=dict(
        required=False,
        type='bool'),
    update_all_workers=dict(
        required=False,
        type='bool'),
    gateway_enabled=dict(
        required=False,
        type='bool'),
    kms_config=dict(
        required=False,
        elements='',
        type='list'),
    kube_version=dict(
        required=False,
        type='str'),
    operating_system=dict(
        required=False,
        type='str'),
    default_pool_size=dict(
        required=False,
        type='int'),
    no_subnet=dict(
        required=False,
        type='bool'),
    labels=dict(
        required=False,
        elements='',
        type='dict'),
    public_vlan_id=dict(
        required=False,
        type='str'),
    webhook=dict(
        required=False,
        elements='',
        type='list'),
    public_service_endpoint=dict(
        required=False,
        type='bool'),
    disk_encryption=dict(
        required=False,
        type='bool'),
    machine_type=dict(
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
        resource_type='ibm_container_cluster',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.51.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_container_cluster',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.51.0',
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
