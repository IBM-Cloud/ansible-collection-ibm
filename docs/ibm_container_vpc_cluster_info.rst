
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

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  crn (False, str, None)
    CRN of resource instance


  status (False, str, None)
    The status of the cluster master


  worker_count (False, int, None)
    Number of workers


  workers (False, list, None)
    NA


  private_service_endpoint (False, bool, None)
    NA


  private_service_endpoint_url (False, str, None)
    NA


  kube_version (False, str, None)
    NA


  resource_crn (False, str, None)
    The crn of the resource


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  ingress_hostname (False, str, None)
    NA


  resource_group_id (False, str, None)
    ID of the resource group.


  albs (False, list, None)
    NA


  ingress_secret (False, str, None)
    NA


  public_service_endpoint_url (False, str, None)
    NA


  health (False, str, None)
    NA


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  resource_status (False, str, None)
    The status of the resource


  cluster_name_id (True, str, None)
    Name of the cluster


  worker_pools (False, list, None)
    NA


  master_url (False, str, None)
    NA


  tags (False, list, None)
    NA


  resource_name (False, str, None)
    The name of the resource


  alb_type (False, str, all)
    NA


  public_service_endpoint (False, bool, None)
    NA


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

