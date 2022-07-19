#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_scc_si_occurrence
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/scc_si_occurrence

short_description: Configure IBM Cloud 'ibm_scc_si_occurrence' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_scc_si_occurrence' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.41.1
    - Terraform v0.12.20

options:
    context:
        description:
            - None
        required: False
        type: list
        elements: dict
    account_id:
        description:
            - None
        required: False
        type: str
    provider_id:
        description:
            - (Required for new resource) Part of the parent. This field contains the provider ID. For example: providers/{provider_id}.
        required: True
        type: str
    note_name:
        description:
            - (Required for new resource) An analysis note associated with this image, in the form "{account_id}/providers/{provider_id}/notes/{note_id}" This field can be used as a filter in list requests.
        required: True
        type: str
    occurrence_id:
        description:
            - (Required for new resource) The id of the occurrence.
        required: True
        type: str
    resource_url:
        description:
            - The unique URL of the resource, image or the container, for which the `Occurrence` applies. For example, https://gcr.io/provider/image@sha256:foo. This field can be used as a filter in list requests.
        required: False
        type: str
    remediation:
        description:
            - A description of actions that can be taken to remedy the `Note`.
        required: False
        type: str
    kpi:
        description:
            - Kpi provides details about a KPI occurrence.
        required: False
        type: list
        elements: dict
    kind:
        description:
            - (Required for new resource) The type of note. Use this field to filter notes and occurences by kind. - FINDING&#58; The note and occurrence represent a finding. - KPI&#58; The note and occurrence represent a KPI value. - CARD&#58; The note represents a card showing findings and related metric values. - CARD_CONFIGURED&#58; The note represents a card configured for a user account. - SECTION&#58; The note represents a section in a dashboard.
        required: True
        type: str
    finding:
        description:
            - Finding provides details about a finding occurrence.
        required: False
        type: list
        elements: dict
    replace_if_exists:
        description:
            - When set to true, an existing occurrence is replaced rather than duplicated.
        required: False
        type: bool
        default: False
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
    ('provider_id', 'str'),
    ('note_name', 'str'),
    ('occurrence_id', 'str'),
    ('kind', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'context',
    'account_id',
    'provider_id',
    'note_name',
    'occurrence_id',
    'resource_url',
    'remediation',
    'kpi',
    'kind',
    'finding',
    'replace_if_exists',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('provider_id', 'str'),
    ('occurrence_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'account_id',
    'provider_id',
    'occurrence_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    context=dict(
        required=False,
        elements='',
        type='list'),
    account_id=dict(
        required=False,
        type='str'),
    provider_id=dict(
        required=False,
        type='str'),
    note_name=dict(
        required=False,
        type='str'),
    occurrence_id=dict(
        required=False,
        type='str'),
    resource_url=dict(
        required=False,
        type='str'),
    remediation=dict(
        required=False,
        type='str'),
    kpi=dict(
        required=False,
        elements='',
        type='list'),
    kind=dict(
        required=False,
        type='str'),
    finding=dict(
        required=False,
        elements='',
        type='list'),
    replace_if_exists=dict(
        required=False,
        type='bool'),
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
        resource_type='ibm_scc_si_occurrence',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.41.1',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_scc_si_occurrence',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.41.1',
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
