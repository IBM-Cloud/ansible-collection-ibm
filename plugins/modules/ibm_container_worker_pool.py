#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_worker_pool
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_worker_pool

short_description: Configure IBM Cloud 'ibm_container_worker_pool' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_worker_pool' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    orphan_on_delete:
        description:
            - Orphan the workerpool resource instead of deleting it
        required: False
        type: bool
    operating_system:
        description:
            - The operating system of the workers in the worker pool.
        required: False
        type: str
    disk_encryption:
        description:
            - worker node disk encrypted if set to true
        required: False
        type: bool
        default: True
    import_on_create:
        description:
            - Import an existing workerpool from the cluster instead of creating a new
        required: False
        type: bool
    hardware:
        description:
            - Hardware type
        required: False
        type: str
        default: shared
    machine_type:
        description:
            - (Required for new resource) worker nodes machine type
        required: True
        type: str
    worker_pool_name:
        description:
            - (Required for new resource) worker pool name
        required: True
        type: str
    entitlement:
        description:
            - Entitlement option reduces additional OCP Licence cost in Openshift Clusters
        required: False
        type: str
    labels:
        description:
            - list of labels to worker pool
        required: False
        type: dict
        elements: str
    taints:
        description:
            - WorkerPool Taints
        required: False
        type: list
        elements: dict
    cluster:
        description:
            - (Required for new resource) Cluster name
        required: True
        type: str
    size_per_zone:
        description:
            - (Required for new resource) Number of nodes per zone
        required: True
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
    ('machine_type', 'str'),
    ('worker_pool_name', 'str'),
    ('cluster', 'str'),
    ('size_per_zone', 'int'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'resource_group_id',
    'orphan_on_delete',
    'operating_system',
    'disk_encryption',
    'import_on_create',
    'hardware',
    'machine_type',
    'worker_pool_name',
    'entitlement',
    'labels',
    'taints',
    'cluster',
    'size_per_zone',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('cluster', 'str'),
    ('worker_pool_name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'cluster',
    'worker_pool_name',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    resource_group_id=dict(
        required=False,
        type='str'),
    orphan_on_delete=dict(
        required=False,
        type='bool'),
    operating_system=dict(
        required=False,
        type='str'),
    disk_encryption=dict(
        required=False,
        type='bool'),
    import_on_create=dict(
        required=False,
        type='bool'),
    hardware=dict(
        required=False,
        type='str'),
    machine_type=dict(
        required=False,
        type='str'),
    worker_pool_name=dict(
        required=False,
        type='str'),
    entitlement=dict(
        required=False,
        type='str'),
    labels=dict(
        required=False,
        elements='',
        type='dict'),
    taints=dict(
        required=False,
        elements='',
        type='list'),
    cluster=dict(
        required=False,
        type='str'),
    size_per_zone=dict(
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
        resource_type='ibm_container_worker_pool',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_container_worker_pool',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.71.2',
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
