
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

- IBM-Cloud terraform-provider-ibm v1.5.0
- Terraform v0.12.20



Parameters
----------

  health_monitor_port (False, int, None)
    None


  provisioning_status (False, str, None)
    None


  name (False, str, None)
    (Required for new resource) Load Balancer Pool name


  algorithm (False, str, None)
    (Required for new resource) Load Balancer Pool algorithm


  health_delay (False, int, None)
    (Required for new resource) Load Blancer health delay time period


  health_timeout (False, int, None)
    (Required for new resource) Load Balancer health timeout interval


  health_type (False, str, None)
    (Required for new resource) Load Balancer health type


  session_persistence_cookie_name (False, str, None)
    Load Balancer Pool session persisence cookie name


  lb (False, str, None)
    (Required for new resource) Load Balancer ID


  protocol (False, str, None)
    (Required for new resource) Load Balancer Protocol


  health_retries (False, int, None)
    (Required for new resource) Load Balancer health retry count


  health_monitor_url (False, str, None)
    None


  session_persistence_type (False, str, None)
    Load Balancer Pool session persisence type.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, any, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

