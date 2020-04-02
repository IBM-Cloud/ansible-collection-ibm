
ibm_lb_vpx_service -- Configure IBM Cloud 'ibm_lb_vpx_service' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lb_vpx_service' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.3.0
- Terraform v0.12.20



Parameters
----------

  name (False, str, None)
    (Required for new resource)


  destination_port (False, int, None)
    (Required for new resource)


  weight (False, int, None)
    (Required for new resource)


  connection_limit (False, int, None)
    (Required for new resource)


  usip (False, str, False)
    None


  vip_id (False, str, None)
    (Required for new resource)


  destination_ip_address (False, str, None)
    (Required for new resource)


  health_check (False, str, None)
    (Required for new resource)


  tags (False, list, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

