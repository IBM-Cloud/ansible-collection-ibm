
ibm_is_lb_pool -- Configure IBM Cloud 'ibm_is_lb_pool' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_lb_pool' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  health_delay (False, int, None)
    (Required for new resource)


  health_retries (False, int, None)
    (Required for new resource)


  health_timeout (False, int, None)
    (Required for new resource)


  health_type (False, str, None)
    (Required for new resource)


  session_persistence_type (False, str, None)
    None


  protocol (False, str, None)
    (Required for new resource)


  lb (False, str, None)
    (Required for new resource)


  algorithm (False, str, None)
    (Required for new resource)


  health_monitor_url (False, str, None)
    None


  health_monitor_port (False, int, None)
    None


  session_persistence_cookie_name (False, str, None)
    None


  provisioning_status (False, str, None)
    None


  name (False, str, None)
    (Required for new resource)


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, any, 2)
    IBM Cloud infrastructure generation.


  ibmcloud_api_key (False, any, None)
    (Required when generation = 2) The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environmental variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environmental variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

