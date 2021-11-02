
ibm_enterprise_account -- Configure IBM Cloud 'ibm_enterprise_account' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_enterprise_account' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/enterprise_account

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.35.0
- Terraform v0.12.20



Parameters
----------

  parent (True, str, None)
    (Required for new resource) The CRN of the parent under which the account will be created. The parent can be an existing account group or the enterprise itself.


  name (False, str, None)
    The name of the account. This field must have 3 - 60 characters.


  enterprise_id (False, str, None)
    The enterprise ID that the account is a part of.


  account_id (False, str, None)
    The source account id of account to be imported


  enterprise_account_id (False, str, None)
    The enterprise account ID.


  owner_iam_id (False, str, None)
    The IAM ID of the account owner, such as `IBMid-0123ABC`. The IAM ID must already exist.


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

