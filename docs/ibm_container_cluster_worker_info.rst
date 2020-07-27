
ibm_container_cluster_worker_info -- Retrieve IBM Cloud 'ibm_container_cluster_worker' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_cluster_worker' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.9.0
- Terraform v0.12.20



Parameters
----------

  worker_id (True, str, None)
    ID of the worker


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  region (False, str, None)
    The cluster region


  resource_group_id (False, str, None)
    ID of the resource group.


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

