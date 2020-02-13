
ibm_iam_auth_token_info -- Retrieve IBM Cloud 'ibm_iam_auth_token' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_iam_auth_token' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  iam_access_token (False, str, None)
    None


  iam_refresh_token (False, str, None)
    None


  uaa_access_token (False, str, None)
    None


  uaa_refresh_token (False, str, None)
    None


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

