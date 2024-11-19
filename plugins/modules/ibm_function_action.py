#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_function_action
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/function_action

short_description: Configure IBM Cloud 'ibm_function_action' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_function_action' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    namespace:
        description:
            - (Required for new resource) IBM Cloud function namespace.
        required: True
        type: str
    limits:
        description:
            - None
        required: False
        type: list
        elements: dict
    publish:
        description:
            - Action visibilty.
        required: False
        type: bool
    user_defined_parameters:
        description:
            - Parameters values in KEY VALUE format. Parameter bindings included in the context passed to the action.
        required: False
        type: str
        default: []
    name:
        description:
            - (Required for new resource) Name of action.
        required: True
        type: str
    exec:
        description:
            - (Required for new resource) Execution info
        required: True
        type: list
        elements: dict
    user_defined_annotations:
        description:
            - Annotation values in KEY VALUE format.
        required: False
        type: str
        default: []
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
    function_namespace:
        description:
            - The namespace in IBM Cloud™ Functions where you want to
              create your resources. This can also be provided via the
              environment variable 'FUNCTION_NAMESPACE'.
        required: True
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
    ('namespace', 'str'),
    ('name', 'str'),
    ('exec', 'list'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'namespace',
    'limits',
    'publish',
    'user_defined_parameters',
    'name',
    'exec',
    'user_defined_annotations',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('namespace', 'str'),
    ('name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'namespace',
    'name',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    namespace=dict(
        required=False,
        type='str'),
    limits=dict(
        required=False,
        elements='',
        type='list'),
    publish=dict(
        required=False,
        type='bool'),
    user_defined_parameters=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    exec=dict(
        required=False,
        elements='',
        type='list'),
    user_defined_annotations=dict(
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
    function_namespace=dict(
        type='str',
        fallback=(env_fallback, ['FUNCTION_NAMESPACE']),
        required=True),
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
        resource_type='ibm_function_action',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_function_action',
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
