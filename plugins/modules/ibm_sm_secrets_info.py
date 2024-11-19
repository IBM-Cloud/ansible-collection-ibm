#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_sm_secrets_info
for_more_info: refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/sm_secrets

short_description: Retrieve IBM Cloud 'ibm_sm_secrets' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_sm_secrets' resource
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    match_all_labels:
        description:
            - Filter secrets by a label or a combination of labels.
        required: False
        type: list
        elements: str
    instance_id:
        description:
            - The ID of the Secrets Manager instance.
        required: True
        type: str
    endpoint_type:
        description:
            - public or private.
        required: False
        type: str
    groups:
        description:
            - Filter secrets by groups. You can apply multiple filters by using a comma-separated list of secret group IDs. If you need to filter secrets that are in the default secret group, use the `default` keyword.
        required: False
        type: str
    secret_types:
        description:
            - Filter secrets by secret types.
        required: False
        type: list
        elements: str
    region:
        description:
            - The region of the Secrets Manager instance.
        required: False
        type: str
    sort:
        description:
            - Sort a collection of secrets by the specified field in ascending order. To sort in descending order use the `-` character. Available values: id | created_at | updated_at | expiration_date | secret_type | name
        required: False
        type: str
    search:
        description:
            - Obtain a collection of secrets that contain the specified string in one or more of the fields: `id`, `name`, `description`,
        `labels`, `secret_type`.
        required: False
        type: str
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
    ('instance_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'match_all_labels',
    'instance_id',
    'endpoint_type',
    'groups',
    'secret_types',
    'region',
    'sort',
    'search',
]


TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    match_all_labels=dict(
        required=False,
        elements='',
        type='list'),
    instance_id=dict(
        required=True,
        type='str'),
    endpoint_type=dict(
        required=False,
        type='str'),
    groups=dict(
        required=False,
        type='str'),
    secret_types=dict(
        required=False,
        elements='',
        type='list'),
    region=dict(
        required=False,
        type='str'),
    sort=dict(
        required=False,
        type='str'),
    search=dict(
        required=False,
        type='str'),
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

    result = ibmcloud_terraform(
        resource_type='ibm_sm_secrets',
        tf_type='data',
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
