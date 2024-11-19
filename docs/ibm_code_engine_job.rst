
ibm_code_engine_job -- Configure IBM Cloud 'ibm_code_engine_job' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_code_engine_job' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/code_engine_job

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  run_as_user (False, int, 0)
    The user ID (UID) to run the job.


  scale_memory_limit (False, str, 4G)
    Optional amount of memory set for the instance of the job. For valid values see [Supported memory and CPU combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo). The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and M are the shorthand expressions for GB and MB. For more information see [Units of measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).


  image_secret (False, str, None)
    The name of the image registry access secret. The image registry access secret is used to authenticate with a private registry when you download the container image. If the image reference points to a registry that requires authentication, the job / job runs will be created but submitted job runs will fail, until this property is provided, too. This property must not be set on a job run, which references a job template.


  run_mode (False, str, task)
    The mode for runs of the job. Valid values are `task` and `daemon`. In `task` mode, the `max_execution_time` and `retry_limit` properties apply. In `daemon` mode, since there is no timeout and failed instances are restarted indefinitely, the `max_execution_time` and `retry_limit` properties are not allowed.


  run_service_account (False, str, default)
    The name of the service account. For built-in service accounts, you can use the shortened names `manager`, `none`, `reader`, and `writer`. This property must not be set on a job run, which references a job template.


  scale_array_spec (False, str, 0)
    Define a custom set of array indices as a comma-separated list containing single values and hyphen-separated ranges, such as  5,12-14,23,27. Each instance gets its array index value from the environment variable JOB_INDEX. The number of unique array indices that you specify with this parameter determines the number of job instances to run.


  project_id (True, str, None)
    (Required for new resource) The ID of the project.


  run_arguments (False, list, None)
    Set arguments for the job that are passed to start job run containers. If not specified an empty string array will be applied and the arguments specified by the container image, will be used to start the container.


  scale_retry_limit (False, int, 3)
    The number of times to rerun an instance of the job before the job is marked as failed. This property can only be specified if `run_mode` is `task`.


  scale_cpu_limit (False, str, 1)
    Optional amount of CPU set for the instance of the job. For valid values see [Supported memory and CPU combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).


  scale_ephemeral_storage_limit (False, str, 400M)
    Optional amount of ephemeral storage to set for the instance of the job. The amount specified as ephemeral storage, must not exceed the amount of `scale_memory_limit`. The units for specifying ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M are the shorthand expressions for GB and MB. For more information see [Units of measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).


  scale_max_execution_time (False, int, 7200)
    The maximum execution time in seconds for runs of the job. This property can only be specified if `run_mode` is `task`.


  image_reference (True, str, None)
    (Required for new resource) The name of the image that is used for this job. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and `TAG` are optional. If `REGISTRY` is not specified, the default is `docker.io`. If `TAG` is not specified, the default is `latest`. If the image reference points to a registry that requires authentication, make sure to also specify the property `image_secret`.


  name (True, str, None)
    (Required for new resource) The name of the job.


  run_commands (False, list, None)
    Set commands for the job that are passed to start job run containers. If not specified an empty string array will be applied and the command specified by the container image, will be used to start the container.


  run_env_variables (False, list, None)
    References to config maps, secrets or literal values, which are exposed as environment variables in the job run.


  run_volume_mounts (False, list, None)
    Optional mounts of config maps or secrets.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

