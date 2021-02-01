
ibm_iam_authorization_policy -- Configure IBM Cloud 'ibm_iam_authorization_policy' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_iam_authorization_policy' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.19.0
- Terraform v0.12.20



Parameters
----------

  target_resource_type (False, str, None)
    Resource type of target service


  source_service_name (True, str, None)
    (Required for new resource) The source service name


  roles (True, list, None)
    (Required for new resource) Role names of the policy definition


  source_resource_instance_id (False, str, None)
    The source resource instance Id


  source_resource_group_id (False, str, None)
    The source resource group Id


  source_service_account (False, str, None)
    Account GUID of source service


  target_service_name (True, str, None)
    (Required for new resource) The target service name


  target_resource_instance_id (False, str, None)
    The target resource instance Id


  target_resource_group_id (False, str, None)
    The target resource group Id


  source_resource_type (False, str, None)
    Resource type of source service


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

