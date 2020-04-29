#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_function_package
short_description: Configure IBM Cloud 'ibm_function_package' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_function_package' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.5.0
    - Terraform v0.12.20

options:
    name:
        description:
            - (Required for new resource) Name of package.
        required: False
        type: str
    publish:
        description:
            - Package visibilty.
        required: False
        type: bool
        default: False
    version:
        description:
            - Semantic version of the item.
        required: False
        type: str
    user_defined_annotations:
        description:
            - Annotation values in KEY VALUE format.
        required: False
        type: str
        default: []
    user_defined_parameters:
        description:
            - Parameters values in KEY VALUE format. Parameter bindings included in the context passed to the package.
        required: False
        type: str
        default: []
    annotations:
        description:
            - All annotations set on package by user and those set by the IBM Cloud Function backend/API.
        required: False
        type: str
    parameters:
        description:
            - All parameters set on package by user and those set by the IBM Cloud Function backend/API.
        required: False
        type: str
    bind_package_name:
        description:
            - Name of package to be binded.
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
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'name',
    'publish',
    'version',
    'user_defined_annotations',
    'user_defined_parameters',
    'annotations',
    'parameters',
    'bind_package_name',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    name=dict(
        required=False,
        type='str'),
    publish=dict(
        default=False,
        type='bool'),
    version=dict(
        required=False,
        type='str'),
    user_defined_annotations=dict(
        default='[]',
        type='str'),
    user_defined_parameters=dict(
        default='[]',
        type='str'),
    annotations=dict(
        required=False,
        type='str'),
    parameters=dict(
        required=False,
        type='str'),
    bind_package_name=dict(
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
        resource_type='ibm_function_package',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.5.0',
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
