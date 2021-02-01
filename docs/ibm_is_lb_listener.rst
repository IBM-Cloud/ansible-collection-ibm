
ibm_is_lb_listener -- Configure IBM Cloud 'ibm_is_lb_listener' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_lb_listener' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.19.0
- Terraform v0.12.20



Parameters
----------

  lb (True, str, None)
    (Required for new resource) Loadbalancer listener ID


  certificate_instance (False, str, None)
    certificate instance for the Loadbalancer


  default_pool (False, str, None)
    Loadbalancer default pool info


  port (True, int, None)
    (Required for new resource) Loadbalancer listener port


  protocol (True, str, None)
    (Required for new resource) Loadbalancer protocol


  connection_limit (False, int, None)
    Connection limit for Loadbalancer


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

