
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

- IBM-Cloud terraform-provider-ibm v1.3.0
- Terraform v0.12.20



Parameters
----------

  server_url (False, str, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  workers (False, list, None)
    None


  vlans (False, list, None)
    None


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  resource_group_id (False, str, None)
    ID of the resource group.


  alb_type (False, str, all)
    None


  ingress_secret (False, str, None)
    None


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  private_service_endpoint (False, bool, None)
    None


  resource_status (False, str, None)
    The status of the resource


  cluster_name_id (True, str, None)
    Name or id of the cluster


  bounded_services (False, list, None)
    None


  crn (False, str, None)
    CRN of resource instance


  resource_name (False, str, None)
    The name of the resource


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  is_trusted (False, bool, None)
    None


  region (False, str, None)
    The cluster region


  public_service_endpoint_url (False, str, None)
    None


  resource_crn (False, str, None)
    The crn of the resource


  worker_count (False, int, None)
    Number of workers


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  private_service_endpoint_url (False, str, None)
    None


  ingress_hostname (False, str, None)
    None


  worker_pools (False, list, None)
    None


  albs (False, list, None)
    None


  public_service_endpoint (False, bool, None)
    None


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

