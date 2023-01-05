
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

- IBM-Cloud terraform-provider-ibm v1.47.1
- Terraform v0.12.20



Parameters
----------

  tags (False, list, None)
    None


  resource_tags (False, list, None)
    Set access management tags.


  description (False, str, None)
    Description of the Policy


  profile_id (False, str, None)
    UUID of Trusted Profile


  roles (True, list, None)
    (Required for new resource) Role names of the policy definition


  resource_attributes (False, list, None)
    Set resource attributes.


  transaction_id (False, str, None)
    Set transactionID for debug


  iam_id (False, str, None)
    IAM ID of Trusted Profile


  resources (False, list, None)
    None


  account_management (False, bool, False)
    Give access to all account management services


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

