#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_schematics_workspace
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/schematics_workspace

short_description: Configure IBM Cloud 'ibm_schematics_workspace' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_schematics_workspace' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    template_git_release:
        description:
            - The repository release.
        required: False
        type: str
    frozen_by:
        description:
            - The user ID that froze the workspace.
        required: False
        type: str
    template_type:
        description:
            - (Required for new resource) The Terraform version that you want to use to run your Terraform code. Enter `terraform_v0.12` to use Terraform version 0.12, and `terraform_v0.11` to use Terraform version 0.11. The Terraform config files are run with Terraform version 0.11. This is a required variable. Make sure that your Terraform config files are compatible with the Terraform version that you select.
        required: True
        type: str
    template_git_branch:
        description:
            - The repository branch.
        required: False
        type: str
    description:
        description:
            - The description of the workspace.
        required: False
        type: str
    tags:
        description:
            - A list of tags that are associated with the workspace.
        required: False
        type: list
        elements: str
    locked_by:
        description:
            - The user ID that initiated a resource-related action, such as applying or destroying resources, that locked the workspace.
        required: False
        type: str
    template_init_state_file:
        description:
            - The content of an existing Terraform statefile that you want to import in to your workspace. To get the content of a Terraform statefile for a specific Terraform template in an existing workspace, run `ibmcloud schematics state pull --id <workspace_id> --template <template_id>`.
        required: False
        type: str
    frozen:
        description:
            - If set to true, the workspace is frozen and changes to the workspace are disabled.
        required: False
        type: bool
    template_uninstall_script_name:
        description:
            - Uninstall script name.
        required: False
        type: str
    template_values_metadata:
        description:
            - List of values metadata.
        required: False
        type: list
        elements: dict
    template_git_repo_url:
        description:
            - The repository URL.
        required: False
        type: str
    locked:
        description:
            - If set to true, the workspace is locked and disabled for changes.
        required: False
        type: bool
    locked_time:
        description:
            - The timestamp when the workspace was locked.
        required: False
        type: str
    shared_data:
        description:
            - Information about the Target used by the templates originating from the  IBM Cloud catalog offerings. This information is not relevant for workspace created using your own Terraform template.
        required: False
        type: list
        elements: dict
    template_env_settings:
        description:
            - A list of environment variables that you want to apply during the execution of a bash script or Terraform job. This field must be provided as a list of key-value pairs, for example, **TF_LOG=debug**. Each entry will be a map with one entry where `key is the environment variable name and value is value`. You can define environment variables for IBM Cloud catalog offerings that are provisioned by using a bash script. See [example to use special environment variable](https://cloud.ibm.com/docs/schematics?topic=schematics-set-parallelism#parallelism-example)  that are supported by Schematics.
        required: False
        type: list
        elements: dict
    template_git_repo_sha_value:
        description:
            - The repository SHA value.
        required: False
        type: str
    template_git_has_uploadedgitrepotar:
        description:
            - Has uploaded git repo tar
        required: False
        type: bool
    frozen_at:
        description:
            - The timestamp when the workspace was frozen.
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The name of your workspace. The name can be up to 128 characters long and can include alphanumeric characters, spaces, dashes, and underscores. When you create a workspace for your own Terraform template, consider including the microservice component that you set up with your Terraform template and the IBM Cloud environment where you want to deploy your resources in your name.
        required: True
        type: str
    template_values:
        description:
            - A list of variable values that you want to apply during the Helm chart installation. The list must be provided in JSON format, such as `"autoscaling: enabled: true minReplicas: 2"`. The values that you define here override the default Helm chart values. This field is supported only for IBM Cloud catalog offerings that are provisioned by using the Terraform Helm provider.
        required: False
        type: str
    template_inputs:
        description:
            - VariablesRequest -.
        required: False
        type: list
        elements: dict
    x_github_token:
        description:
            - The personal access token to authenticate with your private GitHub or GitLab repository and access your Terraform template.
        required: False
        type: str
    applied_shareddata_ids:
        description:
            - List of applied shared dataset ID.
        required: False
        type: list
        elements: str
    catalog_ref:
        description:
            - Information about the software template that you chose from the IBM Cloud catalog. This information is returned for IBM Cloud catalog offerings only.
        required: False
        type: list
        elements: dict
    location:
        description:
            - The location where you want to create your Schematics workspace and run the Schematics jobs. The location that you enter must match the API endpoint that you use. For example, if you use the Frankfurt API endpoint, you must specify `eu-de` as your location. If you use an API endpoint for a geography and you do not specify a location, Schematics determines the location based on availability.
        required: False
        type: str
    resource_group:
        description:
            - The ID of the resource group where you want to provision the workspace.
        required: False
        type: str
    template_git_url:
        description:
            - The source URL.
        required: False
        type: str
    template_git_folder:
        description:
            - The subfolder in your GitHub or GitLab repository where your Terraform template is stored.
        required: False
        type: str
    template_ref:
        description:
            - Workspace template ref.
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
    ('template_type', 'str'),
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'template_git_release',
    'frozen_by',
    'template_type',
    'template_git_branch',
    'description',
    'tags',
    'locked_by',
    'template_init_state_file',
    'frozen',
    'template_uninstall_script_name',
    'template_values_metadata',
    'template_git_repo_url',
    'locked',
    'locked_time',
    'shared_data',
    'template_env_settings',
    'template_git_repo_sha_value',
    'template_git_has_uploadedgitrepotar',
    'frozen_at',
    'name',
    'template_values',
    'template_inputs',
    'x_github_token',
    'applied_shareddata_ids',
    'catalog_ref',
    'location',
    'resource_group',
    'template_git_url',
    'template_git_folder',
    'template_ref',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('workspace_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'template_values_metadata',
    'template_git_has_uploadedgitrepotar',
    'location',
    'workspace_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    template_git_release=dict(
        required=False,
        type='str'),
    frozen_by=dict(
        required=False,
        type='str'),
    template_type=dict(
        required=False,
        type='str'),
    template_git_branch=dict(
        required=False,
        type='str'),
    description=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    locked_by=dict(
        required=False,
        type='str'),
    template_init_state_file=dict(
        required=False,
        type='str'),
    frozen=dict(
        required=False,
        type='bool'),
    template_uninstall_script_name=dict(
        required=False,
        type='str'),
    template_values_metadata=dict(
        required=False,
        elements='',
        type='list'),
    template_git_repo_url=dict(
        required=False,
        type='str'),
    locked=dict(
        required=False,
        type='bool'),
    locked_time=dict(
        required=False,
        type='str'),
    shared_data=dict(
        required=False,
        elements='',
        type='list'),
    template_env_settings=dict(
        required=False,
        elements='',
        type='list'),
    template_git_repo_sha_value=dict(
        required=False,
        type='str'),
    template_git_has_uploadedgitrepotar=dict(
        required=False,
        type='bool'),
    frozen_at=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    template_values=dict(
        required=False,
        type='str'),
    template_inputs=dict(
        required=False,
        elements='',
        type='list'),
    x_github_token=dict(
        required=False,
        type='str'),
    applied_shareddata_ids=dict(
        required=False,
        elements='',
        type='list'),
    catalog_ref=dict(
        required=False,
        elements='',
        type='list'),
    location=dict(
        required=False,
        type='str'),
    resource_group=dict(
        required=False,
        type='str'),
    template_git_url=dict(
        required=False,
        type='str'),
    template_git_folder=dict(
        required=False,
        type='str'),
    template_ref=dict(
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
        resource_type='ibm_schematics_workspace',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_schematics_workspace',
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
