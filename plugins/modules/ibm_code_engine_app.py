#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_code_engine_app
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/code_engine_app

short_description: Configure IBM Cloud 'ibm_code_engine_app' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_code_engine_app' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    image_port:
        description:
            - Optional port the app listens on. While the app will always be exposed via port `443` for end users, this port is used to connect to the port that is exposed by the container image.
        required: False
        type: int
        default: 8080
    scale_request_timeout:
        description:
            - Optional amount of time in seconds that is allowed for a running app to respond to a request.
        required: False
        type: int
        default: 300
    image_reference:
        description:
            - (Required for new resource) The name of the image that is used for this app. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and `TAG` are optional. If `REGISTRY` is not specified, the default is `docker.io`. If `TAG` is not specified, the default is `latest`. If the image reference points to a registry that requires authentication, make sure to also specify the property `image_secret`.
        required: True
        type: str
    run_as_user:
        description:
            - Optional user ID (UID) to run the app.
        required: False
        type: int
        default: 0
    run_volume_mounts:
        description:
            - Mounts of config maps or secrets.
        required: False
        type: list
        elements: dict
    scale_max_instances:
        description:
            - Optional maximum number of instances for this app. If you set this value to `0`, this property does not set a upper scaling limit. However, the app scaling is still limited by the project quota for instances. See [Limits and quotas for Code Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits).
        required: False
        type: int
        default: 10
    probe_liveness:
        description:
            - Response model for probes.
        required: False
        type: list
        elements: dict
    run_env_variables:
        description:
            - References to config maps, secrets or literal values, which are exposed as environment variables in the application.
        required: False
        type: list
        elements: dict
    managed_domain_mappings:
        description:
            - Optional value controlling which of the system managed domain mappings will be setup for the application. Valid values are 'local_public', 'local_private' and 'local'. Visibility can only be 'local_private' if the project supports application private visibility.
        required: False
        type: str
        default: local_public
    probe_readiness:
        description:
            - Response model for probes.
        required: False
        type: list
        elements: dict
    run_arguments:
        description:
            - Optional arguments for the app that are passed to start the container. If not specified an empty string array will be applied and the arguments specified by the container image, will be used to start the container.
        required: False
        type: list
        elements: str
    run_commands:
        description:
            - Optional commands for the app that are passed to start the container. If not specified an empty string array will be applied and the command specified by the container image, will be used to start the container.
        required: False
        type: list
        elements: str
    scale_concurrency_target:
        description:
            - Optional threshold of concurrent requests per instance at which one or more additional instances are created. Use this value to scale up instances based on concurrent number of requests. This option defaults to the value of the `scale_concurrency` option, if not specified.
        required: False
        type: int
    project_id:
        description:
            - (Required for new resource) The ID of the project.
        required: True
        type: str
    image_secret:
        description:
            - Optional name of the image registry access secret. The image registry access secret is used to authenticate with a private registry when you download the container image. If the image reference points to a registry that requires authentication, the app will be created but cannot reach the ready status, until this property is provided, too.
        required: False
        type: str
    scale_concurrency:
        description:
            - Optional maximum number of requests that can be processed concurrently per instance.
        required: False
        type: int
        default: 100
    scale_down_delay:
        description:
            - Optional amount of time in seconds that delays the scale-down behavior for an app instance.
        required: False
        type: int
        default: 0
    name:
        description:
            - (Required for new resource) The name of the app.
        required: True
        type: str
    run_service_account:
        description:
            - Optional name of the service account. For built-in service accounts, you can use the shortened names `manager` , `none`, `reader`, and `writer`.
        required: False
        type: str
        default: default
    scale_cpu_limit:
        description:
            - Optional number of CPU set for the instance of the app. For valid values see [Supported memory and CPU combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).
        required: False
        type: str
        default: 1
    scale_ephemeral_storage_limit:
        description:
            - Optional amount of ephemeral storage to set for the instance of the app. The amount specified as ephemeral storage, must not exceed the amount of `scale_memory_limit`. The units for specifying ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M are the shorthand expressions for GB and MB. For more information see [Units of measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        required: False
        type: str
        default: 400M
    scale_initial_instances:
        description:
            - Optional initial number of instances that are created upon app creation or app update.
        required: False
        type: int
        default: 1
    scale_memory_limit:
        description:
            - Optional amount of memory set for the instance of the app. For valid values see [Supported memory and CPU combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo). The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and M are the shorthand expressions for GB and MB. For more information see [Units of measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).
        required: False
        type: str
        default: 4G
    scale_min_instances:
        description:
            - Optional minimum number of instances for this app. If you set this value to `0`, the app will scale down to zero, if not hit by any request for some time.
        required: False
        type: int
        default: 0
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
    ('image_reference', 'str'),
    ('project_id', 'str'),
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'image_port',
    'scale_request_timeout',
    'image_reference',
    'run_as_user',
    'run_volume_mounts',
    'scale_max_instances',
    'probe_liveness',
    'run_env_variables',
    'managed_domain_mappings',
    'probe_readiness',
    'run_arguments',
    'run_commands',
    'scale_concurrency_target',
    'project_id',
    'image_secret',
    'scale_concurrency',
    'scale_down_delay',
    'name',
    'run_service_account',
    'scale_cpu_limit',
    'scale_ephemeral_storage_limit',
    'scale_initial_instances',
    'scale_memory_limit',
    'scale_min_instances',
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
    image_port=dict(
        required=False,
        type='int'),
    scale_request_timeout=dict(
        required=False,
        type='int'),
    image_reference=dict(
        required=False,
        type='str'),
    run_as_user=dict(
        required=False,
        type='int'),
    run_volume_mounts=dict(
        required=False,
        elements='',
        type='list'),
    scale_max_instances=dict(
        required=False,
        type='int'),
    probe_liveness=dict(
        required=False,
        elements='',
        type='list'),
    run_env_variables=dict(
        required=False,
        elements='',
        type='list'),
    managed_domain_mappings=dict(
        required=False,
        type='str'),
    probe_readiness=dict(
        required=False,
        elements='',
        type='list'),
    run_arguments=dict(
        required=False,
        elements='',
        type='list'),
    run_commands=dict(
        required=False,
        elements='',
        type='list'),
    scale_concurrency_target=dict(
        required=False,
        type='int'),
    project_id=dict(
        required=False,
        type='str'),
    image_secret=dict(
        required=False,
        type='str'),
    scale_concurrency=dict(
        required=False,
        type='int'),
    scale_down_delay=dict(
        required=False,
        type='int'),
    name=dict(
        required=False,
        type='str'),
    run_service_account=dict(
        required=False,
        type='str'),
    scale_cpu_limit=dict(
        required=False,
        type='str'),
    scale_ephemeral_storage_limit=dict(
        required=False,
        type='str'),
    scale_initial_instances=dict(
        required=False,
        type='int'),
    scale_memory_limit=dict(
        required=False,
        type='str'),
    scale_min_instances=dict(
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
        resource_type='ibm_code_engine_app',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_code_engine_app',
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
