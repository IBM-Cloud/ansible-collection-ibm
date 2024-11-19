
ibm_appid_token_config -- Configure IBM Cloud 'ibm_appid_token_config' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_appid_token_config' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/appid_token_config

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  access_token_expires_in (False, int, None)
    The length of time for which access tokens are valid in seconds


  refresh_token_expires_in (False, int, 2592000)
    The length of time for which refresh tokens are valid in seconds


  anonymous_token_expires_in (False, int, 2592000)
    None


  anonymous_access_enabled (False, bool, None)
    The length of time for which an anonymous token is valid in seconds


  refresh_token_enabled (False, bool, None)
    None


  access_token_claim (False, list, None)
    A set of objects that are created when claims that are related to access tokens are mapped


  id_token_claim (False, list, None)
    A set of objects that are created when claims that are related to identity tokens are mapped


  tenant_id (True, str, None)
    (Required for new resource) The service `tenantId`


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

