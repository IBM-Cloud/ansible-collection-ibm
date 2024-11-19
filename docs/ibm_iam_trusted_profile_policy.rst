
ibm_iam_trusted_profile_policy -- Configure IBM Cloud 'ibm_iam_trusted_profile_policy' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_iam_trusted_profile_policy' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/iam_trusted_profile_policy

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  profile_id (False, str, None)
    UUID of Trusted Profile


  resource_attributes (False, list, None)
    Set resource attributes.


  tags (False, list, None)
    None


  resource_tags (False, list, None)
    Set access management tags.


  transaction_id (False, str, None)
    Set transactionID for debug


  rule_conditions (False, list, None)
    Rule conditions enforced by the policy


  rule_operator (False, str, None)
    Operator that multiple rule conditions are evaluated over


  iam_id (False, str, None)
    IAM ID of Trusted Profile


  roles (True, list, None)
    (Required for new resource) Role names of the policy definition


  resources (False, list, None)
    None


  account_management (False, bool, False)
    Give access to all account management services


  description (False, str, None)
    Description of the Policy


  pattern (False, str, None)
    Pattern rule follows for time-based condition


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

