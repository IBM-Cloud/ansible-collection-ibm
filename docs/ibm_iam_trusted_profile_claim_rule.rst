
ibm_iam_trusted_profile_claim_rule -- Configure IBM Cloud 'ibm_iam_trusted_profile_claim_rule' resource
=======================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_iam_trusted_profile_claim_rule' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/iam_trusted_profile_claim_rule

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  cr_type (False, str, None)
    The compute resource type the rule applies to, required only if type is specified as 'Profile-CR'. Valid values are VSI, IKS_SA, ROKS_SA.


  expiration (False, int, None)
    Session expiration in seconds, only required if type is 'Profile-SAML'.


  name (False, str, None)
    Name of the claim rule to be created or updated.


  type (True, str, None)
    (Required for new resource) Type of the calim rule, either 'Profile-SAML' or 'Profile-CR'.


  conditions (True, list, None)
    (Required for new resource) Conditions of this claim rule.


  realm_name (False, str, None)
    The realm name of the Idp this claim rule applies to. This field is required only if the type is specified as 'Profile-SAML'.


  profile_id (True, str, None)
    (Required for new resource) ID of the trusted profile to create a claim rule.


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

