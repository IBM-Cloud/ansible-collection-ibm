
ibm_is_lb_listener_policy_rule -- Configure IBM Cloud 'ibm_is_lb_listener_policy_rule' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_lb_listener_policy_rule' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.3
- Terraform v0.12.20



Parameters
----------

  listener (False, str, None)
    (Required for new resource) Listener ID.


  policy (False, str, None)
    (Required for new resource) Listener Policy ID


  condition (False, str, None)
    (Required for new resource) Condition info of the rule.


  type (False, str, None)
    (Required for new resource) Policy rule type.


  rule (False, str, None)
    None


  provisioning_status (False, str, None)
    None


  lb (False, str, None)
    (Required for new resource) Loadbalancer ID


  field (False, str, None)
    None


  value (False, str, None)
    (Required for new resource) policy rule value info


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

