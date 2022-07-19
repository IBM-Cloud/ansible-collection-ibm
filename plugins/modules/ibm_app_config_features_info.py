#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_app_config_features_info
for_more_info: refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/app_config_features

short_description: Retrieve IBM Cloud 'ibm_app_config_features' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_app_config_features' resource
requirements:
    - IBM-Cloud terraform-provider-ibm v1.41.1
    - Terraform v0.12.20

options:
    environment_id:
        description:
            - Environment Id.
        required: True
        type: str
    sort:
        description:
            - Sort the feature details based on the specified attribute.
        required: False
        type: str
    collections:
        description:
            - Filter features by a list of comma separated collections.
        required: False
        type: list
        elements: str
    guid:
        description:
            - GUID of the App Configuration service. Get it from the service instance credentials section of the dashboard.
        required: True
        type: str
    tags:
        description:
            - Filter the resources to be returned based on the associated tags. Specify the parameter as a list of comma separated tags. Returns resources associated with any of the specified tags.
        required: False
        type: str
    offset:
        description:
            - The number of records to skip. By specifying `offset`, you retrieve a subset of items that starts with the `offset` value. Use `offset` with `limit` to page through the available records.
        required: False
        type: int
    limit:
        description:
            - The number of records to retrieve. By default, the list operation return the first 10 records. To retrieve different set of records, use `limit` with `offset` to page through the available records.
        required: False
        type: int
    segments:
        description:
            - Filter features by a list of comma separated segments.
        required: False
        type: list
        elements: str
    expand:
        description:
            - If set to `true`, returns expanded view of the resource details.
        required: False
        type: bool
    includes:
        description:
            - Include the associated collections or targeting rules details in the response.
        required: False
        type: list
        elements: str
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
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
    ('environment_id', 'str'),
    ('guid', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'environment_id',
    'sort',
    'collections',
    'guid',
    'tags',
    'offset',
    'limit',
    'segments',
    'expand',
    'includes',
]


TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    environment_id=dict(
        required=True,
        type='str'),
    sort=dict(
        required=False,
        type='str'),
    collections=dict(
        required=False,
        elements='',
        type='list'),
    guid=dict(
        required=True,
        type='str'),
    tags=dict(
        required=False,
        type='str'),
    offset=dict(
        required=False,
        type='int'),
    limit=dict(
        required=False,
        type='int'),
    segments=dict(
        required=False,
        elements='',
        type='list'),
    expand=dict(
        required=False,
        type='bool'),
    includes=dict(
        required=False,
        elements='',
        type='list'),
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
        resource_type='ibm_app_config_features',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.41.1',
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
