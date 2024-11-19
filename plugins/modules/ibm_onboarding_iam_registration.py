#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_onboarding_iam_registration
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/onboarding_iam_registration

short_description: Configure IBM Cloud 'ibm_onboarding_iam_registration' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_onboarding_iam_registration' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    supported_authorization_subjects:
        description:
            - The list of supported authorization subjects.
        required: False
        type: list
        elements: dict
    actions:
        description:
            - The product access management action.
        required: False
        type: list
        elements: dict
    env:
        description:
            - The environment to fetch this object from.
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The IAM registration name, which must be the programmatic name of the product.
        required: True
        type: str
    supported_anonymous_accesses:
        description:
            - The list of supported anonymous accesses.
        required: False
        type: list
        elements: dict
    product_id:
        description:
            - (Required for new resource) The unique ID of the product.
        required: True
        type: str
    additional_policy_scopes:
        description:
            - List of additional policy scopes.
        required: False
        type: list
        elements: str
    display_name:
        description:
            - The display name of the object.
        required: False
        type: list
        elements: dict
    supported_network:
        description:
            - The registration of set of endpoint types that are supported by your service in the `networkType` environment attribute. This constrains the context-based restriction rules specific to the service such that they describe access restrictions on only this set of endpoints.
        required: False
        type: list
        elements: dict
    enabled:
        description:
            - Whether the service is enabled or disabled for IAM.
        required: False
        type: bool
    parent_ids:
        description:
            - The list of parent IDs for product access management.
        required: False
        type: list
        elements: str
    resource_hierarchy_attribute:
        description:
            - The resource hierarchy key-value pair for composite services.
        required: False
        type: list
        elements: dict
    supported_attributes:
        description:
            - The list of supported attributes.
        required: False
        type: list
        elements: dict
    supported_roles:
        description:
            - The list of roles that you can use to assign access.
        required: False
        type: list
        elements: dict
    service_type:
        description:
            - The type of the service.
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
    ('name', 'str'),
    ('product_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'supported_authorization_subjects',
    'actions',
    'env',
    'name',
    'supported_anonymous_accesses',
    'product_id',
    'additional_policy_scopes',
    'display_name',
    'supported_network',
    'enabled',
    'parent_ids',
    'resource_hierarchy_attribute',
    'supported_attributes',
    'supported_roles',
    'service_type',
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
    supported_authorization_subjects=dict(
        required=False,
        elements='',
        type='list'),
    actions=dict(
        required=False,
        elements='',
        type='list'),
    env=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    supported_anonymous_accesses=dict(
        required=False,
        elements='',
        type='list'),
    product_id=dict(
        required=False,
        type='str'),
    additional_policy_scopes=dict(
        required=False,
        elements='',
        type='list'),
    display_name=dict(
        required=False,
        elements='',
        type='list'),
    supported_network=dict(
        required=False,
        elements='',
        type='list'),
    enabled=dict(
        required=False,
        type='bool'),
    parent_ids=dict(
        required=False,
        elements='',
        type='list'),
    resource_hierarchy_attribute=dict(
        required=False,
        elements='',
        type='list'),
    supported_attributes=dict(
        required=False,
        elements='',
        type='list'),
    supported_roles=dict(
        required=False,
        elements='',
        type='list'),
    service_type=dict(
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

    result = ibmcloud_terraform(
        resource_type='ibm_onboarding_iam_registration',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.71.2',
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
