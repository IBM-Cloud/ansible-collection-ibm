#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_logs_dashboard
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/logs_dashboard

short_description: Configure IBM Cloud 'ibm_logs_dashboard' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_logs_dashboard' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    filters:
        description:
            - List of filters that can be applied to the dashboard's data.
        required: False
        type: list
        elements: dict
    folder_id:
        description:
            - Unique identifier of the folder containing the dashboard.
        required: False
        type: list
        elements: dict
    two_minutes:
        description:
            - Auto refresh interval is set to two minutes.
        required: False
        type: list
        elements: dict
    five_minutes:
        description:
            - Auto refresh interval is set to five minutes.
        required: False
        type: list
        elements: dict
    endpoint_type:
        description:
            - public or private.
        required: False
        type: str
    name:
        description:
            - (Required for new resource) Display name of the dashboard.
        required: True
        type: str
    description:
        description:
            - Brief description or summary of the dashboard's purpose or content.
        required: False
        type: str
    variables:
        description:
            - List of variables that can be used within the dashboard for dynamic content.
        required: False
        type: list
        elements: dict
    href:
        description:
            - Unique identifier for the dashboard.
        required: False
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
    layout:
        description:
            - (Required for new resource) Layout configuration for the dashboard's visual elements.
        required: True
        type: list
        elements: dict
    folder_path:
        description:
            - Path of the folder containing the dashboard.
        required: False
        type: list
        elements: dict
    false:
        description:
            - Auto refresh interval is set to off.
        required: False
        type: list
        elements: dict
    annotations:
        description:
            - List of annotations that can be applied to the dashboard's visual elements.
        required: False
        type: list
        elements: dict
    absolute_time_frame:
        description:
            - Absolute time frame specifying a fixed start and end time.
        required: False
        type: list
        elements: dict
    relative_time_frame:
        description:
            - Relative time frame specifying a duration from the current time.
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
    ('instance_id', 'str'),
    ('layout', 'list'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'filters',
    'folder_id',
    'two_minutes',
    'five_minutes',
    'endpoint_type',
    'name',
    'description',
    'variables',
    'href',
    'instance_id',
    'region',
    'layout',
    'folder_path',
    'false',
    'annotations',
    'absolute_time_frame',
    'relative_time_frame',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('instance_id', 'str'),
    ('dashboard_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'instance_id',
    'dashboard_id',
    'region',
    'endpoint_type',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    filters=dict(
        required=False,
        elements='',
        type='list'),
    folder_id=dict(
        required=False,
        elements='',
        type='list'),
    two_minutes=dict(
        required=False,
        elements='',
        type='list'),
    five_minutes=dict(
        required=False,
        elements='',
        type='list'),
    endpoint_type=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    description=dict(
        required=False,
        type='str'),
    variables=dict(
        required=False,
        elements='',
        type='list'),
    href=dict(
        required=False,
        type='str'),
    instance_id=dict(
        required=False,
        type='str'),
    region=dict(
        required=False,
        type='str'),
    layout=dict(
        required=False,
        elements='',
        type='list'),
    folder_path=dict(
        required=False,
        elements='',
        type='list'),
    false=dict(
        required=False,
        elements='',
        type='list'),
    annotations=dict(
        required=False,
        elements='',
        type='list'),
    absolute_time_frame=dict(
        required=False,
        elements='',
        type='list'),
    relative_time_frame=dict(
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
        resource_type='ibm_logs_dashboard',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_logs_dashboard',
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
