#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_lb_listener_policy
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_lb_listener_policy

short_description: Configure IBM Cloud 'ibm_is_lb_listener_policy' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_lb_listener_policy' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.66.0
    - Terraform v1.5.5

options:
    action:
        description:
            - (Required for new resource) Policy Action
        required: True
        type: str
    name:
        description:
            - Policy name
        required: False
        type: str
    listener:
        description:
            - (Required for new resource) Listener ID
        required: True
        type: str
    priority:
        description:
            - (Required for new resource) Listener Policy Priority
        required: True
        type: int
    lb:
        description:
            - (Required for new resource) Load Balancer Listener Policy
        required: True
        type: str
    target:
        description:
            - - If `action` is `forward`, the response is a `LoadBalancerPoolReference`- If `action` is `redirect`, the response is a `LoadBalancerListenerPolicyRedirectURL`- If `action` is `https_redirect`, the response is a `LoadBalancerListenerHTTPSRedirect`.
        required: False
        type: list
        elements: dict
    rules:
        description:
            - Policy Rules
        required: False
        type: list
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
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
        type: str
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
    ('action', 'str'),
    ('listener', 'str'),
    ('priority', 'int'),
    ('lb', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'action',
    'name',
    'listener',
    'priority',
    'lb',
    'target',
    'rules',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('lb', 'str'),
    ('listener', 'str'),
    ('policy_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'lb',
    'listener',
    'policy_id',
]

TL_CONFLICTS_MAP = {
    'target': ['target_url', 'target_http_status_code', 'target_id', 'target_https_redirect_listener', 'target_https_redirect_uri', 'target_https_redirect_status_code'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    action=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    listener=dict(
        required=False,
        type='str'),
    priority=dict(
        required=False,
        type='int'),
    lb=dict(
        required=False,
        type='str'),
    target=dict(
        required=False,
        elements='',
        type='list'),
    rules=dict(
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

    # VPC required arguments checks
    if module.params['generation'] == 1:
        missing_args = []
        if module.params['iaas_classic_username'] is None:
            missing_args.append('iaas_classic_username')
        if module.params['iaas_classic_api_key'] is None:
            missing_args.append('iaas_classic_api_key')
        if missing_args:
            module.fail_json(msg=(
                "VPC generation=1 missing required arguments: " +
                ", ".join(missing_args)))
    elif module.params['generation'] == 2:
        if module.params['ibmcloud_api_key'] is None:
            module.fail_json(
                msg=("VPC generation=2 missing required argument: "
                     "ibmcloud_api_key"))

    result_ds = ibmcloud_terraform(
        resource_type='ibm_is_lb_listener_policy',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.66.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_lb_listener_policy',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.66.0',
            tl_required_params=TL_REQUIRED_PARAMETERS,
            tl_all_params=TL_ALL_PARAMETERS)
        if result['rc'] > 0:
            module.fail_json(
                msg=Terraform.parse_stderr(result['stderr']), **result)

        module.exit_json(**result)
    else:
        module.exit_json(**result_ds)


def main():
    run_module()


if __name__ == '__main__':
    main()
