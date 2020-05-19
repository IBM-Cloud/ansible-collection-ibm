
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

- IBM-Cloud terraform-provider-ibm v1.5.3
- Terraform v0.12.20



Parameters
----------

  albs (False, list, None)
    None


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  private_service_endpoint_url (False, str, None)
    None


  is_trusted (False, bool, None)
    None


  worker_pools (False, list, None)
    None


  ingress_secret (False, str, None)
    None


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  cluster_name_id (True, str, None)
    Name or id of the cluster


  bounded_services (False, list, None)
    None


  vlans (False, list, None)
    None


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  region (False, str, None)
    The cluster region


  server_url (False, str, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  resource_crn (False, str, None)
    The crn of the resource


  resource_status (False, str, None)
    The status of the resource


  private_service_endpoint (False, bool, None)
    None


  worker_count (False, int, None)
    Number of workers


  workers (False, list, None)
    None


  alb_type (False, str, all)
    None


  public_service_endpoint_url (False, str, None)
    None


  crn (False, str, None)
    CRN of resource instance


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  ingress_hostname (False, str, None)
    None


  resource_group_id (False, str, None)
    ID of the resource group.


  resource_name (False, str, None)
    The name of the resource


  public_service_endpoint (False, bool, None)
    None


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

