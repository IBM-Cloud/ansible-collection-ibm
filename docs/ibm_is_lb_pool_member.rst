
ibm_is_lb_pool_member -- Configure IBM Cloud 'ibm_is_lb_pool_member' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_lb_pool_member' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_lb_pool_member

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.50.0
- Terraform v0.12.20



Parameters
----------

  pool (True, str, None)
    (Required for new resource) Loadblancer Poold ID


  lb (True, str, None)
    (Required for new resource) Load balancer ID


  port (True, int, None)
    (Required for new resource) Load Balancer Pool port


  target_address (False, str, None)
    Load balancer pool member target address


  weight (False, int, None)
    Load balcner pool member weight


  target_id (False, str, None)
    Load balancer pool member target id


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

