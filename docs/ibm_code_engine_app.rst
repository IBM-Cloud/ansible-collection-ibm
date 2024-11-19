
ibm_code_engine_app -- Configure IBM Cloud 'ibm_code_engine_app' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_code_engine_app' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/code_engine_app

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  image_port (False, int, 8080)
    Optional port the app listens on. While the app will always be exposed via port `443` for end users, this port is used to connect to the port that is exposed by the container image.


  scale_request_timeout (False, int, 300)
    Optional amount of time in seconds that is allowed for a running app to respond to a request.


  image_reference (True, str, None)
    (Required for new resource) The name of the image that is used for this app. The format is `REGISTRY/NAMESPACE/REPOSITORY:TAG` where `REGISTRY` and `TAG` are optional. If `REGISTRY` is not specified, the default is `docker.io`. If `TAG` is not specified, the default is `latest`. If the image reference points to a registry that requires authentication, make sure to also specify the property `image_secret`.


  run_as_user (False, int, 0)
    Optional user ID (UID) to run the app.


  run_volume_mounts (False, list, None)
    Mounts of config maps or secrets.


  scale_max_instances (False, int, 10)
    Optional maximum number of instances for this app. If you set this value to `0`, this property does not set a upper scaling limit. However, the app scaling is still limited by the project quota for instances. See [Limits and quotas for Code Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-limits).


  probe_liveness (False, list, None)
    Response model for probes.


  run_env_variables (False, list, None)
    References to config maps, secrets or literal values, which are exposed as environment variables in the application.


  managed_domain_mappings (False, str, local_public)
    Optional value controlling which of the system managed domain mappings will be setup for the application. Valid values are 'local_public', 'local_private' and 'local'. Visibility can only be 'local_private' if the project supports application private visibility.


  probe_readiness (False, list, None)
    Response model for probes.


  run_arguments (False, list, None)
    Optional arguments for the app that are passed to start the container. If not specified an empty string array will be applied and the arguments specified by the container image, will be used to start the container.


  run_commands (False, list, None)
    Optional commands for the app that are passed to start the container. If not specified an empty string array will be applied and the command specified by the container image, will be used to start the container.


  scale_concurrency_target (False, int, None)
    Optional threshold of concurrent requests per instance at which one or more additional instances are created. Use this value to scale up instances based on concurrent number of requests. This option defaults to the value of the `scale_concurrency` option, if not specified.


  project_id (True, str, None)
    (Required for new resource) The ID of the project.


  image_secret (False, str, None)
    Optional name of the image registry access secret. The image registry access secret is used to authenticate with a private registry when you download the container image. If the image reference points to a registry that requires authentication, the app will be created but cannot reach the ready status, until this property is provided, too.


  scale_concurrency (False, int, 100)
    Optional maximum number of requests that can be processed concurrently per instance.


  scale_down_delay (False, int, 0)
    Optional amount of time in seconds that delays the scale-down behavior for an app instance.


  name (True, str, None)
    (Required for new resource) The name of the app.


  run_service_account (False, str, default)
    Optional name of the service account. For built-in service accounts, you can use the shortened names `manager` , `none`, `reader`, and `writer`.


  scale_cpu_limit (False, str, 1)
    Optional number of CPU set for the instance of the app. For valid values see [Supported memory and CPU combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).


  scale_ephemeral_storage_limit (False, str, 400M)
    Optional amount of ephemeral storage to set for the instance of the app. The amount specified as ephemeral storage, must not exceed the amount of `scale_memory_limit`. The units for specifying ephemeral storage are Megabyte (M) or Gigabyte (G), whereas G and M are the shorthand expressions for GB and MB. For more information see [Units of measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).


  scale_initial_instances (False, int, 1)
    Optional initial number of instances that are created upon app creation or app update.


  scale_memory_limit (False, str, 4G)
    Optional amount of memory set for the instance of the app. For valid values see [Supported memory and CPU combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo). The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and M are the shorthand expressions for GB and MB. For more information see [Units of measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).


  scale_min_instances (False, int, 0)
    Optional minimum number of instances for this app. If you set this value to `0`, the app will scale down to zero, if not hit by any request for some time.


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

