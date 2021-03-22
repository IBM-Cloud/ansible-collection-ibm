
ibm_container_cluster_info -- Retrieve IBM Cloud 'ibm_container_cluster' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_cluster' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.21.2
- Terraform v0.12.20



Parameters
----------

  resource_group_id (False, str, None)
    ID of the resource group.


  list_bounded_services (False, bool, True)
    If set to false bounded services won't be listed.


  name (False, str, None)
    Name or id of the cluster


  alb_type (False, str, all)
    None


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

