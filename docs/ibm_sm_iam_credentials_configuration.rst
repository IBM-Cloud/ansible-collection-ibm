
ibm_sm_iam_credentials_configuration -- Configure IBM Cloud 'ibm_sm_iam_credentials_configuration' resource
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_sm_iam_credentials_configuration' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/sm_iam_credentials_configuration

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.51.0
- Terraform v0.12.20



Parameters
----------

  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  name (True, str, None)
    (Required for new resource) A human-readable unique name to assign to your configuration.To protect your privacy, do not use personal data, such as your name or location, as an name for your secret.


  api_key (True, str, None)
    (Required for new resource) The API key that is generated for this secret.After the secret reaches the end of its lease (see the `ttl` field), the API key is deleted automatically. If you want to continue to use the same API key for future read operations, see the `reuse_api_key` field.


  instance_id (True, str, None)
    (Required for new resource) The ID of the Secrets Manager instance.


  endpoint_type (False, str, None)
    public or private.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

