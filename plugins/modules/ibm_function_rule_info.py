#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_function_rule_info
short_description: Retrieve IBM Cloud 'ibm_function_rule' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_function_rule' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.6.0
    - Terraform v0.12.20

options:
    version:
        description:
            - Semantic version of the rule
        required: False
        type: str
    name:
        description:
            - Name of the rule.
        required: True
        type: str
    trigger_name:
        description:
            - Name of the trigger.
        required: False
        type: str
    action_name:
        description:
            - Name of an action.
        required: False
        type: str
    status:
        description:
            - Status of the rule.
        required: False
        type: str
    publish:
        description:
            - Rule Visibility.
        required: False
        type: bool
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
    'version',
    'name',
    'trigger_name',
    'action_name',
    'status',
    'publish',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    version=dict(
        required=False,
        type='str'),
    name=dict(
        required=True,
        type='str'),
    trigger_name=dict(
        required=False,
        type='str'),
    action_name=dict(
        required=False,
        type='str'),
    status=dict(
        required=False,
        type='str'),
    publish=dict(
        required=False,
        type='bool'),
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

    result = ibmcloud_terraform(
        resource_type='ibm_function_rule',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.6.0',
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
