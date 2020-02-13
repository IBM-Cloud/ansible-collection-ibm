
ibm_function_action_info -- Retrieve IBM Cloud 'ibm_function_action' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_function_action' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  version (False, str, None)
    Semantic version of the item.


  annotations (False, str, None)
    All annotations set on action by user and those set by the IBM Cloud Function backend/API.


  parameters (False, str, None)
    All paramters set on action by user and those set by the IBM Cloud Function backend/API.


  name (True, str, None)
    Name of action.


  limits (False, list, None)
    None


  exec (False, list, None)
    None


  publish (False, bool, None)
    Action visibilty.


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

