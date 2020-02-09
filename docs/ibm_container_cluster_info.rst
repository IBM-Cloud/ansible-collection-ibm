
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

- IBM-Cloud terraform-provider-ibm v1.2.0
- Terraform v0.12.20



Parameters
----------

  worker_pools (False, list, None)
    None


  bounded_services (False, list, None)
    None


  vlans (False, list, None)
    None


  alb_type (False, str, all)
    None


  albs (False, list, None)
    None


  cluster_name_id (True, str, None)
    Name or id of the cluster


  worker_count (False, int, None)
    Number of workers


  workers (False, list, None)
    None


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  crn (False, str, None)
    CRN of resource instance


  is_trusted (False, bool, None)
    None


  region (False, str, None)
    The cluster region


  private_service_endpoint (False, bool, None)
    None


  server_url (False, str, None)
    None


  resource_crn (False, str, None)
    The crn of the resource


  resource_status (False, str, None)
    The status of the resource


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  public_service_endpoint (False, bool, None)
    None


  public_service_endpoint_url (False, str, None)
    None


  resource_group_id (False, str, None)
    ID of the resource group.


  private_service_endpoint_url (False, str, None)
    None


  resource_name (False, str, None)
    The name of the resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

