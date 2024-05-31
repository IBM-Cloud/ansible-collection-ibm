#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_code_engine_job
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/code_engine_job

short_description: Configure IBM Cloud 'ibm_code_engine_job' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_code_engine_job' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.65.1
    - Terraform v1.5.5

options:
    name:
        description:
            - (Required for new resource) The name of the job. Use a name that is unique within the project.
        required: True
        type: str
    image_secret:
        description:
            - The name of the image registry access secret. The image registry access secret is used to authenticate with a private registry when you download the container image. If the image reference points to a registry that requires authentication, the job / job runs will be created but submitted job runs will fail, until this property is provided, too. This property must not be set on a job run, which references a job template.
        required: False
        type: str
    scale_array_spec:
        description:
            - Define a custom set of array indices as comma-separated list containing single values and hyphen-separated ranges like `5,12-14,23,27`. Each instance can pick up its array index via environment variable `JOB_INDEX`. The number of unique array indices specified here determines the number of job instances to run.
        required: False
        type: str
        default: 0
    project_id:
        description:
            - (Required for new resource) The ID of the project.
        required: True
        type: str
    run_mode:
        description:
            - The mode for runs of the job. Valid values are `task` and `daemon`. In `task` mode, the `scale_max_execution_time` and `scale_retry_limit` properties apply. In `daemon` mode, since there is no timeout and failed instances are restarted indefinitely, the `scale_max_execution_time` and `scale_retry_limit` properties are not allowed.
        required: False
        type: str
        default: task
    run_service_account:
        description:
            - The name of the service account. For built-in service accounts, you can use the shortened names `manager`, `none`, `reader`, and `writer`. This property must not be set on a job run, which references a job template.
        required: False
        type: str
        default: default
    scale_memory_limit:
        description:
            - Optional amount of memory set for the instance of the job. For valid values see [Supported memory and CPU combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo). The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and M are the shorthand expressions for GB and MB. For more information see [Units of measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        required: False
        type: str
        default: 4G
    run_commands:
        description:
            - Set commands for the job that are passed to start job run containers. If not specified an empty string array will be applied and the command specified by the container image, will be used to start the container.
        required: False
        type: list
        elements: str
    run_env_variables:
        description:
            - Optional references to config maps, secrets or a literal values.
        required: False
        type: list
        elements: dict
    run_volume_mounts:
        description:
            - Optional mounts of config maps or a secrets.
        required: False
        type: list
        elements: dict
    scale_cpu_limit:
        description:
            - Optional amount of CPU set for the instance of the job. For valid values see [Supported memory and CPU combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        required: False
        type: str
        default: 1
    scale_ephemeral_storage_limit:
        description:
            - Optional amount of ephemeral storage to set for the instance of the job. The amount specified as ephemeral storage, must not exceed the amount of `scale_memory_limit`. The units for specifying ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M are the shorthand expressions for GB and MB. For more information see [Units of measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        required: False
        type: str
        default: 400M
    image_reference:
        description:
            - (Required for new resource) The name of the image that is used for this job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and `TAG` are optional. If `REGISTRY` is not specified, the default is `docker.io`. If `TAG` is not specified, the default is `latest`. If the image reference points to a registry that requires authentication, make sure to also specify the property `image_secret`.
        required: True
        type: str
    run_arguments:
        description:
            - Set arguments for the job that are passed to start job run containers. If not specified an empty string array will be applied and the arguments specified by the container image, will be used to start the container.
        required: False
        type: list
        elements: str
    run_as_user:
        description:
            - The user ID (UID) to run the application (e.g., 1001).
        required: False
        type: int
        default: 0
    scale_max_execution_time:
        description:
            - The maximum execution time in seconds for runs of the job. This property can only be specified if `run_mode` is `task`.
        required: False
        type: int
        default: 7200
    scale_retry_limit:
        description:
            - The number of times to rerun an instance of the job before the job is marked as failed. This property can only be specified if `run_mode` is `task`.
        required: False
        type: int
        default: 3
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
    ('name', 'str'),
    ('project_id', 'str'),
    ('image_reference', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'name',
    'image_secret',
    'scale_array_spec',
    'project_id',
    'run_mode',
    'run_service_account',
    'scale_memory_limit',
    'run_commands',
    'run_env_variables',
    'run_volume_mounts',
    'scale_cpu_limit',
    'scale_ephemeral_storage_limit',
    'image_reference',
    'run_arguments',
    'run_as_user',
    'scale_max_execution_time',
    'scale_retry_limit',
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
    image_secret=dict(
        required=False,
        type='str'),
    scale_array_spec=dict(
        required=False,
        type='str'),
    project_id=dict(
        required=False,
        type='str'),
    run_mode=dict(
        required=False,
        type='str'),
    run_service_account=dict(
        required=False,
        type='str'),
    scale_memory_limit=dict(
        required=False,
        type='str'),
    run_commands=dict(
        required=False,
        elements='',
        type='list'),
    run_env_variables=dict(
        required=False,
        elements='',
        type='list'),
    run_volume_mounts=dict(
        required=False,
        elements='',
        type='list'),
    scale_cpu_limit=dict(
        required=False,
        type='str'),
    scale_ephemeral_storage_limit=dict(
        required=False,
        type='str'),
    image_reference=dict(
        required=False,
        type='str'),
    run_arguments=dict(
        required=False,
        elements='',
        type='list'),
    run_as_user=dict(
        required=False,
        type='int'),
    scale_max_execution_time=dict(
        required=False,
        type='int'),
    scale_retry_limit=dict(
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
        resource_type='ibm_code_engine_job',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.65.1',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_code_engine_job',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.65.1',
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
