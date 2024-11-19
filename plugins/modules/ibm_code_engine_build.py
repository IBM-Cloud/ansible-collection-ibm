#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_code_engine_build
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/code_engine_build

short_description: Configure IBM Cloud 'ibm_code_engine_build' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_code_engine_build' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    output_secret:
        description:
            - (Required for new resource) The secret that is required to access the image registry. Make sure that the secret is granted with push permissions towards the specified container registry namespace.
        required: True
        type: str
    source_secret:
        description:
            - Name of the secret that is used access the repository source. This field is optional if the `source_type` is `git`. Additionally, if the `source_url` points to a repository that requires authentication, the build will be created but cannot access any source code, until this property is provided, too. If the `source_type` value is `local`, this field must be omitted.
        required: False
        type: str
    source_url:
        description:
            - The URL of the code repository. This field is required if the `source_type` is `git`. If the `source_type` value is `local`, this field must be omitted. If the repository is publicly available you can provide a 'https' URL like `https://github.com/IBM/CodeEngine`. If the repository requires authentication, you need to provide a 'ssh' URL like `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that points to a secret of format `ssh_auth`.
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The name of the build.
        required: True
        type: str
    source_type:
        description:
            - Specifies the type of source to determine if your build source is in a repository or based on local source code.* local - For builds from local source code.* git - For builds from git version controlled source code.
        required: False
        type: str
        default: git
    strategy_spec_file:
        description:
            - Optional path to the specification file that is used for build strategies for building an image.
        required: False
        type: str
        default: Dockerfile
    project_id:
        description:
            - (Required for new resource) The ID of the project.
        required: True
        type: str
    source_context_dir:
        description:
            - Optional directory in the repository that contains the buildpacks file or the Dockerfile.
        required: False
        type: str
    source_revision:
        description:
            - Commit, tag, or branch in the source repository to pull. This field is optional if the `source_type` is `git` and uses the HEAD of default branch if not specified. If the `source_type` value is `local`, this field must be omitted.
        required: False
        type: str
    strategy_size:
        description:
            - Optional size for the build, which determines the amount of resources used. Build sizes are `small`, `medium`, `large`, `xlarge`, `xxlarge`.
        required: False
        type: str
        default: medium
    strategy_type:
        description:
            - (Required for new resource) The strategy to use for building the image.
        required: True
        type: str
    timeout:
        description:
            - The maximum amount of time, in seconds, that can pass before the build must succeed or fail.
        required: False
        type: int
        default: 600
    output_image:
        description:
            - (Required for new resource) The name of the image.
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
    ('output_secret', 'str'),
    ('name', 'str'),
    ('project_id', 'str'),
    ('strategy_type', 'str'),
    ('output_image', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'output_secret',
    'source_secret',
    'source_url',
    'name',
    'source_type',
    'strategy_spec_file',
    'project_id',
    'source_context_dir',
    'source_revision',
    'strategy_size',
    'strategy_type',
    'timeout',
    'output_image',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('project_id', 'str'),
    ('name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'project_id',
    'name',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    output_secret=dict(
        required=False,
        type='str'),
    source_secret=dict(
        required=False,
        type='str'),
    source_url=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    source_type=dict(
        required=False,
        type='str'),
    strategy_spec_file=dict(
        required=False,
        type='str'),
    project_id=dict(
        required=False,
        type='str'),
    source_context_dir=dict(
        required=False,
        type='str'),
    source_revision=dict(
        required=False,
        type='str'),
    strategy_size=dict(
        required=False,
        type='str'),
    strategy_type=dict(
        required=False,
        type='str'),
    timeout=dict(
        required=False,
        type='int'),
    output_image=dict(
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
        resource_type='ibm_code_engine_build',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_code_engine_build',
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
