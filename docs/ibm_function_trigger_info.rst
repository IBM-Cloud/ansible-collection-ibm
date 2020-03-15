
ibm_function_trigger_info -- Retrieve IBM Cloud 'ibm_function_trigger' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_function_trigger' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.4
- Terraform v0.12.20



Parameters
----------

  name (True, str, None)
    Name of Trigger.


  publish (False, bool, None)
    Trigger Visibility.


  version (False, str, None)
    Semantic version of the trigger.


  annotations (False, str, None)
    All annotations set on trigger by user and those set by the IBM Cloud Function backend/API.


  parameters (False, str, None)
    All parameters set on trigger by user and those set by the IBM Cloud Function backend/API.


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

