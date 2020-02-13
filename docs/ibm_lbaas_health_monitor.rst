
ibm_lbaas_health_monitor -- Configure IBM Cloud 'ibm_lbaas_health_monitor' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lbaas_health_monitor' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  max_retries (False, int, 2)
    None


  timeout (False, int, 2)
    None


  url_path (False, str, /)
    None


  monitor_id (False, str, None)
    (Required for new resource)


  lbaas_id (False, str, None)
    (Required for new resource)


  protocol (False, str, None)
    (Required for new resource)


  port (False, int, None)
    (Required for new resource)


  interval (False, int, 5)
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

