
ibm_cloud_shell_account_settings -- Configure IBM Cloud 'ibm_cloud_shell_account_settings' resource
===================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cloud_shell_account_settings' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cloud_shell_account_settings

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  default_enable_new_regions (False, bool, None)
    Set whether Cloud Shell is enabled in a specific location for the account. The location determines where user and session data are stored. By default, users are routed to the nearest available location.


  features (False, list, None)
    List of Cloud Shell features.


  account_id (True, str, None)
    (Required for new resource) The account ID in which the account settings belong to.


  rev (False, str, None)
    Unique revision number for the settings object.


  regions (False, list, None)
    List of Cloud Shell region settings.


  default_enable_new_features (False, bool, None)
    You can choose which Cloud Shell features are available in the account and whether any new features are enabled as they become available. The feature settings apply only to the enabled Cloud Shell locations.


  enabled (False, bool, None)
    When enabled, Cloud Shell is available to all users in the account.


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

