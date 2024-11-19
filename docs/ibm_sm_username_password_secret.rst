
ibm_sm_username_password_secret -- Configure IBM Cloud 'ibm_sm_username_password_secret' resource
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_sm_username_password_secret' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/sm_username_password_secret

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  secret_group_id (False, str, None)
    A v4 UUID identifier, or `default` secret group.


  instance_id (True, str, None)
    (Required for new resource) The ID of the Secrets Manager instance.


  description (False, str, None)
    An extended description of your secret.To protect your privacy, do not use personal data, such as your name or location, as a description for your secret group.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  expiration_date (False, str, None)
    The date a secret is expired. The date format follows RFC 3339.


  name (True, str, None)
    (Required for new resource) A human-readable name to assign to your secret.To protect your privacy, do not use personal data, such as your name or location, as a name for your secret.


  version_custom_metadata (False, dict, None)
    The secret version metadata that a user can customize.


  username (True, str, None)
    (Required for new resource) The username that is assigned to the secret.


  password_generation_policy (False, list, None)
    Policy for auto-generated passwords.


  labels (False, list, None)
    Labels that you can use to search for secrets in your instance.Up to 30 labels can be created.


  rotation (False, list, None)
    Determines whether Secrets Manager rotates your secrets automatically.


  password (False, str, None)
    The password that is assigned to the secret.


  endpoint_type (False, str, None)
    public or private.


  custom_metadata (False, dict, None)
    The secret metadata that a user can customize.


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

