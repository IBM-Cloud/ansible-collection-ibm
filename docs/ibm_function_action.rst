
ibm_function_action -- Configure IBM Cloud 'ibm_function_action' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_function_action' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.2
- Terraform v0.12.20



Parameters
----------

  name (False, str, None)
    (Required for new resource) Name of action.


  exec (False, list, None)
    (Required for new resource) Execution info


  limits (False, list, None)
    None


  publish (False, bool, None)
    Action visibilty.


  version (False, str, None)
    Semantic version of the item.


  user_defined_annotations (False, str, [])
    Annotation values in KEY VALUE format.


  user_defined_parameters (False, str, [])
    Parameters values in KEY VALUE format. Parameter bindings included in the context passed to the action.


  annotations (False, str, None)
    All annotations set on action by user and those set by the IBM Cloud Function backend/API.


  parameters (False, str, None)
    All paramters set on action by user and those set by the IBM Cloud Function backend/API.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  function_namespace (True, any, None)
    The namespace in IBM Cloud™ Functions where you want to create your resources. This can also be provided via the environment variable 'FUNCTION_NAMESPACE'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

