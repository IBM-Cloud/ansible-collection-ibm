
ibm_is_lb_listener_policy -- Configure IBM Cloud 'ibm_is_lb_listener_policy' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_lb_listener_policy' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.23.0
- Terraform v0.12.20



Parameters
----------

  lb (True, str, None)
    (Required for new resource) Load Balancer Listener Policy


  priority (True, int, None)
    (Required for new resource) Listener Policy Priority


  target_id (False, str, None)
    Listener Policy Target ID


  target_http_status_code (False, int, None)
    Listener Policy target HTTPS Status code.


  target_url (False, str, None)
    Policy Target URL


  listener (True, str, None)
    (Required for new resource) Listener ID


  action (True, str, None)
    (Required for new resource) Policy Action


  name (False, str, None)
    Policy name


  rules (False, list, None)
    Policy Rules


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

