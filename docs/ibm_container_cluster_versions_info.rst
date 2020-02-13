
ibm_container_cluster_versions_info -- Retrieve IBM Cloud 'ibm_container_cluster_versions' resource
===================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_cluster_versions' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  region (False, str, None)
    The cluster region


  resource_group_id (False, str, None)
    ID of the resource group.


  valid_kube_versions (False, list, None)
    List supported kube-versions


  valid_openshift_versions (False, list, None)
    List of supported openshift-versions


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

