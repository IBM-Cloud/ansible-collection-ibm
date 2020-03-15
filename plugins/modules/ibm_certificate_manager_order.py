#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_certificate_manager_order
short_description: Configure IBM Cloud 'ibm_certificate_manager_order' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_certificate_manager_order' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.4
    - Terraform v0.12.20

options:
    domains:
        description:
            - (Required for new resource) 
        required: False
        type: list
        elements: str
    rotate_keys:
        description:
            - None
        required: False
        type: bool
        default: False
    description:
        description:
            - None
        required: False
        type: str
    domain_validation_method:
        description:
            - None
        required: False
        type: str
        default: dns - 01
    key_algorithm:
        description:
            - None
        required: False
        type: str
    certificate_manager_instance_id:
        description:
            - (Required for new resource) 
        required: False
        type: str
    issuer:
        description:
            - None
        required: False
        type: str
    expires_on:
        description:
            - None
        required: False
        type: int
    has_previous:
        description:
            - None
        required: False
        type: str
    name:
        description:
            - (Required for new resource) 
        required: False
        type: str
    begins_on:
        description:
            - None
        required: False
        type: int
    status:
        description:
            - None
        required: False
        type: str
    dns_provider_instance_crn:
        description:
            - None
        required: False
        type: str
    algorithm:
        description:
            - None
        required: False
        type: str
    imported:
        description:
            - None
        required: False
        type: bool
    issuance_info:
        description:
            - None
        required: False
        type: dict
        elements: dict
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
    ('domains', 'list'),
    ('certificate_manager_instance_id', 'str'),
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'domains',
    'rotate_keys',
    'description',
    'domain_validation_method',
    'key_algorithm',
    'certificate_manager_instance_id',
    'issuer',
    'expires_on',
    'has_previous',
    'name',
    'begins_on',
    'status',
    'dns_provider_instance_crn',
    'algorithm',
    'imported',
    'issuance_info',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    domains=dict(
        required=False,
        elements='',
        type='list'),
    rotate_keys=dict(
        default=False,
        type='bool'),
    description=dict(
        required=False,
        type='str'),
    domain_validation_method=dict(
        default='dns - 01',
        type='str'),
    key_algorithm=dict(
        required=False,
        type='str'),
    certificate_manager_instance_id=dict(
        required=False,
        type='str'),
    issuer=dict(
        required=False,
        type='str'),
    expires_on=dict(
        required=False,
        type='int'),
    has_previous=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    begins_on=dict(
        required=False,
        type='int'),
    status=dict(
        required=False,
        type='str'),
    dns_provider_instance_crn=dict(
        required=False,
        type='str'),
    algorithm=dict(
        required=False,
        type='str'),
    imported=dict(
        required=False,
        type='bool'),
    issuance_info=dict(
        required=False,
        elements='',
        type='dict'),
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
        resource_type='ibm_certificate_manager_order',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.2.4',
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
