
ibm_appid_cloud_directory_user -- Configure IBM Cloud 'ibm_appid_cloud_directory_user' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_appid_cloud_directory_user' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/appid_cloud_directory_user

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  create_profile (False, bool, True)
    A boolean indication if a profile should be created for the Cloud Directory user


  tenant_id (True, str, None)
    (Required for new resource) The AppID instance GUID


  active (False, bool, True)
    Determines if the user account is active or not


  display_name (False, str, None)
    Cloud Directory user display name


  user_name (False, str, None)
    Optional username


  password (True, str, None)
    (Required for new resource) User password


  status (False, str, PENDING)
    Accepted values `PENDING` or `CONFIRMED`


  email (True, list, None)
    (Required for new resource) A set of user emails


  locked_until (False, int, None)
    Integer (epoch time in milliseconds), determines till when the user account will be locked


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

