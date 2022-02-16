
ibm_appid_idp_cloud_directory -- Configure IBM Cloud 'ibm_appid_idp_cloud_directory' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_appid_idp_cloud_directory' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/appid_idp_cloud_directory

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.38.2
- Terraform v0.12.20



Parameters
----------

  signup_enabled (False, bool, True)
    None


  welcome_enabled (False, bool, True)
    None


  reset_password_enabled (False, bool, True)
    None


  reset_password_notification_enabled (False, bool, True)
    None


  identity_confirm_access_mode (False, str, FULL)
    None


  identity_confirm_methods (False, list, None)
    None


  tenant_id (True, str, None)
    (Required for new resource)


  is_active (True, bool, None)
    (Required for new resource)


  self_service_enabled (False, bool, True)
    None


  identity_field (False, str, None)
    None


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

