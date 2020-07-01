
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

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  zone (False, str, None)
    Zone info.


  alb_type (False, str, None)
    Type of the ALB


  status (False, str, None)
    Status of the ALB


  enable (False, bool, None)
    Enable the ALB instance in the cluster


  disable_deployment (False, bool, None)
    Disable the ALB instance in the cluster


  name (False, str, None)
    ALB name


  load_balancer_hostname (False, str, None)
    Load balancer host name


  resize (False, bool, None)
    boolean value to resize the albs


  state_ (False, str, None)
    ALB state


  alb_id (True, str, None)
    (Required for new resource) ALB ID


  cluster (False, str, None)
    cluster id


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

