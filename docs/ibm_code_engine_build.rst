
ibm_code_engine_build -- Configure IBM Cloud 'ibm_code_engine_build' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_code_engine_build' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/code_engine_build

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  output_secret (True, str, None)
    (Required for new resource) The secret that is required to access the image registry. Make sure that the secret is granted with push permissions towards the specified container registry namespace.


  source_secret (False, str, None)
    Name of the secret that is used access the repository source. This field is optional if the `source_type` is `git`. Additionally, if the `source_url` points to a repository that requires authentication, the build will be created but cannot access any source code, until this property is provided, too. If the `source_type` value is `local`, this field must be omitted.


  source_url (False, str, None)
    The URL of the code repository. This field is required if the `source_type` is `git`. If the `source_type` value is `local`, this field must be omitted. If the repository is publicly available you can provide a 'https' URL like `https://github.com/IBM/CodeEngine`. If the repository requires authentication, you need to provide a 'ssh' URL like `git@github.com:IBM/CodeEngine.git` along with a `source_secret` that points to a secret of format `ssh_auth`.


  name (True, str, None)
    (Required for new resource) The name of the build.


  source_type (False, str, git)
    Specifies the type of source to determine if your build source is in a repository or based on local source code.* local - For builds from local source code.* git - For builds from git version controlled source code.


  strategy_spec_file (False, str, Dockerfile)
    Optional path to the specification file that is used for build strategies for building an image.


  project_id (True, str, None)
    (Required for new resource) The ID of the project.


  source_context_dir (False, str, None)
    Optional directory in the repository that contains the buildpacks file or the Dockerfile.


  source_revision (False, str, None)
    Commit, tag, or branch in the source repository to pull. This field is optional if the `source_type` is `git` and uses the HEAD of default branch if not specified. If the `source_type` value is `local`, this field must be omitted.


  strategy_size (False, str, medium)
    Optional size for the build, which determines the amount of resources used. Build sizes are `small`, `medium`, `large`, `xlarge`, `xxlarge`.


  strategy_type (True, str, None)
    (Required for new resource) The strategy to use for building the image.


  timeout (False, int, 600)
    The maximum amount of time, in seconds, that can pass before the build must succeed or fail.


  output_image (True, str, None)
    (Required for new resource) The name of the image.


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

