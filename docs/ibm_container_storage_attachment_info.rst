
ibm_container_storage_attachment_info -- Retrieve IBM Cloud 'ibm_container_storage_attachment' resource
=======================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_storage_attachment' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/container_storage_attachment

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  volume_attachment_id (True, str, None)
    The volume attachment ID


  cluster (True, str, None)
    Cluster name or ID


  worker (True, str, None)
    Worker node ID


  resource_group_id (False, str, None)
    ID of the resource group.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

