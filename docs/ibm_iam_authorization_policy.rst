
ibm_iam_authorization_policy -- Configure IBM Cloud 'ibm_iam_authorization_policy' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_iam_authorization_policy' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/iam_authorization_policy

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  source_service_name (False, str, None)
    The source service name


  target_service_name (False, str, None)
    The target service name


  source_service_account (False, str, None)
    Account GUID of source service


  subject_attributes (False, list, None)
    Set subject attributes.


  transaction_id (False, str, None)
    Set transactionID for debug


  source_resource_instance_id (False, str, None)
    The source resource instance Id


  source_resource_group_id (False, str, None)
    The source resource group Id


  resource_attributes (False, list, None)
    Set resource attributes.


  description (False, str, None)
    Description of the Policy


  target_resource_group_id (False, str, None)
    The target resource group Id


  roles (True, list, None)
    (Required for new resource) Role names of the policy definition


  target_resource_instance_id (False, str, None)
    The target resource instance Id


  source_resource_type (False, str, None)
    Resource type of source service


  target_resource_type (False, str, None)
    Resource type of target service


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

