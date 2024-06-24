#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_logs_alert
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/logs_alert

short_description: Configure IBM Cloud 'ibm_logs_alert' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_logs_alert' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.66.0
    - Terraform v1.5.5

options:
    name:
        description:
            - (Required for new resource) Alert name.
        required: True
        type: str
    notification_groups:
        description:
            - (Required for new resource) Alert notification groups.
        required: True
        type: list
        elements: dict
    notification_payload_filters:
        description:
            - JSON keys to include in the alert notification, if left empty get the full log text in the alert notification.
        required: False
        type: list
        elements: str
    expiration:
        description:
            - Alert expiration date.
        required: False
        type: list
        elements: dict
    condition:
        description:
            - (Required for new resource) Alert condition.
        required: True
        type: list
        elements: dict
    filters:
        description:
            - (Required for new resource) Alert filters.
        required: True
        type: list
        elements: dict
    meta_labels:
        description:
            - The Meta labels to add to the alert.
        required: False
        type: list
        elements: dict
    meta_labels_strings:
        description:
            - The Meta labels to add to the alert as string with ':' separator.
        required: False
        type: list
        elements: str
    description:
        description:
            - Alert description.
        required: False
        type: str
    is_active:
        description:
            - (Required for new resource) Alert is active.
        required: True
        type: bool
    severity:
        description:
            - (Required for new resource) Alert severity.
        required: True
        type: str
    instance_id:
        description:
            - (Required for new resource) The ID of the logs instance.
        required: True
        type: str
    region:
        description:
            - The region of the logs instance.
        required: False
        type: str
    tracing_alert:
        description:
            - The definition for tracing alert.
        required: False
        type: list
        elements: dict
    incident_settings:
        description:
            - Incident settings, will create the incident based on this configuration.
        required: False
        type: list
        elements: dict
    active_when:
        description:
            - When should the alert be active.
        required: False
        type: list
        elements: dict
    endpoint_type:
        description:
            - public or private.
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
    ('name', 'str'),
    ('notification_groups', 'list'),
    ('condition', 'list'),
    ('filters', 'list'),
    ('is_active', 'bool'),
    ('severity', 'str'),
    ('instance_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'name',
    'notification_groups',
    'notification_payload_filters',
    'expiration',
    'condition',
    'filters',
    'meta_labels',
    'meta_labels_strings',
    'description',
    'is_active',
    'severity',
    'instance_id',
    'region',
    'tracing_alert',
    'incident_settings',
    'active_when',
    'endpoint_type',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('instance_id', 'str'),
    ('logs_alert_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'region',
    'endpoint_type',
    'instance_id',
    'logs_alert_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    name=dict(
        required=False,
        type='str'),
    notification_groups=dict(
        required=False,
        elements='',
        type='list'),
    notification_payload_filters=dict(
        required=False,
        elements='',
        type='list'),
    expiration=dict(
        required=False,
        elements='',
        type='list'),
    condition=dict(
        required=False,
        elements='',
        type='list'),
    filters=dict(
        required=False,
        elements='',
        type='list'),
    meta_labels=dict(
        required=False,
        elements='',
        type='list'),
    meta_labels_strings=dict(
        required=False,
        elements='',
        type='list'),
    description=dict(
        required=False,
        type='str'),
    is_active=dict(
        required=False,
        type='bool'),
    severity=dict(
        required=False,
        type='str'),
    instance_id=dict(
        required=False,
        type='str'),
    region=dict(
        required=False,
        type='str'),
    tracing_alert=dict(
        required=False,
        elements='',
        type='list'),
    incident_settings=dict(
        required=False,
        elements='',
        type='list'),
    active_when=dict(
        required=False,
        elements='',
        type='list'),
    endpoint_type=dict(
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
        resource_type='ibm_logs_alert',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.66.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_logs_alert',
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
