
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

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  cos_instance_crn (False, str, None)
    A standard cloud object storage instance CRN to back up the internal registry in your OpenShift on VPC Gen 2 cluster


  master_status (False, str, None)
    None


  name (True, str, None)
    (Required for new resource) The cluster name


  worker_count (False, int, 1)
    Number of worker nodes in the cluster


  tags (False, list, None)
    List of tags for the resources


  master_url (False, str, None)
    None


  private_service_endpoint_url (False, str, None)
    None


  crn (False, str, None)
    CRN of resource instance


  ingress_hostname (False, str, None)
    None


  resource_crn (False, str, None)
    The crn of the resource


  vpc_id (True, str, None)
    (Required for new resource) The vpc id where the cluster is


  kube_version (False, str, None)
    Kubernetes version


  disable_public_service_endpoint (False, bool, False)
    Boolean value true if Public service endpoint to be disabled


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  service_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for services


  resource_status (False, str, None)
    The status of the resource


  pod_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for pods


  resource_group_id (False, str, None)
    ID of the resource group.


  ingress_secret (False, str, None)
    None


  public_service_endpoint_url (False, str, None)
    None


  state_ (False, str, None)
    None


  albs (False, list, None)
    None


  resource_name (False, str, None)
    The name of the resource


  flavor (True, str, None)
    (Required for new resource) Cluster nodes flavour


  zones (True, list, None)
    (Required for new resource) Zone info


  wait_till (False, str, IngressReady)
    wait_till can be configured for Master Ready, One worker Ready or Ingress Ready


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

