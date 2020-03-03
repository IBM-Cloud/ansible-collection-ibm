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
    - IBM-Cloud terraform-provider-ibm v1.2.3
    - Terraform v0.12.20

options:
    last_name:
        description:
            - (Required for new resource) 
        required: False
        type: str
    company_name:
        description:
            - (Required for new resource) 
        required: False
        type: str
    timezone:
        description:
            - (Required for new resource) 
        required: False
        type: str
    user_status:
        description:
            - None
        required: False
        type: str
        default: ACTIVE
    api_key:
        description:
            - None
        required: False
        type: str
    ibm_id:
        description:
            - None
        required: False
        type: str
    first_name:
        description:
            - (Required for new resource) 
        required: False
        type: str
    email:
        description:
            - (Required for new resource) 
        required: False
        type: str
    address1:
        description:
            - (Required for new resource) 
        required: False
        type: str
    state_:
        description:
            - (Required for new resource) 
        required: False
        type: str
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    username:
        description:
            - None
        required: False
        type: str
    password:
        description:
            - None
        required: False
        type: str
    permissions:
        description:
            - None
        required: False
        type: list
        elements: str
    has_api_key:
        description:
            - None
        required: False
        type: bool
        default: False
    country:
        description:
            - (Required for new resource) 
        required: False
        type: str
    city:
        description:
            - (Required for new resource) 
        required: False
        type: str
    address2:
        description:
            - None
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
            - The API Key used for authentification. This can also be provided
              via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('last_name', 'str'),
    ('company_name', 'str'),
    ('timezone', 'str'),
    ('first_name', 'str'),
    ('email', 'str'),
    ('address1', 'str'),
    ('state_', 'str'),
    ('country', 'str'),
    ('city', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'last_name',
    'company_name',
    'timezone',
    'user_status',
    'api_key',
    'ibm_id',
    'first_name',
    'email',
    'address1',
    'state_',
    'tags',
    'username',
    'password',
    'permissions',
    'has_api_key',
    'country',
    'city',
    'address2',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    last_name=dict(
        required=False,
        type='str'),
    company_name=dict(
        required=False,
        type='str'),
    timezone=dict(
        required=False,
        type='str'),
    user_status=dict(
        default='ACTIVE',
        type='str'),
    api_key=dict(
        required=False,
        type='str'),
    ibm_id=dict(
        required=False,
        type='str'),
    first_name=dict(
        required=False,
        type='str'),
    email=dict(
        required=False,
        type='str'),
    address1=dict(
        required=False,
        type='str'),
    state_=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    username=dict(
        required=False,
        type='str'),
    password=dict(
        required=False,
        type='str'),
    permissions=dict(
        required=False,
        elements='',
        type='list'),
    has_api_key=dict(
        default=False,
        type='bool'),
    country=dict(
        required=False,
        type='str'),
    city=dict(
        required=False,
        type='str'),
    address2=dict(
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
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south')
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
        resource_type='ibm_compute_user',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.2.3',
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
