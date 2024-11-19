
ibm_container_storage_attachment -- Configure IBM Cloud 'ibm_container_storage_attachment' resource
===================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_storage_attachment' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_storage_attachment

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  worker (True, str, None)
    (Required for new resource) worker node ID


  resource_group_id (False, str, None)
    ID of the resource group.


  volume (True, str, None)
    (Required for new resource) VPC Volume ID


  cluster (True, str, None)
    (Required for new resource) Cluster name or ID


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

