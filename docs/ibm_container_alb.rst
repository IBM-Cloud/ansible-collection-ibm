
ibm_container_alb -- Configure IBM Cloud 'ibm_container_alb' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_alb' resource

This module supports idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.21.2
- Terraform v0.12.20



Parameters
----------

  user_ip (False, str, None)
    IP assigned by the user


  enable (False, bool, None)
    set to true if ALB needs to be enabled


  alb_id (True, str, None)
    (Required for new resource) ALB ID


  disable_deployment (False, bool, None)
    Set to true if ALB needs to be disabled


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

