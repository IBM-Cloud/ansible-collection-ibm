
ibm_function_rule_info -- Retrieve IBM Cloud 'ibm_function_rule' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_function_rule' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.2
- Terraform v0.12.20



Parameters
----------

  name (True, str, None)
    Name of the rule.


  trigger_name (False, str, None)
    Name of the trigger.


  action_name (False, str, None)
    Name of an action.


  status (False, str, None)
    Status of the rule.


  publish (False, bool, None)
    Rule Visibility.


  version (False, str, None)
    Semantic version of the rule


  function_namespace (True, any, None)
    The namespace in IBM Cloud™ Functions where you want to create your resources. This can also be provided via the environment variable 'FUNCTION_NAMESPACE'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

