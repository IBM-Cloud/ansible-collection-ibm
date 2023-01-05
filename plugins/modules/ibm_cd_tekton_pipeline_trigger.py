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
    - IBM-Cloud terraform-provider-ibm v1.47.1
    - Terraform v0.12.20

options:
    event_listener:
        description:
            - (Required for new resource) Event listener name. The name of the event listener to which the trigger is associated. The event listeners are defined in the definition repositories of the Tekton pipeline.
        required: True
        type: str
    max_concurrent_runs:
        description:
            - Defines the maximum number of concurrent runs for this trigger. Omit this property to disable the concurrency limit.
        required: False
        type: int
    timezone:
        description:
            - Only needed for timer triggers. Timezone for timer trigger.
        required: False
        type: str
    scm_source:
        description:
            - SCM source repository for a Git trigger. Only needed for Git triggers.
        required: False
        type: list
        elements: dict
    events:
        description:
            - Only needed for Git triggers. Events object defines the events to which this Git trigger listens.
        required: False
        type: list
        elements: dict
    name:
        description:
            - (Required for new resource) Trigger name.
        required: True
        type: str
    disabled:
        description:
            - Flag whether the trigger is disabled. If omitted the trigger is enabled by default.
        required: False
        type: bool
    worker:
        description:
            - Worker used to run the trigger. If not specified the trigger will use the default pipeline worker.
        required: False
        type: list
        elements: dict
    cron:
        description:
            - Only needed for timer triggers. Cron expression for timer trigger.
        required: False
        type: str
    tags:
        description:
            - Trigger tags array.
        required: False
        type: list
        elements: str
    secret:
        description:
            - Only needed for generic webhook trigger type. Secret used to start generic webhook trigger.
        required: False
        type: list
        elements: dict
    pipeline_id:
        description:
            - (Required for new resource) The Tekton pipeline ID.
        required: True
        type: str
    type:
        description:
            - (Required for new resource) Trigger type.
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
    ('event_listener', 'str'),
    ('name', 'str'),
    ('pipeline_id', 'str'),
    ('type', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'event_listener',
    'max_concurrent_runs',
    'timezone',
    'scm_source',
    'events',
    'name',
    'disabled',
    'worker',
    'cron',
    'tags',
    'secret',
    'pipeline_id',
    'type',
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
    event_listener=dict(
        required=False,
        type='str'),
    max_concurrent_runs=dict(
        required=False,
        type='int'),
    timezone=dict(
        required=False,
        type='str'),
    scm_source=dict(
        required=False,
        elements='',
        type='list'),
    events=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=False,
        type='str'),
    disabled=dict(
        required=False,
        type='bool'),
    worker=dict(
        required=False,
        elements='',
        type='list'),
    cron=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    secret=dict(
        required=False,
        elements='',
        type='list'),
    pipeline_id=dict(
        required=False,
        type='str'),
    type=dict(
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
        ibm_provider_version='1.47.1',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_cd_tekton_pipeline_trigger',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.47.1',
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
