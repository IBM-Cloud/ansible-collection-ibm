
ibm_is_instance_group_manager_policy -- Configure IBM Cloud 'ibm_is_instance_group_manager_policy' resource
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_instance_group_manager_policy' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance_group_manager_policy

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.46.0
- Terraform v0.12.20



Parameters
----------

  name (False, str, None)
    instance group manager policy name


  instance_group (True, str, None)
    (Required for new resource) instance group ID


  instance_group_manager (True, str, None)
    (Required for new resource) Instance group manager ID


  metric_type (True, str, None)
    (Required for new resource) The type of metric to be evaluated


  metric_value (True, int, None)
    (Required for new resource) The metric value to be evaluated


  policy_type (True, str, None)
    (Required for new resource) The type of Policy for the Instance Group


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

