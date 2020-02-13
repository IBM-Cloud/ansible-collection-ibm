
ibm_container_vpc_alb -- Configure IBM Cloud 'ibm_container_vpc_alb' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_vpc_alb' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  enable (False, bool, None)
    None


  disable_deployment (False, bool, None)
    None


  load_balancer_hostname (False, str, None)
    None


  status (False, str, None)
    None


  zone (False, str, None)
    None


  alb_id (False, str, None)
    (Required for new resource)


  alb_type (False, str, None)
    None


  cluster (False, str, None)
    None


  name (False, str, None)
    None


  resize (False, bool, None)
    None


  state_ (False, str, None)
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

