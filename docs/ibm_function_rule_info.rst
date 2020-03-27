
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

- IBM-Cloud terraform-provider-ibm v1.2.6
- Terraform v0.12.20



Parameters
----------

  version (False, str, None)
    Semantic version of the rule


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


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

