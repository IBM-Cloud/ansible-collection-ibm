
ibm_logs_rule_group -- Configure IBM Cloud 'ibm_logs_rule_group' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_logs_rule_group' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/logs_rule_group

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  rule_subgroups (True, list, None)
    (Required for new resource) Rule subgroups. Will try to execute the first rule subgroup, and if not matched will try to match the next one in order.


  endpoint_type (False, str, None)
    public or private.


  name (True, str, None)
    (Required for new resource) The name of the rule group.


  description (False, str, None)
    A description for the rule group, should express what is the rule group purpose.


  enabled (False, bool, None)
    Whether or not the rule is enabled.


  rule_matchers (False, list, None)
    // Optional rule matchers which if matched will make the rule go through the rule group.


  order (False, int, None)
    // The order in which the rule group will be evaluated. The lower the order, the more priority the group will have. Not providing the order will by default create a group with the last order.


  instance_id (True, str, None)
    (Required for new resource) The ID of the logs instance.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

