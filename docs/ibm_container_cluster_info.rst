
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

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  private_service_endpoint (False, bool, None)
    NA


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  is_trusted (False, bool, None)
    NA


  vlans (False, list, None)
    NA


  albs (False, list, None)
    NA


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  worker_pools (False, list, None)
    NA


  ingress_secret (False, str, None)
    NA


  resource_crn (False, str, None)
    The crn of the resource


  bounded_services (False, list, None)
    NA


  crn (False, str, None)
    CRN of resource instance


  server_url (False, str, None)
    NA


  workers (False, list, None)
    NA


  alb_type (False, str, all)
    NA


  resource_group_id (False, str, None)
    ID of the resource group.


  cluster_name_id (True, str, None)
    Name or id of the cluster


  resource_name (False, str, None)
    The name of the resource


  resource_status (False, str, None)
    The status of the resource


  ingress_hostname (False, str, None)
    NA


  public_service_endpoint (False, bool, None)
    NA


  private_service_endpoint_url (False, str, None)
    NA


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  worker_count (False, int, None)
    Number of workers


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  region (False, str, None)
    The cluster region


  public_service_endpoint_url (False, str, None)
    NA


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

