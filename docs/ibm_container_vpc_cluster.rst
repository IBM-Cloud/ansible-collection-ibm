
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

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  flavor (False, str, None)
    (Required for new resource) NA


  service_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for services


  master_url (False, str, None)
    NA


  public_service_endpoint_url (False, str, None)
    NA


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  ingress_secret (False, str, None)
    NA


  resource_name (False, str, None)
    The name of the resource


  vpc_id (False, str, None)
    (Required for new resource) The vpc id where the cluster is


  kube_version (False, str, None)
    NA


  worker_count (False, int, 1)
    NA


  disable_public_service_endpoint (False, bool, False)
    NA


  ingress_hostname (False, str, None)
    NA


  resource_group_id (False, str, None)
    ID of the resource group.


  resource_crn (False, str, None)
    The crn of the resource


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  state_ (False, str, None)
    NA


  master_status (False, str, None)
    NA


  name (False, str, None)
    (Required for new resource) The cluster name


  zones (False, list, None)
    (Required for new resource) NA


  pod_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for pods


  tags (False, list, None)
    NA


  wait_till (False, str, IngressReady)
    wait_till can be configured for Master Ready, One worker Ready or Ingress Ready


  albs (False, list, None)
    NA


  private_service_endpoint_url (False, str, None)
    NA


  crn (False, str, None)
    CRN of resource instance


  resource_status (False, str, None)
    The status of the resource


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

