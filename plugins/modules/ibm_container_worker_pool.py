#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_worker_pool
short_description: Configure IBM Cloud 'ibm_container_worker_pool' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_worker_pool' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.5.2
    - Terraform v0.12.20

options:
    region:
        description:
            - The worker pool region
        required: False
        type: str
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    machine_type:
        description:
            - (Required for new resource) worker nodes machine type
        required: False
        type: str
    worker_pool_name:
        description:
            - (Required for new resource) worker pool name
        required: False
        type: str
    entitlement:
        description:
            - Entitlement option reduces additional OCP Licence cost in Openshift Clusters
        required: False
        type: str
    hardware:
        description:
            - Hardware type
        required: False
        type: str
        default: shared
    state_:
        description:
            - worker pool state
        required: False
        type: str
    labels:
        description:
            - list of labels to worker pool
        required: False
        type: dict
        elements: 
    cluster:
        description:
            - (Required for new resource) Cluster name
        required: False
        type: str
    size_per_zone:
        description:
            - (Required for new resource) Number of nodes per zone
        required: False
        type: int
    disk_encryption:
        description:
            - worker node disk encrypted if set to true
        required: False
        type: bool
        default: True
    zones:
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
    'region',
    'resource_group_id',
    'machine_type',
    'worker_pool_name',
    'entitlement',
    'hardware',
    'state_',
    'labels',
    'cluster',
    'size_per_zone',
    'disk_encryption',
    'zones',
    'resource_controller_url',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    region=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
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
    hardware=dict(
        default='shared',
        type='str'),
    state_=dict(
        required=False,
        type='str'),
    labels=dict(
        required=False,
        elements='',
        type='dict'),
    cluster=dict(
        required=False,
        type='str'),
    size_per_zone=dict(
        required=False,
        type='int'),
    disk_encryption=dict(
        default=True,
        type='bool'),
    zones=dict(
        required=False,
        elements='',
        type='list'),
    resource_controller_url=dict(
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
        resource_type='ibm_container_worker_pool',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.5.2',
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
