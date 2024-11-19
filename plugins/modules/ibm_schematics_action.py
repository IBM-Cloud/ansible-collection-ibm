#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_schematics_action
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/schematics_action

short_description: Configure IBM Cloud 'ibm_schematics_action' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_schematics_action' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    description:
        description:
            - Action description.
        required: False
        type: str
    tags:
        description:
            - Action tags.
        required: False
        type: list
        elements: str
    source_readme_url:
        description:
            - URL of the `README` file, for the source URL.
        required: False
        type: str
    source:
        description:
            - Source of templates, playbooks, or controls.
        required: False
        type: list
        elements: dict
    targets_ini:
        description:
            - Inventory of host and host group for the playbook in `INI` file format. For example, `"targets_ini": "[webserverhost]  172.22.192.6  [dbhost]  172.22.192.5"`. For more information, about an inventory host group syntax, see [Inventory host groups](https://cloud.ibm.com/docs/schematics?topic=schematics-schematics-cli-reference#schematics-inventory-host-grps).
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The unique name of your action. The name can be up to 128 characters long and can include alphanumeric characters, spaces, dashes, and underscores. **Example** you can use the name to stop action.
        required: True
        type: str
    user_state:
        description:
            - User defined status of the Schematics object.
        required: False
        type: list
        elements: dict
    x_github_token:
        description:
            - The personal access token to authenticate with your private GitHub or GitLab repository and access your Terraform template.
        required: False
        type: str
    action_outputs:
        description:
            - Output variables for the Action.
        required: False
        type: list
        elements: dict
    resource_group:
        description:
            - Resource-group name for an action.  By default, action is created in default resource group.
        required: False
        type: str
    credentials:
        description:
            - credentials of the Action.
        required: False
        type: list
        elements: dict
    location:
        description:
            - List of locations supported by IBM Cloud Schematics service.  While creating your workspace or action, choose the right region, since it cannot be changed.  Note, this does not limit the location of the IBM Cloud resources, provisioned using Schematics.
        required: False
        type: str
    command_parameter:
        description:
            - Schematics job command parameter (playbook-name).
        required: False
        type: str
    inventory:
        description:
            - Target inventory record ID, used by the action or ansible playbook.
        required: False
        type: str
    bastion:
        description:
            - Describes a bastion resource.
        required: False
        type: list
        elements: dict
    action_inputs:
        description:
            - Input variables for the Action.
        required: False
        type: list
        elements: dict
    settings:
        description:
            - Environment variables for the Action.
        required: False
        type: list
        elements: dict
    source_type:
        description:
            - Type of source for the Template.
        required: False
        type: str
    bastion_credential:
        description:
            - User editable variable data & system generated reference to value.
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
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'description',
    'tags',
    'source_readme_url',
    'source',
    'targets_ini',
    'name',
    'user_state',
    'x_github_token',
    'action_outputs',
    'resource_group',
    'credentials',
    'location',
    'command_parameter',
    'inventory',
    'bastion',
    'action_inputs',
    'settings',
    'source_type',
    'bastion_credential',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('action_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'location',
    'action_id',
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
    tags=dict(
        required=False,
        elements='',
        type='list'),
    source_readme_url=dict(
        required=False,
        type='str'),
    source=dict(
        required=False,
        elements='',
        type='list'),
    targets_ini=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    user_state=dict(
        required=False,
        elements='',
        type='list'),
    x_github_token=dict(
        required=False,
        type='str'),
    action_outputs=dict(
        required=False,
        elements='',
        type='list'),
    resource_group=dict(
        required=False,
        type='str'),
    credentials=dict(
        required=False,
        elements='',
        type='list'),
    location=dict(
        required=False,
        type='str'),
    command_parameter=dict(
        required=False,
        type='str'),
    inventory=dict(
        required=False,
        type='str'),
    bastion=dict(
        required=False,
        elements='',
        type='list'),
    action_inputs=dict(
        required=False,
        elements='',
        type='list'),
    settings=dict(
        required=False,
        elements='',
        type='list'),
    source_type=dict(
        required=False,
        type='str'),
    bastion_credential=dict(
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
        resource_type='ibm_schematics_action',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_schematics_action',
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
