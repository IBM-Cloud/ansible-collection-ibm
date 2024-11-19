
ibm_is_lb_listener -- Configure IBM Cloud 'ibm_is_lb_listener' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_lb_listener' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_lb_listener

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  connection_limit (False, int, None)
    Connection limit for Loadbalancer


  port_min (False, int, None)
    The inclusive lower bound of the range of ports used by this listener. Only load balancers in the `network` family support more than one port per listener.


  port_max (False, int, None)
    The inclusive upper bound of the range of ports used by this listener. Only load balancers in the `network` family support more than one port per listener


  protocol (True, str, None)
    (Required for new resource) Loadbalancer protocol


  accept_proxy_protocol (False, bool, None)
    Listener will forward proxy protocol


  default_pool (False, str, None)
    Loadbalancer default pool info


  lb (True, str, None)
    (Required for new resource) Loadbalancer listener ID


  port (False, int, None)
    Loadbalancer listener port


  certificate_instance (False, str, None)
    certificate instance for the Loadbalancer


  https_redirect (False, list, None)
    If present, the target listener that requests are redirected to.


  idle_connection_timeout (False, int, None)
    idle connection timeout of listener


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

