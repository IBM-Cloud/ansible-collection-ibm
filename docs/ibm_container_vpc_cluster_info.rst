
ibm_container_vpc_cluster_info -- Retrieve IBM Cloud 'ibm_container_vpc_cluster' resource
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_vpc_cluster' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.3.0
- Terraform v0.12.20



Parameters
----------

  private_service_endpoint (False, bool, None)
    None


  resource_status (False, str, None)
    The status of the resource


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  cluster_name_id (True, str, None)
    Name of the cluster


  public_service_endpoint (False, bool, None)
    None


  crn (False, str, None)
    CRN of resource instance


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  worker_pools (False, list, None)
    None


  alb_type (False, str, all)
    None


  ingress_hostname (False, str, None)
    None


  ingress_secret (False, str, None)
    None


  resource_group_id (False, str, None)
    ID of the resource group.


  private_service_endpoint_url (False, str, None)
    None


  status (False, str, None)
    The status of the cluster master


  kube_version (False, str, None)
    None


  worker_count (False, int, None)
    Number of workers


  albs (False, list, None)
    None


  resource_crn (False, str, None)
    The crn of the resource


  master_url (False, str, None)
    None


  health (False, str, None)
    None


  tags (False, list, None)
    None


  resource_name (False, str, None)
    The name of the resource


  workers (False, list, None)
    None


  public_service_endpoint_url (False, str, None)
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

