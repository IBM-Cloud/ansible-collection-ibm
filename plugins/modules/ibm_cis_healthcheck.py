#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cis_healthcheck
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cis_healthcheck

short_description: Configure IBM Cloud 'ibm_cis_healthcheck' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cis_healthcheck' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    cis_id:
        description:
            - (Required for new resource) CIS instance crn
        required: True
        type: str
    expected_body:
        description:
            - expected_body
        required: False
        type: str
    allow_insecure:
        description:
            - allow_insecure
        required: False
        type: bool
        default: False
    headers:
        description:
            - None
        required: False
        type: list
        elements: dict
    path:
        description:
            - path
        required: False
        type: str
        default: /
    method:
        description:
            - method
        required: False
        type: str
        default: GET
    timeout:
        description:
            - timeout
        required: False
        type: int
        default: 5
    retries:
        description:
            - retries
        required: False
        type: int
        default: 2
    interval:
        description:
            - interval
        required: False
        type: int
        default: 60
    expected_codes:
        description:
            - expected_codes
        required: False
        type: str
    type:
        description:
            - type
        required: False
        type: str
        default: http
    description:
        description:
            - description
        required: False
        type: str
        default:  
    follow_redirects:
        description:
            - follow_redirects
        required: False
        type: bool
        default: False
    port:
        description:
            - port number
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
    ('cis_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'cis_id',
    'expected_body',
    'allow_insecure',
    'headers',
    'path',
    'method',
    'timeout',
    'retries',
    'interval',
    'expected_codes',
    'type',
    'description',
    'follow_redirects',
    'port',
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
    cis_id=dict(
        required=False,
        type='str'),
    expected_body=dict(
        required=False,
        type='str'),
    allow_insecure=dict(
        required=False,
        type='bool'),
    headers=dict(
        required=False,
        elements='',
        type='list'),
    path=dict(
        required=False,
        type='str'),
    method=dict(
        required=False,
        type='str'),
    timeout=dict(
        required=False,
        type='int'),
    retries=dict(
        required=False,
        type='int'),
    interval=dict(
        required=False,
        type='int'),
    expected_codes=dict(
        required=False,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    description=dict(
        required=False,
        type='str'),
    follow_redirects=dict(
        required=False,
        type='bool'),
    port=dict(
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
        resource_type='ibm_cis_healthcheck',
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
