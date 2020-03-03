#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_ssl_certificate
short_description: Configure IBM Cloud 'ibm_compute_ssl_certificate' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_compute_ssl_certificate' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.3
    - Terraform v0.12.20

options:
    modify_date:
        description:
            - None
        required: False
        type: str
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    validity_begin:
        description:
            - None
        required: False
        type: str
    key_size:
        description:
            - None
        required: False
        type: int
    create_date:
        description:
            - None
        required: False
        type: str
    common_name:
        description:
            - None
        required: False
        type: str
    organization_name:
        description:
            - None
        required: False
        type: str
    validity_days:
        description:
            - None
        required: False
        type: int
    validity_end:
        description:
            - None
        required: False
        type: str
    certificate:
        description:
            - (Required for new resource) 
        required: False
        type: str
    intermediate_certificate:
        description:
            - None
        required: False
        type: str
    private_key:
        description:
            - (Required for new resource) 
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
    ('certificate', 'str'),
    ('private_key', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'modify_date',
    'tags',
    'validity_begin',
    'key_size',
    'create_date',
    'common_name',
    'organization_name',
    'validity_days',
    'validity_end',
    'certificate',
    'intermediate_certificate',
    'private_key',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    modify_date=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    validity_begin=dict(
        required=False,
        type='str'),
    key_size=dict(
        required=False,
        type='int'),
    create_date=dict(
        required=False,
        type='str'),
    common_name=dict(
        required=False,
        type='str'),
    organization_name=dict(
        required=False,
        type='str'),
    validity_days=dict(
        required=False,
        type='int'),
    validity_end=dict(
        required=False,
        type='str'),
    certificate=dict(
        required=False,
        type='str'),
    intermediate_certificate=dict(
        required=False,
        type='str'),
    private_key=dict(
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
        resource_type='ibm_compute_ssl_certificate',
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
