
ibm_container_dedicated_host_info -- Retrieve IBM Cloud 'ibm_container_dedicated_host' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_dedicated_host' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/container_dedicated_host

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.48.0
- Terraform v0.12.20



Parameters
----------

  host_pool_id (True, str, None)
    The id of the dedicated host pool the dedicated host is associated with


  host_id (True, str, None)
    The id of the dedicated host


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

