#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_function_package_info
short_description: Retrieve IBM Cloud 'ibm_function_package' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_function_package' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.5
    - Terraform v0.12.20

options:
    name:
        description:
            - Name of the package.
        required: True
        type: str
    publish:
        description:
            - Package Visibility.
        required: False
        type: bool
    version:
        description:
            - Semantic version of the package.
        required: False
        type: str
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
            - Name of binded package.
        required: False
        type: str
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be
              provided via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
        required: False

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
    'annotations',
    'parameters',
    'bind_package_name',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    name=dict(
        required=True,
        type='str'),
    publish=dict(
        required=False,
        type='bool'),
    version=dict(
        required=False,
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
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_function_package',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.2.5',
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
