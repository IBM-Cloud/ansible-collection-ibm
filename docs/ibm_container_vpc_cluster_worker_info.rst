
ibm_container_vpc_cluster_worker_info -- Retrieve IBM Cloud 'ibm_container_vpc_cluster_worker' resource
=======================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_vpc_cluster_worker' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.19.0
- Terraform v0.12.20



Parameters
----------

  cluster_name_id (True, str, None)
    Name or ID of the cluster


  resource_group_id (False, str, None)
    ID of the resource group.


  worker_id (True, str, None)
    ID of the worker


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

