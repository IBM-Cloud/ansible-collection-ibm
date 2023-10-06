
ibm_function_action_info -- Retrieve IBM Cloud 'ibm_function_action' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_function_action' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/function_action

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.50.0
- Terraform v0.12.20



Parameters
----------

  name (True, str, None)
    Name of action.


  namespace (True, str, None)
    Name of the namespace.


  function_namespace (True, any, None)
    The namespace in IBM Cloud™ Functions where you want to create your resources. This can also be provided via the environment variable 'FUNCTION_NAMESPACE'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

