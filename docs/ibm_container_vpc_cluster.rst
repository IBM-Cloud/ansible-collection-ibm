
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

- IBM-Cloud terraform-provider-ibm v1.7.1
- Terraform v0.12.20



Parameters
----------

  disable_public_service_endpoint (False, bool, False)
    Boolean value true if Public service endpoint to be disabled


  public_service_endpoint_url (False, str, None)
    None


  name (False, str, None)
    (Required for new resource) The cluster name


  master_url (False, str, None)
    None


  private_service_endpoint_url (False, str, None)
    None


  resource_name (False, str, None)
    The name of the resource


  vpc_id (False, str, None)
    (Required for new resource) The vpc id where the cluster is


  kube_version (False, str, None)
    Kubernetes version


  ingress_secret (False, str, None)
    None


  resource_status (False, str, None)
    The status of the resource


  resource_group_id (False, str, None)
    ID of the resource group.


  resource_crn (False, str, None)
    The crn of the resource


  worker_count (False, int, 1)
    Number of worker nodes in the cluster


  wait_till (False, str, IngressReady)
    wait_till can be configured for Master Ready, One worker Ready or Ingress Ready


  crn (False, str, None)
    CRN of resource instance


  pod_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for pods


  state_ (False, str, None)
    None


  service_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for services


  tags (False, list, None)
    List of tags for the resources


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  flavor (False, str, None)
    (Required for new resource) Cluster nodes flavour


  zones (False, list, None)
    (Required for new resource) Zone info


  albs (False, list, None)
    None


  ingress_hostname (False, str, None)
    None


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  master_status (False, str, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

