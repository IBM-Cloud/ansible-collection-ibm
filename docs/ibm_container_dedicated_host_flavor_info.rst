
ibm_container_dedicated_host_flavor_info -- Retrieve IBM Cloud 'ibm_container_dedicated_host_flavor' resource
=============================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_dedicated_host_flavor' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/container_dedicated_host_flavor

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  zone (True, str, None)
    The zone of the dedicated host flavor


  host_flavor_id (True, str, None)
    The id of the dedicated host flavor


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

