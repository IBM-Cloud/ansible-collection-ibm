
ibm_function_trigger -- Configure IBM Cloud 'ibm_function_trigger' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_function_trigger' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  user_defined_parameters (False, str, [])
    Parameters values in KEY VALUE format. Parameter bindings included in the context passed to the trigger.


  annotations (False, str, None)
    All annotations set on trigger by user and those set by the IBM Cloud Function backend/API.


  parameters (False, str, None)
    All parameters set on trigger by user and those set by the IBM Cloud Function backend/API.


  name (False, str, None)
    (Required for new resource) Name of Trigger.


  feed (False, list, None)
    Trigger feed


  publish (False, bool, None)
    Trigger visbility.


  version (False, str, None)
    Semantic version of the item.


  user_defined_annotations (False, str, [])
    Annotation values in KEY VALUE format.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

