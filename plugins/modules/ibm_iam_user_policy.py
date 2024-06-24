#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_iam_user_policy
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/iam_user_policy

short_description: Configure IBM Cloud 'ibm_iam_user_policy' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_iam_user_policy' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.66.0
    - Terraform v1.5.5

options:
    resources:
        description:
            - None
        required: False
        type: list
        elements: dict
    description:
        description:
            - Description of the Policy
        required: False
        type: str
    transaction_id:
        description:
            - Set transactionID for debug
        required: False
        type: str
    rule_conditions:
        description:
            - Rule conditions enforced by the policy
        required: False
        type: list
        elements: dict
    rule_operator:
        description:
            - Operator that multiple rule conditions are evaluated over
        required: False
        type: str
    ibm_id:
        description:
            - (Required for new resource) The ibm id or email of user
        required: True
        type: str
    roles:
        description:
            - (Required for new resource) Role names of the policy definition
        required: True
        type: list
        elements: str
    resource_attributes:
        description:
            - Set resource attributes.
        required: False
        type: list
        elements: dict
    account_management:
        description:
            - Give access to all account management services
        required: False
        type: bool
        default: False
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    resource_tags:
        description:
            - Set access management tags.
        required: False
        type: list
        elements: dict
    pattern:
        description:
            - Pattern rule follows for time-based condition
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
    iaas_classic_username:
        description:
            - The IBM Cloud Classic Infrastructure (SoftLayer) user name. This
              can also be provided via the environment variable
              'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - The IBM Cloud Classic Infrastructure API key. This can also be
              provided via the environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
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
    ('ibm_id', 'str'),
    ('roles', 'list'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'resources',
    'description',
    'transaction_id',
    'rule_conditions',
    'rule_operator',
    'ibm_id',
    'roles',
    'resource_attributes',
    'account_management',
    'tags',
    'resource_tags',
    'pattern',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('ibm_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'transaction_id',
    'ibm_id',
    'sort',
]

TL_CONFLICTS_MAP = {
    'resources': ['account_management', 'resource_attributes'],
    'resource_attributes': ['resources', 'account_management'],
    'account_management': ['resources', 'resource_attributes'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    resources=dict(
        required=False,
        elements='',
        type='list'),
    description=dict(
        required=False,
        type='str'),
    transaction_id=dict(
        required=False,
        type='str'),
    rule_conditions=dict(
        required=False,
        elements='',
        type='list'),
    rule_operator=dict(
        required=False,
        type='str'),
    ibm_id=dict(
        required=False,
        type='str'),
    roles=dict(
        required=False,
        elements='',
        type='list'),
    resource_attributes=dict(
        required=False,
        elements='',
        type='list'),
    account_management=dict(
        required=False,
        type='bool'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    resource_tags=dict(
        required=False,
        elements='',
        type='list'),
    pattern=dict(
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
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
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
        resource_type='ibm_iam_user_policy',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.66.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_iam_user_policy',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.66.0',
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
