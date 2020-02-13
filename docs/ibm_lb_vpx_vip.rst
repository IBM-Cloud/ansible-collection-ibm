
ibm_lb_vpx_vip -- Configure IBM Cloud 'ibm_lb_vpx_vip' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lb_vpx_vip' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  load_balancing_method (False, str, None)
    (Required for new resource)


  source_port (False, int, None)
    (Required for new resource)


  type (False, str, None)
    (Required for new resource)


  security_certificate_id (False, int, None)
    None


  nad_controller_id (False, int, None)
    (Required for new resource)


  name (False, str, None)
    (Required for new resource)


  virtual_ip_address (False, str, None)
    (Required for new resource)


  tags (False, list, None)
    None


  persistence (False, str, None)
    None


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

