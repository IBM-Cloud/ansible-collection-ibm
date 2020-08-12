#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_vpc_worker_pool
short_description: Configure IBM Cloud 'ibm_container_vpc_worker_pool' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_vpc_worker_pool' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.10.0
    - Terraform v0.12.20

options:
    zones:
        description:
            - (Required for new resource) Zones info
        required: True
        type: list
        elements: dict
    vpc_id:
        description:
            - (Required for new resource) The vpc id where the cluster is
        required: True
        type: str
    worker_count:
        description:
            - (Required for new resource) The number of workers
        required: True
        type: int
    entitlement:
        description:
            - Entitlement option reduces additional OCP Licence cost in Openshift Clusters
        required: False
        type: str
    cluster:
        description:
            - (Required for new resource) Cluster name
        required: True
        type: str
    flavor:
        description:
            - (Required for new resource) cluster node falvor
        required: True
        type: str
    worker_pool_name:
        description:
            - (Required for new resource) worker pool name
        required: True
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
    ('zones', 'list'),
    ('vpc_id', 'str'),
    ('worker_count', 'int'),
    ('cluster', 'str'),
    ('flavor', 'str'),
    ('worker_pool_name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'zones',
    'vpc_id',
    'worker_count',
    'entitlement',
    'cluster',
    'flavor',
    'worker_pool_name',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    zones=dict(
        required=False,
        elements='',
        type='list'),
    vpc_id=dict(
        required=False,
        type='str'),
    worker_count=dict(
        required=False,
        type='int'),
    entitlement=dict(
        required=False,
        type='str'),
    cluster=dict(
        required=False,
        type='str'),
    flavor=dict(
        required=False,
        type='str'),
    worker_pool_name=dict(
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

    result = ibmcloud_terraform(
        resource_type='ibm_container_vpc_worker_pool',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.10.0',
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
