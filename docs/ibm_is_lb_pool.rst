
ibm_is_lb_pool -- Configure IBM Cloud 'ibm_is_lb_pool' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_lb_pool' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.23.2
- Terraform v0.12.20



Parameters
----------

  name (True, str, None)
    (Required for new resource) Load Balancer Pool name


  algorithm (True, str, None)
    (Required for new resource) Load Balancer Pool algorithm


  health_type (True, str, None)
    (Required for new resource) Load Balancer health type


  health_monitor_port (False, int, None)
    Health monitor Port the LB Pool


  protocol (True, str, None)
    (Required for new resource) Load Balancer Protocol


  session_persistence_type (False, str, None)
    Load Balancer Pool session persisence type.


  proxy_protocol (False, str, None)
    PROXY protocol setting for this pool


  lb (True, str, None)
    (Required for new resource) Load Balancer ID


  health_retries (True, int, None)
    (Required for new resource) Load Balancer health retry count


  health_delay (True, int, None)
    (Required for new resource) Load Blancer health delay time period


  health_timeout (True, int, None)
    (Required for new resource) Load Balancer health timeout interval


  health_monitor_url (False, str, None)
    Health monitor URL of LB Pool


  session_persistence_cookie_name (False, str, None)
    Load Balancer Pool session persisence cookie name


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

