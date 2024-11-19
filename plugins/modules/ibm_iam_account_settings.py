#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_iam_account_settings
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/iam_account_settings

short_description: Configure IBM Cloud 'ibm_iam_account_settings' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_iam_account_settings' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    user_mfa:
        description:
            - List of users that are exempted from the MFA requirement of the account.
        required: False
        type: list
        elements: dict
    max_sessions_per_identity:
        description:
            - Defines the max allowed sessions per identity required by the account. Value values:  * Any whole number greater than 0  * NOT_SET - To unset account setting and use service default.
        required: False
        type: str
    restrict_create_platform_apikey:
        description:
            - Defines whether or not creating platform API keys is access controlled. Valid values:  * RESTRICTED - to apply access control  * NOT_RESTRICTED - to remove access control  * NOT_SET - to 'unset' a previous set value.
        required: False
        type: str
    if_match:
        description:
            - Version of the account settings to be updated. Specify the version that you retrieved as entity_tag (ETag header) when reading the account. This value helps identifying parallel usage of this API. Pass * to indicate to update any version available. This might result in stale updates.
        required: False
        type: str
        default: *
    session_invalidation_in_seconds:
        description:
            - Defines the period of time in seconds in which a session will be invalidated due to inactivity. Valid values:  * Any whole number between '900' and '7200'  * NOT_SET - To unset account setting and use service default.
        required: False
        type: str
    system_access_token_expiration_in_seconds:
        description:
            - Defines the access token expiration in seconds. Valid values:  * Any whole number between '900' and '3600'  * NOT_SET - To unset account setting and use service default.
        required: False
        type: str
    include_history:
        description:
            - Defines if the entity history is included in the response.
        required: False
        type: bool
        default: False
    restrict_create_service_id:
        description:
            - Defines whether or not creating a Service Id is access controlled. Valid values:  * RESTRICTED - to apply access control  * NOT_RESTRICTED - to remove access control  * NOT_SET - to 'unset' a previous set value.
        required: False
        type: str
    session_expiration_in_seconds:
        description:
            - Defines the session expiration in seconds for the account. Valid values:  * Any whole number between between '900' and '86400'  * NOT_SET - To unset account setting and use service default.
        required: False
        type: str
    system_refresh_token_expiration_in_seconds:
        description:
            - Defines the refresh token expiration in seconds. Valid values:  * Any whole number between '900' and '2592000'  * NOT_SET - To unset account setting and use service default.
        required: False
        type: str
    entity_tag:
        description:
            - Version of the account settings.
        required: False
        type: str
    mfa:
        description:
            - Defines the MFA trait for the account. Valid values:  * NONE - No MFA trait set  * TOTP - For all non-federated IBMId users  * TOTP4ALL - For all users  * LEVEL1 - Email-based MFA for all users  * LEVEL2 - TOTP-based MFA for all users  * LEVEL3 - U2F MFA for all users.
        required: False
        type: str
    allowed_ip_addresses:
        description:
            - Defines the IP addresses and subnets from which IAM tokens can be created for the account.
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
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'user_mfa',
    'max_sessions_per_identity',
    'restrict_create_platform_apikey',
    'if_match',
    'session_invalidation_in_seconds',
    'system_access_token_expiration_in_seconds',
    'include_history',
    'restrict_create_service_id',
    'session_expiration_in_seconds',
    'system_refresh_token_expiration_in_seconds',
    'entity_tag',
    'mfa',
    'allowed_ip_addresses',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
    'include_history',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    user_mfa=dict(
        required=False,
        elements='',
        type='list'),
    max_sessions_per_identity=dict(
        required=False,
        type='str'),
    restrict_create_platform_apikey=dict(
        required=False,
        type='str'),
    if_match=dict(
        required=False,
        type='str'),
    session_invalidation_in_seconds=dict(
        required=False,
        type='str'),
    system_access_token_expiration_in_seconds=dict(
        required=False,
        type='str'),
    include_history=dict(
        required=False,
        type='bool'),
    restrict_create_service_id=dict(
        required=False,
        type='str'),
    session_expiration_in_seconds=dict(
        required=False,
        type='str'),
    system_refresh_token_expiration_in_seconds=dict(
        required=False,
        type='str'),
    entity_tag=dict(
        required=False,
        type='str'),
    mfa=dict(
        required=False,
        type='str'),
    allowed_ip_addresses=dict(
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

    result_ds = ibmcloud_terraform(
        resource_type='ibm_iam_account_settings',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_iam_account_settings',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.71.2',
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
