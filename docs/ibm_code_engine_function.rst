
ibm_code_engine_function -- Configure IBM Cloud 'ibm_code_engine_function' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_code_engine_function' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/code_engine_function

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  name (True, str, None)
    (Required for new resource) The name of the function.


  scale_memory_limit (False, str, 4G)
    Optional amount of memory set for the instance of the function. For valid values see [Supported memory and CPU combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo). The units for specifying memory are Megabyte (M) or Gigabyte (G), whereas G and M are the shorthand expressions for GB and MB. For more information see [Units of measurement](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo#unit-measurements).


  code_reference (True, str, None)
    (Required for new resource) Specifies either a reference to a code bundle or the source code itself. To specify the source code, use the data URL scheme and include the source code as base64 encoded. The data URL scheme is defined in [RFC 2397](https://tools.ietf.org/html/rfc2397).


  managed_domain_mappings (False, str, local_public)
    Optional value controlling which of the system managed domain mappings will be setup for the function. Valid values are 'local_public', 'local_private' and 'local'. Visibility can only be 'local_private' if the project supports function private visibility.


  scale_concurrency (False, int, 1)
    Number of parallel requests handled by a single instance, supported only by Node.js, default is `1`.


  scale_max_execution_time (False, int, 60)
    Timeout in secs after which the function is terminated.


  code_secret (False, str, None)
    The name of the secret that is used to access the specified `code_reference`. The secret is used to authenticate with a non-public endpoint that is specified as`code_reference`.


  runtime (True, str, None)
    (Required for new resource) The managed runtime used to execute the injected code.


  scale_down_delay (False, int, 1)
    Optional amount of time in seconds that delays the scale down behavior for a function.


  scale_cpu_limit (False, str, 1)
    Optional amount of CPU set for the instance of the function. For valid values see [Supported memory and CPU combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo).


  project_id (True, str, None)
    (Required for new resource) The ID of the project.


  code_binary (False, bool, None)
    Specifies whether the code is binary or not. Defaults to false when `code_reference` is set to a data URL. When `code_reference` is set to a code bundle URL, this field is always true.


  code_main (False, str, main)
    Specifies the name of the function that should be invoked.


  run_env_variables (False, list, None)
    References to config maps, secrets or literal values, which are defined by the function owner and are exposed as environment variables in the function.


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

