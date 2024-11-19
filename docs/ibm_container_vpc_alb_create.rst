
ibm_container_vpc_alb_create -- Configure IBM Cloud 'ibm_container_vpc_alb_create' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_vpc_alb_create' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_vpc_alb_create

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  resource_group_id (False, str, None)
    ID of the resource group.


  type (True, str, None)
    (Required for new resource) The type of ALB that you want to create.


  zone (True, str, None)
    (Required for new resource) The zone where you want to deploy the ALB.


  cluster (True, str, None)
    (Required for new resource) The ID of the cluster that the ALB belongs to.


  enable (False, bool, None)
    Enable the ALB instance in the cluster


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

