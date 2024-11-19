#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_app_config_snapshot
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/app_config_snapshot

short_description: Configure IBM Cloud 'ibm_app_config_snapshot' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_app_config_snapshot' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    git_config_id:
        description:
            - (Required for new resource) Git config id. Allowed special characters are dot ( . ), hyphen( - ), underscore ( _ ) only
        required: True
        type: str
    git_token:
        description:
            - (Required for new resource) Git token, this needs to be provided with enough permission to write and update the file.
        required: True
        type: str
    git_config_name:
        description:
            - (Required for new resource) Git config name. Allowed special characters are dot ( . ), hyphen( - ), underscore ( _ ) only
        required: True
        type: str
    git_branch:
        description:
            - (Required for new resource) Branch name to which you need to write or update the configuration.
        required: True
        type: str
    action:
        description:
            - action promote
        required: False
        type: str
    guid:
        description:
            - (Required for new resource) GUID of the App Configuration service. Get it from the service instance credentials section of the dashboard.
        required: True
        type: str
    environment_id:
        description:
            - (Required for new resource) Environment id.
        required: True
        type: str
    git_url:
        description:
            - (Required for new resource) Git url which will be used to connect to the github account.
        required: True
        type: str
    git_file_path:
        description:
            - (Required for new resource) Git file path, this is a path where your configuration file will be written.
        required: True
        type: str
    collection_id:
        description:
            - (Required for new resource) Collection id.
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
    ('git_config_id', 'str'),
    ('git_token', 'str'),
    ('git_config_name', 'str'),
    ('git_branch', 'str'),
    ('guid', 'str'),
    ('environment_id', 'str'),
    ('git_url', 'str'),
    ('git_file_path', 'str'),
    ('collection_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'git_config_id',
    'git_token',
    'git_config_name',
    'git_branch',
    'action',
    'guid',
    'environment_id',
    'git_url',
    'git_file_path',
    'collection_id',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('guid', 'str'),
    ('git_config_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'guid',
    'git_config_id',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    git_config_id=dict(
        required=False,
        type='str'),
    git_token=dict(
        required=False,
        type='str'),
    git_config_name=dict(
        required=False,
        type='str'),
    git_branch=dict(
        required=False,
        type='str'),
    action=dict(
        required=False,
        type='str'),
    guid=dict(
        required=False,
        type='str'),
    environment_id=dict(
        required=False,
        type='str'),
    git_url=dict(
        required=False,
        type='str'),
    git_file_path=dict(
        required=False,
        type='str'),
    collection_id=dict(
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
        resource_type='ibm_app_config_snapshot',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_app_config_snapshot',
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
