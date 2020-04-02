#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_api_gateway_endpoint
short_description: Configure IBM Cloud 'ibm_api_gateway_endpoint' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_api_gateway_endpoint' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.3.0
    - Terraform v0.12.20

options:
    service_instance_crn:
        description:
            - (Required for new resource) Api Gateway Service Instance Crn
        required: False
        type: str
    open_api_doc_name:
        description:
            - (Required for new resource) Json File path
        required: False
        type: str
    routes:
        description:
            - Invokable routes for an endpoint
        required: False
        type: list
        elements: str
    managed:
        description:
            - Managed indicates if endpoint is online or offline.
        required: False
        type: bool
        default: False
    provider_id:
        description:
            - Provider ID of an endpoint allowable values user-defined and whisk
        required: False
        type: str
        default: user-defined
    name:
        description:
            - (Required for new resource) Endpoint name
        required: False
        type: str
    shared:
        description:
            - The Shared status of an endpoint
        required: False
        type: bool
    base_path:
        description:
            - Base path of an endpoint
        required: False
        type: str
    endpoint_id:
        description:
            - Endpoint ID
        required: False
        type: str
    type:
        description:
            - Action type of Endpoint ALoowable values are share, unshare, manage, unmanage
        required: False
        type: str
        default: unshare
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
    ('service_instance_crn', 'str'),
    ('open_api_doc_name', 'str'),
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'service_instance_crn',
    'open_api_doc_name',
    'routes',
    'managed',
    'provider_id',
    'name',
    'shared',
    'base_path',
    'endpoint_id',
    'type',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    service_instance_crn=dict(
        required=False,
        type='str'),
    open_api_doc_name=dict(
        required=False,
        type='str'),
    routes=dict(
        required=False,
        elements='',
        type='list'),
    managed=dict(
        default=False,
        type='bool'),
    provider_id=dict(
        default='user-defined',
        type='str'),
    name=dict(
        required=False,
        type='str'),
    shared=dict(
        required=False,
        type='bool'),
    base_path=dict(
        required=False,
        type='str'),
    endpoint_id=dict(
        required=False,
        type='str'),
    type=dict(
        default='unshare',
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
        resource_type='ibm_api_gateway_endpoint',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.3.0',
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
