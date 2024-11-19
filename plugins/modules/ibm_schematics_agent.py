#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_schematics_agent
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/schematics_agent

short_description: Configure IBM Cloud 'ibm_schematics_agent' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_schematics_agent' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    schematics_location:
        description:
            - (Required for new resource) List of locations supported by IBM Cloud Schematics service.  While creating your workspace or action, choose the right region, since it cannot be changed.  Note, this does not limit the location of the IBM Cloud resources, provisioned using Schematics.
        required: True
        type: str
    tags:
        description:
            - Tags for the agent.
        required: False
        type: list
        elements: str
    agent_inputs:
        description:
            - Additional input variables for the agent.
        required: False
        type: list
        elements: dict
    user_state:
        description:
            - User defined status of the agent.
        required: False
        type: list
        elements: dict
    name:
        description:
            - (Required for new resource) The name of the agent (must be unique, for an account).
        required: True
        type: str
    resource_group:
        description:
            - (Required for new resource) The resource-group name for the agent.  By default, agent will be registered in Default Resource Group.
        required: True
        type: str
    version:
        description:
            - (Required for new resource) Agent version.
        required: True
        type: str
    agent_location:
        description:
            - (Required for new resource) The location where agent is deployed in the user environment.
        required: True
        type: str
    agent_infrastructure:
        description:
            - (Required for new resource) The infrastructure parameters used by the agent.
        required: True
        type: list
        elements: dict
    description:
        description:
            - Agent description.
        required: False
        type: str
    agent_metadata:
        description:
            - The metadata of an agent.
        required: False
        type: list
        elements: dict
    run_destroy_resources:
        description:
            - Argument which helps to run destroy resources job. Increment the value to destroy resources associated with agent deployment.
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
    ('schematics_location', 'str'),
    ('name', 'str'),
    ('resource_group', 'str'),
    ('version', 'str'),
    ('agent_location', 'str'),
    ('agent_infrastructure', 'list'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'schematics_location',
    'tags',
    'agent_inputs',
    'user_state',
    'name',
    'resource_group',
    'version',
    'agent_location',
    'agent_infrastructure',
    'description',
    'agent_metadata',
    'run_destroy_resources',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('agent_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'agent_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    schematics_location=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    agent_inputs=dict(
        required=False,
        elements='',
        type='list'),
    user_state=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=False,
        type='str'),
    resource_group=dict(
        required=False,
        type='str'),
    version=dict(
        required=False,
        type='str'),
    agent_location=dict(
        required=False,
        type='str'),
    agent_infrastructure=dict(
        required=False,
        elements='',
        type='list'),
    description=dict(
        required=False,
        type='str'),
    agent_metadata=dict(
        required=False,
        elements='',
        type='list'),
    run_destroy_resources=dict(
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

    result_ds = ibmcloud_terraform(
        resource_type='ibm_schematics_agent',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_schematics_agent',
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
