
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

- IBM-Cloud terraform-provider-ibm v1.3.0
- Terraform v0.12.20



Parameters
----------

  flavor (False, str, None)
    (Required for new resource)


  pod_subnet (False, str, 172.30.0.0/16)
    Custom subnet CIDR to provide private IP addresses for pods


  master_url (False, str, None)
    None


  crn (False, str, None)
    CRN of resource instance


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  master_status (False, str, None)
    None


  resource_group_id (False, str, None)
    ID of the resource group.


  albs (False, list, None)
    None


  vpc_id (False, str, None)
    (Required for new resource) The vpc id where the cluster is


  kube_version (False, str, None)
    None


  tags (False, list, None)
    None


  wait_till (False, str, IngressReady)
    wait_till can be configured for Master Ready, One worker Ready or Ingress Ready


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  public_service_endpoint_url (False, str, None)
    None


  ingress_secret (False, str, None)
    None


  resource_name (False, str, None)
    The name of the resource


  resource_status (False, str, None)
    The status of the resource


  disable_public_service_endpoint (False, bool, False)
    None


  state_ (False, str, None)
    None


  private_service_endpoint_url (False, str, None)
    None


  resource_crn (False, str, None)
    The crn of the resource


  name (False, str, None)
    (Required for new resource) The cluster name


  zones (False, list, None)
    (Required for new resource)


  service_subnet (False, str, 172.21.0.0/16)
    Custom subnet CIDR to provide private IP addresses for services


  worker_count (False, int, 1)
    None


  ingress_hostname (False, str, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

