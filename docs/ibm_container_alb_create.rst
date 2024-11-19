
ibm_container_alb_create -- Configure IBM Cloud 'ibm_container_alb_create' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_alb_create' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_alb_create

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  enable (False, bool, True)
    If set to true, the ALB is enabled by default.


  nlb_version (False, str, None)
    The version of the network load balancer that you want to use for the ALB.


  cluster (True, str, None)
    (Required for new resource) The ID of the cluster that the ALB belongs to.


  alb_type (True, str, None)
    (Required for new resource) The type of ALB that you want to create.


  ingress_image (False, str, None)
    The type of Ingress image that you want to use for your ALB deployment.


  vlan_id (True, str, None)
    (Required for new resource) The VLAN ID that you want to use for your ALBs.


  ip (False, str, None)
    The IP address that you want to assign to the ALB.


  zone (True, str, None)
    (Required for new resource) The zone where you want to deploy the ALB.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

