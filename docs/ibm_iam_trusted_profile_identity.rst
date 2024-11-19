
ibm_iam_trusted_profile_identity -- Configure IBM Cloud 'ibm_iam_trusted_profile_identity' resource
===================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_iam_trusted_profile_identity' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/iam_trusted_profile_identity

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  profile_id (True, str, None)
    (Required for new resource) ID of the trusted profile.


  identity_type (True, str, None)
    (Required for new resource) Type of the identity.


  identifier (True, str, None)
    (Required for new resource) Identifier of the identity that can assume the trusted profiles. This can be a user identifier (IAM id), serviceid or crn. Internally it uses account id of the service id for the identifier 'serviceid' and for the identifier 'crn' it uses account id contained in the CRN.


  type (True, str, None)
    (Required for new resource) Type of the identity.


  accounts (False, list, None)
    Only valid for the type user. Accounts from which a user can assume the trusted profile.


  description (False, str, None)
    Description of the identity that can assume the trusted profile. This is optional field for all the types of identities. When this field is not set for the identity type 'serviceid' then the description of the service id is used. Description is recommended for the identity type 'crn' E.g. 'Instance 1234 of IBM Cloud Service project'.


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

