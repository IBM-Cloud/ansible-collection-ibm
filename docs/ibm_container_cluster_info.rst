
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

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  workers (False, list, None)
    None


  is_trusted (False, bool, None)
    None


  resource_name (False, str, None)
    The name of the resource


  cluster_name_id (True, str, None)
    Name or id of the cluster


  crn (False, str, None)
    CRN of resource instance


  resource_crn (False, str, None)
    The crn of the resource


  vlans (False, list, None)
    None


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  resource_group_id (False, str, None)
    ID of the resource group.


  bounded_services (False, list, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  ingress_secret (False, str, None)
    None


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  public_service_endpoint_url (False, str, None)
    None


  resource_status (False, str, None)
    The status of the resource


  worker_pools (False, list, None)
    None


  region (False, str, None)
    The cluster region


  server_url (False, str, None)
    None


  albs (False, list, None)
    None


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  private_service_endpoint (False, bool, None)
    None


  private_service_endpoint_url (False, str, None)
    None


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  worker_count (False, int, None)
    Number of workers


  alb_type (False, str, all)
    None


  public_service_endpoint (False, bool, None)
    None


  ingress_hostname (False, str, None)
    None


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

