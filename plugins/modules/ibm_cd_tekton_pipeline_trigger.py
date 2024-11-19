#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cd_tekton_pipeline_trigger
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cd_tekton_pipeline_trigger

short_description: Configure IBM Cloud 'ibm_cd_tekton_pipeline_trigger' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cd_tekton_pipeline_trigger' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    secret:
        description:
            - Only needed for Generic Webhook trigger type. The secret is used to start the Generic Webhook trigger.
        required: False
        type: list
        elements: dict
    enabled:
        description:
            - Flag to check if the trigger is enabled.
        required: False
        type: bool
        default: True
    cron:
        description:
            - Only needed for timer triggers. CRON expression that indicates when this trigger will activate. Maximum frequency is every 5 minutes. The string is based on UNIX crontab syntax: minute, hour, day of month, month, day of week. Example: The CRON expression 0 *_/2 * * * - translates to - every 2 hours.
        required: False
        type: str
    tags:
        description:
            - Optional trigger tags array.
        required: False
        type: list
        elements: str
    events:
        description:
            - Either 'events' or 'filter' is required specifically for Git triggers. Stores a list of events that a Git trigger listens to. Choose one or more from 'push', 'pull_request', and 'pull_request_closed'. If SCM repositories use the 'merge request' term, they correspond to the generic term i.e. 'pull request'.
        required: False
        type: list
        elements: str
    favorite:
        description:
            - Mark the trigger as a favorite.
        required: False
        type: bool
        default: False
    source:
        description:
            - Source repository for a Git trigger. Only required for Git triggers. The referenced repository URL must match the URL of a repository tool integration in the parent toolchain. Obtain the list of integrations from the toolchain API https://cloud.ibm.com/apidocs/toolchain#list-tools.
        required: False
        type: list
        elements: dict
    filter:
        description:
            - Either 'events' or 'filter' can be used. Stores the CEL (Common Expression Language) expression value which is used for event filtering against the Git webhook payloads.
        required: False
        type: str
    type:
        description:
            - (Required for new resource) Trigger type.
        required: True
        type: str
    name:
        description:
            - (Required for new resource) Trigger name.
        required: True
        type: str
    worker:
        description:
            - Details of the worker used to run the trigger.
        required: False
        type: list
        elements: dict
    max_concurrent_runs:
        description:
            - Defines the maximum number of concurrent runs for this trigger. If omitted then the concurrency limit is disabled for this trigger.
        required: False
        type: int
    enable_events_from_forks:
        description:
            - When enabled, pull request events from forks of the selected repository will trigger a pipeline run.
        required: False
        type: bool
        default: False
    timezone:
        description:
            - Only used for timer triggers. Specify the timezone used for this timer trigger, which will ensure the CRON activates this trigger relative to the specified timezone. If no timezone is specified, the default timezone used is UTC. Valid timezones are those listed in the IANA timezone database, https://www.iana.org/time-zones.
        required: False
        type: str
    pipeline_id:
        description:
            - (Required for new resource) The Tekton pipeline ID.
        required: True
        type: str
    event_listener:
        description:
            - (Required for new resource) Event listener name. The name of the event listener to which the trigger is associated. The event listeners are defined in the definition repositories of the Tekton pipeline.
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
    ('type', 'str'),
    ('name', 'str'),
    ('pipeline_id', 'str'),
    ('event_listener', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'secret',
    'enabled',
    'cron',
    'tags',
    'events',
    'favorite',
    'source',
    'filter',
    'type',
    'name',
    'worker',
    'max_concurrent_runs',
    'enable_events_from_forks',
    'timezone',
    'pipeline_id',
    'event_listener',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('trigger_id', 'str'),
    ('pipeline_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'trigger_id',
    'pipeline_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    secret=dict(
        required=False,
        elements='',
        type='list'),
    enabled=dict(
        required=False,
        type='bool'),
    cron=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    events=dict(
        required=False,
        elements='',
        type='list'),
    favorite=dict(
        required=False,
        type='bool'),
    source=dict(
        required=False,
        elements='',
        type='list'),
    filter=dict(
        required=False,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    worker=dict(
        required=False,
        elements='',
        type='list'),
    max_concurrent_runs=dict(
        required=False,
        type='int'),
    enable_events_from_forks=dict(
        required=False,
        type='bool'),
    timezone=dict(
        required=False,
        type='str'),
    pipeline_id=dict(
        required=False,
        type='str'),
    event_listener=dict(
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
        resource_type='ibm_cd_tekton_pipeline_trigger',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_cd_tekton_pipeline_trigger',
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
