
ibm_container_dedicated_host -- Configure IBM Cloud 'ibm_container_dedicated_host' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_dedicated_host' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_dedicated_host

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  flavor (True, str, None)
    (Required for new resource) The flavor of the dedicated host


  host_pool_id (True, str, None)
    (Required for new resource) The id of the dedicated host pool the dedicated host is associated with


  zone (True, str, None)
    (Required for new resource) The zone of the dedicated host


  placement_enabled (False, bool, None)
    Enables/disables placement on the dedicated host


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

