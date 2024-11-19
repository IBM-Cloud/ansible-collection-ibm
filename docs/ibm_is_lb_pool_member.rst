
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

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  lb (True, str, None)
    (Required for new resource) Load balancer ID


  target_id (False, str, None)
    Load balancer pool member target id


  weight (False, int, None)
    Load balcner pool member weight


  pool (True, str, None)
    (Required for new resource) Loadblancer Poold ID


  port (True, int, None)
    (Required for new resource) Load Balancer Pool port


  target_address (False, str, None)
    Load balancer pool member target address


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

