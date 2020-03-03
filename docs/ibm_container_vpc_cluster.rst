
ibm_container_vpc_cluster -- Configure IBM Cloud 'ibm_container_vpc_cluster' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_vpc_cluster' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.3
- Terraform v0.12.20



Parameters
----------

  disable_public_service_endpoint (False, bool, False)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  state_ (False, str, None)
    None


  resource_crn (False, str, None)
    The crn of the resource


  name (False, str, None)
    (Required for new resource) The cluster name


  vpc_id (False, str, None)
    (Required for new resource) The vpc id where the cluster is


  service_subnet (False, str, 172.21.0.0/16)
    Custom subnet CIDR to provide private IP addresses for services


  pod_subnet (False, str, 172.30.0.0/16)
    Custom subnet CIDR to provide private IP addresses for pods


  worker_count (False, int, 1)
    None


  albs (False, list, None)
    None


  resource_status (False, str, None)
    The status of the resource


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  zones (False, list, None)
    (Required for new resource)


  kube_version (False, str, None)
    None


  private_service_endpoint_url (False, str, None)
    None


  crn (False, str, None)
    CRN of resource instance


  master_url (False, str, None)
    None


  public_service_endpoint_url (False, str, None)
    None


  resource_name (False, str, None)
    The name of the resource


  flavor (False, str, None)
    (Required for new resource)


  tags (False, list, None)
    None


  master_status (False, str, None)
    None


  resource_group_id (False, str, None)
    ID of the resource group.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

