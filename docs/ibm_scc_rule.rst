
ibm_scc_rule -- Configure IBM Cloud 'ibm_scc_rule' resource
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_scc_rule' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/scc_rule

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.51.0
- Terraform v0.12.20



Parameters
----------

  account_id (True, str, None)
    (Required for new resource) Your IBM Cloud account ID.


  name (True, str, None)
    (Required for new resource) A human-readable alias to assign to your rule.


  enforcement_actions (False, list, None)
    The actions that the service must run on your behalf when a request to create or modify the target resource does not comply with your conditions.


  required_config (True, list, None)
    (Required for new resource) The requirements that must be met to determine the resource's level of compliance in accordance with the rule. Use logical operators (and/or) to define multiple property checks and conditions. To define requirements for a rule, list one or more property check objects in the and array. To add conditions to a property check, use or.


  description (True, str, None)
    (Required for new resource) An extended description of your rule.


  labels (False, list, None)
    Labels that you can use to group and search for similar rules, such as those that help you to meet a specific organization guideline.


  target (True, list, None)
    (Required for new resource) The properties that describe the resource that you want to targetwith the rule or template.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

