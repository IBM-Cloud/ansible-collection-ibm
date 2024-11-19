
ibm_function_rule -- Configure IBM Cloud 'ibm_function_rule' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_function_rule' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/function_rule

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  namespace (True, str, None)
    (Required for new resource) IBM Cloud function namespace.


  name (True, str, None)
    (Required for new resource) Name of rule.


  trigger_name (True, str, None)
    (Required for new resource) Name of trigger.


  action_name (True, str, None)
    (Required for new resource) Name of action.


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

