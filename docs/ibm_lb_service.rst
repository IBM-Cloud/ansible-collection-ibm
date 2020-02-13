
ibm_lb_service -- Configure IBM Cloud 'ibm_lb_service' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lb_service' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  tags (False, list, None)
    None


  service_group_id (False, int, None)
    (Required for new resource)


  ip_address_id (False, int, None)
    (Required for new resource)


  port (False, int, None)
    (Required for new resource)


  enabled (False, bool, None)
    (Required for new resource)


  health_check_type (False, str, None)
    (Required for new resource)


  weight (False, int, None)
    (Required for new resource)


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

