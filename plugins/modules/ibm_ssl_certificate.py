#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_ssl_certificate
short_description: Configure IBM Cloud 'ibm_ssl_certificate' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_ssl_certificate' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.6
    - Terraform v0.12.20

options:
    ssl_type:
        description:
            - (Required for new resource) 
        required: False
        type: str
    certificate_signing_request:
        description:
            - (Required for new resource) 
        required: False
        type: str
    administrative_contact_same_as_technical_flag:
        description:
            - None
        required: False
        type: bool
        default: False
    administrative_contact:
        description:
            - None
        required: False
        type: list
        elements: dict
    server_count:
        description:
            - (Required for new resource) 
        required: False
        type: int
    technical_contact:
        description:
            - (Required for new resource) 
        required: False
        type: list
        elements: dict
    billing_contact:
        description:
            - None
        required: False
        type: list
        elements: dict
    technical_contact_same_as_org_address_flag:
        description:
            - None
        required: False
        type: bool
        default: False
    administrative_address_same_as_organization_flag:
        description:
            - None
        required: False
        type: bool
        default: False
    organization_information:
        description:
            - (Required for new resource) 
        required: False
        type: list
        elements: dict
    server_type:
        description:
            - (Required for new resource) 
        required: False
        type: str
    renewal_flag:
        description:
            - None
        required: False
        type: bool
        default: True
    order_approver_email_address:
        description:
            - (Required for new resource) 
        required: False
        type: str
    billing_contact_same_as_technical_flag:
        description:
            - None
        required: False
        type: bool
        default: False
    billing_address_same_as_organization_flag:
        description:
            - None
        required: False
        type: bool
        default: False
    validity_months:
        description:
            - (Required for new resource) 
        required: False
        type: int
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
    ('ssl_type', 'str'),
    ('certificate_signing_request', 'str'),
    ('server_count', 'int'),
    ('technical_contact', 'list'),
    ('organization_information', 'list'),
    ('server_type', 'str'),
    ('order_approver_email_address', 'str'),
    ('validity_months', 'int'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'ssl_type',
    'certificate_signing_request',
    'administrative_contact_same_as_technical_flag',
    'administrative_contact',
    'server_count',
    'technical_contact',
    'billing_contact',
    'technical_contact_same_as_org_address_flag',
    'administrative_address_same_as_organization_flag',
    'organization_information',
    'server_type',
    'renewal_flag',
    'order_approver_email_address',
    'billing_contact_same_as_technical_flag',
    'billing_address_same_as_organization_flag',
    'validity_months',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    ssl_type=dict(
        required=False,
        type='str'),
    certificate_signing_request=dict(
        required=False,
        type='str'),
    administrative_contact_same_as_technical_flag=dict(
        default=False,
        type='bool'),
    administrative_contact=dict(
        required=False,
        elements='',
        type='list'),
    server_count=dict(
        required=False,
        type='int'),
    technical_contact=dict(
        required=False,
        elements='',
        type='list'),
    billing_contact=dict(
        required=False,
        elements='',
        type='list'),
    technical_contact_same_as_org_address_flag=dict(
        default=False,
        type='bool'),
    administrative_address_same_as_organization_flag=dict(
        default=False,
        type='bool'),
    organization_information=dict(
        required=False,
        elements='',
        type='list'),
    server_type=dict(
        required=False,
        type='str'),
    renewal_flag=dict(
        default=True,
        type='bool'),
    order_approver_email_address=dict(
        required=False,
        type='str'),
    billing_contact_same_as_technical_flag=dict(
        default=False,
        type='bool'),
    billing_address_same_as_organization_flag=dict(
        default=False,
        type='bool'),
    validity_months=dict(
        required=False,
        type='int'),
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
        resource_type='ibm_ssl_certificate',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.2.6',
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
