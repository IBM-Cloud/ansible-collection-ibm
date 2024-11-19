#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_code_engine_function
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/code_engine_function

short_description: Configure IBM Cloud 'ibm_code_engine_function' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_code_engine_function' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    name:
        description:
            - (Required for new resource) The name of the function.
        required: True
        type: str
    scale_memory_limit:
        description:
            - Optional amount of memory set for the instance of the function. For valid values see [Supported memory and CPU combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo). The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and M are the shorthand expressions for GB and MB. For more information see [Units of measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        required: False
        type: str
        default: 4G
    code_reference:
        description:
            - (Required for new resource) Specifies either a reference to a code bundle or the source code itself. To specify the source code, use the data URL scheme and include the source code as base64 encoded. The data URL scheme is defined in [RFC 2397](https://tools.ietf.org/html/rfc2397).
        required: True
        type: str
    managed_domain_mappings:
        description:
            - Optional value controlling which of the system managed domain mappings will be setup for the function. Valid values are 'local_public', 'local_private' and 'local'. Visibility can only be 'local_private' if the project supports function private visibility.
        required: False
        type: str
        default: local_public
    scale_concurrency:
        description:
            - Number of parallel requests handled by a single instance, supported only by Node.js, default is `1`.
        required: False
        type: int
        default: 1
    scale_max_execution_time:
        description:
            - Timeout in secs after which the function is terminated.
        required: False
        type: int
        default: 60
    code_secret:
        description:
            - The name of the secret that is used to access the specified `code_reference`. The secret is used to authenticate with a non-public endpoint that is specified as`code_reference`.
        required: False
        type: str
    runtime:
        description:
            - (Required for new resource) The managed runtime used to execute the injected code.
        required: True
        type: str
    scale_down_delay:
        description:
            - Optional amount of time in seconds that delays the scale down behavior for a function.
        required: False
        type: int
        default: 1
    scale_cpu_limit:
        description:
            - Optional amount of CPU set for the instance of the function. For valid values see [Supported memory and CPU combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        required: False
        type: str
        default: 1
    project_id:
        description:
            - (Required for new resource) The ID of the project.
        required: True
        type: str
    code_binary:
        description:
            - Specifies whether the code is binary or not. Defaults to false when `code_reference` is set to a data URL. When `code_reference` is set to a code bundle URL, this field is always true.
        required: False
        type: bool
    code_main:
        description:
            - Specifies the name of the function that should be invoked.
        required: False
        type: str
        default: main
    run_env_variables:
        description:
            - References to config maps, secrets or literal values, which are defined by the function owner and are exposed as environment variables in the function.
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
    ('code_reference', 'str'),
    ('runtime', 'str'),
    ('project_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'name',
    'scale_memory_limit',
    'code_reference',
    'managed_domain_mappings',
    'scale_concurrency',
    'scale_max_execution_time',
    'code_secret',
    'runtime',
    'scale_down_delay',
    'scale_cpu_limit',
    'project_id',
    'code_binary',
    'code_main',
    'run_env_variables',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('name', 'str'),
    ('project_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'name',
    'project_id',
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
    scale_memory_limit=dict(
        required=False,
        type='str'),
    code_reference=dict(
        required=False,
        type='str'),
    managed_domain_mappings=dict(
        required=False,
        type='str'),
    scale_concurrency=dict(
        required=False,
        type='int'),
    scale_max_execution_time=dict(
        required=False,
        type='int'),
    code_secret=dict(
        required=False,
        type='str'),
    runtime=dict(
        required=False,
        type='str'),
    scale_down_delay=dict(
        required=False,
        type='int'),
    scale_cpu_limit=dict(
        required=False,
        type='str'),
    project_id=dict(
        required=False,
        type='str'),
    code_binary=dict(
        required=False,
        type='bool'),
    code_main=dict(
        required=False,
        type='str'),
    run_env_variables=dict(
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
        resource_type='ibm_code_engine_function',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_code_engine_function',
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
