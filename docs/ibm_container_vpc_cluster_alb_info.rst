
ibm_container_vpc_cluster_alb_info -- Retrieve IBM Cloud 'ibm_container_vpc_cluster_alb' resource
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_vpc_cluster_alb' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/container_vpc_cluster_alb

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.47.1
- Terraform v0.12.20



Parameters
----------

  alb_id (True, str, None)
    ALB ID


  resource_group_id (False, str, None)
    ID of the resource group.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

