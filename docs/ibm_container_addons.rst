
ibm_container_addons -- Configure IBM Cloud 'ibm_container_addons' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_addons' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_addons

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.35.0
- Terraform v0.12.20



Parameters
----------

  addons (True, list, None)
    (Required for new resource)


  cluster (True, str, None)
    (Required for new resource) Cluster Name or ID


  resource_group_id (False, str, None)
    ID of the resource group.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

