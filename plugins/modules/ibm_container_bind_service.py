#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_bind_service
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_bind_service

short_description: Configure IBM Cloud 'ibm_container_bind_service' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_bind_service' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    tags:
        description:
            - List of tags for the resource
        required: False
        type: list
        elements: str
    cluster_name_id:
        description:
            - (Required for new resource) Cluster name or ID
        required: True
        type: str
    service_instance_name:
        description:
            - serivice instance name
        required: False
        type: str
    service_instance_id:
        description:
            - Service instance ID
        required: False
        type: str
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    namespace_id:
        description:
            - (Required for new resource) namespace ID
        required: True
        type: str
    key:
        description:
            - Key info
        required: False
        type: str
    role:
        description:
            - Role info
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
    ('cluster_name_id', 'str'),
    ('namespace_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'tags',
    'cluster_name_id',
    'service_instance_name',
    'service_instance_id',
    'resource_group_id',
    'namespace_id',
    'key',
    'role',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('namespace_id', 'str'),
    ('cluster_name_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'service_instance_id',
    'service_instance_name',
    'namespace_id',
    'cluster_name_id',
]

TL_CONFLICTS_MAP = {
    'service_instance_name': ['service_instance_id'],
    'service_instance_id': ['service_instance_name'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    tags=dict(
        required=False,
        elements='',
        type='list'),
    cluster_name_id=dict(
        required=False,
        type='str'),
    service_instance_name=dict(
        required=False,
        type='str'),
    service_instance_id=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    namespace_id=dict(
        required=False,
        type='str'),
    key=dict(
        required=False,
        type='str'),
    role=dict(
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
        resource_type='ibm_container_bind_service',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_container_bind_service',
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
