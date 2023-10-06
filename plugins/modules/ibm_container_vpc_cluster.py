#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_vpc_cluster
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_vpc_cluster

short_description: Configure IBM Cloud 'ibm_container_vpc_cluster' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_vpc_cluster' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.50.0
    - Terraform v0.12.20

options:
    taints:
        description:
            - WorkerPool Taints
        required: False
        type: list
        elements: dict
    disable_public_service_endpoint:
        description:
            - Boolean value true if Public service endpoint to be disabled
        required: False
        type: bool
        default: False
    wait_till:
        description:
            - wait_till can be configured for Master Ready, One worker Ready or Ingress Ready or Normal
        required: False
        type: str
        default: IngressReady
    host_pool_id:
        description:
            - The ID of the cluster's associated host pool
        required: False
        type: str
    patch_version:
        description:
            - Kubernetes patch version
        required: False
        type: str
    pod_subnet:
        description:
            - Custom subnet CIDR to provide private IP addresses for pods
        required: False
        type: str
    cos_instance_crn:
        description:
            - A standard cloud object storage instance CRN to back up the internal registry in your OpenShift on VPC Gen 2 cluster
        required: False
        type: str
    worker_count:
        description:
            - Number of worker nodes in the cluster
        required: False
        type: int
        default: 1
    secondary_storage:
        description:
            - The secondary storage option for the default worker pool.
        required: False
        type: str
    operating_system:
        description:
            - The operating system of the workers in the default worker pool.
        required: False
        type: str
    crk:
        description:
            - Root Key ID for boot volume encryption
        required: False
        type: str
    image_security_enforcement:
        description:
            - Set true to enable image security enforcement policies
        required: False
        type: bool
        default: False
    name:
        description:
            - (Required for new resource) The cluster name
        required: True
        type: str
    zones:
        description:
            - (Required for new resource) Zone info
        required: True
        type: list
        elements: dict
    entitlement:
        description:
            - Entitlement option reduces additional OCP Licence cost in Openshift Clusters
        required: False
        type: str
    force_delete_storage:
        description:
            - Force the removal of a cluster and its persistent storage. Deleted data cannot be recovered
        required: False
        type: bool
        default: False
    kms_config:
        description:
            - Enables KMS on a given cluster
        required: False
        type: list
        elements: dict
    wait_for_worker_update:
        description:
            - Wait for worker node to update during kube version update.
        required: False
        type: bool
        default: True
    worker_labels:
        description:
            - Labels for default worker pool
        required: False
        type: dict
        elements: str
    retry_patch_version:
        description:
            - Argument which helps to retry the patch version updates on worker nodes. Increment the value to retry the patch updates if the previous apply fails
        required: False
        type: int
    service_subnet:
        description:
            - Custom subnet CIDR to provide private IP addresses for services
        required: False
        type: str
    kms_instance_id:
        description:
            - Instance ID for boot volume encryption
        required: False
        type: str
    kube_version:
        description:
            - Kubernetes version
        required: False
        type: str
    update_all_workers:
        description:
            - Updates all the woker nodes if sets to true
        required: False
        type: bool
        default: False
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    flavor:
        description:
            - (Required for new resource) Cluster nodes flavour
        required: True
        type: str
    kms_account_id:
        description:
            - Account ID of kms instance holder - if not provided, defaults to the account in use
        required: False
        type: str
    vpc_id:
        description:
            - (Required for new resource) The vpc id where the cluster is
        required: True
        type: str
    tags:
        description:
            - List of tags for the resources
        required: False
        type: list
        elements: str
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
    ('name', 'str'),
    ('zones', 'list'),
    ('flavor', 'str'),
    ('vpc_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'taints',
    'disable_public_service_endpoint',
    'wait_till',
    'host_pool_id',
    'patch_version',
    'pod_subnet',
    'cos_instance_crn',
    'worker_count',
    'secondary_storage',
    'operating_system',
    'crk',
    'image_security_enforcement',
    'name',
    'zones',
    'entitlement',
    'force_delete_storage',
    'kms_config',
    'wait_for_worker_update',
    'worker_labels',
    'retry_patch_version',
    'service_subnet',
    'kms_instance_id',
    'kube_version',
    'update_all_workers',
    'resource_group_id',
    'flavor',
    'kms_account_id',
    'vpc_id',
    'tags',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
    'cluster_name_id',
    'alb_type',
    'name',
    'resource_group_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    taints=dict(
        required=False,
        elements='',
        type='list'),
    disable_public_service_endpoint=dict(
        required=False,
        type='bool'),
    wait_till=dict(
        required=False,
        type='str'),
    host_pool_id=dict(
        required=False,
        type='str'),
    patch_version=dict(
        required=False,
        type='str'),
    pod_subnet=dict(
        required=False,
        type='str'),
    cos_instance_crn=dict(
        required=False,
        type='str'),
    worker_count=dict(
        required=False,
        type='int'),
    secondary_storage=dict(
        required=False,
        type='str'),
    operating_system=dict(
        required=False,
        type='str'),
    crk=dict(
        required=False,
        type='str'),
    image_security_enforcement=dict(
        required=False,
        type='bool'),
    name=dict(
        required=False,
        type='str'),
    zones=dict(
        required=False,
        elements='',
        type='list'),
    entitlement=dict(
        required=False,
        type='str'),
    force_delete_storage=dict(
        required=False,
        type='bool'),
    kms_config=dict(
        required=False,
        elements='',
        type='list'),
    wait_for_worker_update=dict(
        required=False,
        type='bool'),
    worker_labels=dict(
        required=False,
        elements='',
        type='dict'),
    retry_patch_version=dict(
        required=False,
        type='int'),
    service_subnet=dict(
        required=False,
        type='str'),
    kms_instance_id=dict(
        required=False,
        type='str'),
    kube_version=dict(
        required=False,
        type='str'),
    update_all_workers=dict(
        required=False,
        type='bool'),
    resource_group_id=dict(
        required=False,
        type='str'),
    flavor=dict(
        required=False,
        type='str'),
    kms_account_id=dict(
        required=False,
        type='str'),
    vpc_id=dict(
        required=False,
        type='str'),
    tags=dict(
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
        resource_type='ibm_container_vpc_cluster',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.50.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_container_vpc_cluster',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.50.0',
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
