
ibm_sm_iam_credentials_secret -- Configure IBM Cloud 'ibm_sm_iam_credentials_secret' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_sm_iam_credentials_secret' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/sm_iam_credentials_secret

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  service_id (False, str, None)
    The service ID under which the API key (see the `api_key` field) is created.If you omit this parameter, Secrets Manager generates a new service ID for your secret at its creation and adds it to the access groups that you assign.Optionally, you can use this field to provide your own service ID if you prefer to manage its access directly or retain the service ID after your secret expires, is rotated, or deleted. If you provide a service ID, do not include the `access_groups` parameter.


  secret_group_id (False, str, None)
    A v4 UUID identifier, or `default` secret group.


  version_custom_metadata (False, dict, None)
    The secret version metadata that a user can customize.


  name (True, str, None)
    (Required for new resource) A human-readable name to assign to your secret.To protect your privacy, do not use personal data, such as your name or location, as a name for your secret.


  account_id (False, str, None)
    The ID of the account in which the IAM credentials are created. Use this field only if the target account is not the same as the account of the Secrets Manager instance. Otherwise, the field can be omitted.


  reuse_api_key (False, bool, True)
    Determines whether to use the same service ID and API key for future read operations on an`iam_credentials` secret. Must be set to `true` for IAM credentials secrets managed with Terraform.


  rotation (False, list, None)
    Determines whether Secrets Manager rotates your secrets automatically.


  custom_metadata (False, dict, None)
    The secret metadata that a user can customize.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  description (False, str, None)
    An extended description of your secret.To protect your privacy, do not use personal data, such as your name or location, as a description for your secret group.


  labels (False, list, None)
    Labels that you can use to search for secrets in your instance.Up to 30 labels can be created.


  ttl (True, str, None)
    (Required for new resource) The time-to-live (TTL) or lease duration to assign to generated credentials.For `iam_credentials` secrets, the TTL defines for how long each generated API key remains valid. The value is an integer that specifies the number of seconds .Minimum duration is 1 minute. Maximum is 90 days.


  access_groups (False, list, None)
    Access Groups that you can use for an `iam_credentials` secret.Up to 10 Access Groups can be used for each secret.


  endpoint_type (False, str, None)
    public or private.


  instance_id (True, str, None)
    (Required for new resource) The ID of the Secrets Manager instance.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

