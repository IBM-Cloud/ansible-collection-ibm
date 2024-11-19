#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cbr_zone
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cbr_zone

short_description: Configure IBM Cloud 'ibm_cbr_zone' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cbr_zone' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    description:
        description:
            - The description of the zone.
        required: False
        type: str
    x_correlation_id:
        description:
            - The supplied or generated value of this header is logged for a request and repeated in a response header for the corresponding response. The same value is used for downstream requests and retries of those requests. If a value of this headers is not supplied in a request, the service generates a random (version 4) UUID.
        required: False
        type: str
    transaction_id:
        description:
            - The `Transaction-Id` header behaves as the `X-Correlation-Id` header. It is supported for backward compatibility with other IBM platform services that support the `Transaction-Id` header only. If both `X-Correlation-Id` and `Transaction-Id` are provided, `X-Correlation-Id` has the precedence over `Transaction-Id`.
        required: False
        type: str
    addresses:
        description:
            - The list of addresses in the zone.
        required: False
        type: list
        elements: dict
    name:
        description:
            - (Required for new resource) The name of the zone.
        required: True
        type: str
    excluded:
        description:
            - The list of excluded addresses in the zone. Only addresses of type `ipAddress`, `ipRange`, and `subnet` can be excluded.
        required: False
        type: list
        elements: dict
    account_id:
        description:
            - (Required for new resource) The id of the account owning this zone.
        required: True
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
    ('name', 'str'),
    ('account_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'description',
    'x_correlation_id',
    'transaction_id',
    'addresses',
    'name',
    'excluded',
    'account_id',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('zone_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'zone_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    description=dict(
        required=False,
        type='str'),
    x_correlation_id=dict(
        required=False,
        type='str'),
    transaction_id=dict(
        required=False,
        type='str'),
    addresses=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=False,
        type='str'),
    excluded=dict(
        required=False,
        elements='',
        type='list'),
    account_id=dict(
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
        resource_type='ibm_cbr_zone',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_cbr_zone',
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
