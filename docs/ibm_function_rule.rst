
ibm_function_rule -- Configure IBM Cloud 'ibm_function_rule' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_function_rule' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  name (False, str, None)
    (Required for new resource) Name of rule.


  trigger_name (False, str, None)
    (Required for new resource) Name of trigger.


  action_name (False, str, None)
    (Required for new resource) Name of action.


  status (False, str, None)
    Status of the rule.


  publish (False, bool, None)
    Rule visbility.


  version (False, str, None)
    Semantic version of the item.


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

