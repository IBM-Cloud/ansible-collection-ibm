#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_user
short_description: Configure IBM Cloud 'ibm_compute_user' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_compute_user' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.6.0
    - Terraform v0.12.20

options:
    username:
        description:
            - user name
        required: False
        type: str
    last_name:
        description:
            - (Required for new resource) Last name of the user
        required: False
        type: str
    city:
        description:
            - (Required for new resource) City name
        required: False
        type: str
    country:
        description:
            - (Required for new resource) Country name
        required: False
        type: str
    api_key:
        description:
            - API key for the user
        required: False
        type: str
    company_name:
        description:
            - (Required for new resource) comapany name
        required: False
        type: str
    address1:
        description:
            - (Required for new resource) Address info of the user
        required: False
        type: str
    address2:
        description:
            - Address info of the user
        required: False
        type: str
    password:
        description:
            - password for the user
        required: False
        type: str
    has_api_key:
        description:
            - API Key info of the user
        required: False
        type: bool
        default: False
    first_name:
        description:
            - (Required for new resource) First name of the user
        required: False
        type: str
    state_:
        description:
            - (Required for new resource) Satate name
        required: False
        type: str
    timezone:
        description:
            - (Required for new resource) time zone info
        required: False
        type: str
    ibm_id:
        description:
            - IBM ID of the  user
        required: False
        type: str
    email:
        description:
            - (Required for new resource) email address of the user
        required: False
        type: str
    user_status:
        description:
            - user status info
        required: False
        type: str
        default: ACTIVE
    permissions:
        description:
            - set of persmissions assigned for the user
        required: False
        type: list
        elements: str
    tags:
        description:
            - Tags set for the resources
        required: False
        type: list
        elements: str
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
    ('last_name', 'str'),
    ('city', 'str'),
    ('country', 'str'),
    ('company_name', 'str'),
    ('address1', 'str'),
    ('first_name', 'str'),
    ('state_', 'str'),
    ('timezone', 'str'),
    ('email', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'username',
    'last_name',
    'city',
    'country',
    'api_key',
    'company_name',
    'address1',
    'address2',
    'password',
    'has_api_key',
    'first_name',
    'state_',
    'timezone',
    'ibm_id',
    'email',
    'user_status',
    'permissions',
    'tags',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    username=dict(
        required=False,
        type='str'),
    last_name=dict(
        required=False,
        type='str'),
    city=dict(
        required=False,
        type='str'),
    country=dict(
        required=False,
        type='str'),
    api_key=dict(
        required=False,
        type='str'),
    company_name=dict(
        required=False,
        type='str'),
    address1=dict(
        required=False,
        type='str'),
    address2=dict(
        required=False,
        type='str'),
    password=dict(
        required=False,
        type='str'),
    has_api_key=dict(
        default=False,
        type='bool'),
    first_name=dict(
        required=False,
        type='str'),
    state_=dict(
        required=False,
        type='str'),
    timezone=dict(
        required=False,
        type='str'),
    ibm_id=dict(
        required=False,
        type='str'),
    email=dict(
        required=False,
        type='str'),
    user_status=dict(
        default='ACTIVE',
        type='str'),
    permissions=dict(
        required=False,
        elements='',
        type='list'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
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

    result = ibmcloud_terraform(
        resource_type='ibm_compute_user',
        tf_type='resource',
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
