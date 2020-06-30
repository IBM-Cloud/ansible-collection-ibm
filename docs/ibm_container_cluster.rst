
ibm_container_cluster -- Configure IBM Cloud 'ibm_container_cluster' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_cluster' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  resource_status (False, str, None)
    The status of the resource


  machine_type (False, str, None)
    Machine type


  subnet_id (False, list, None)
    List of subnet IDs


  private_service_endpoint_url (False, str, None)
    None


  gateway_enabled (False, bool, False)
    Set true for gateway enabled clusters


  resource_name (False, str, None)
    The name of the resource


  tags (False, list, None)
    Tags for the resource


  public_service_endpoint_url (False, str, None)
    None


  datacenter (True, str, None)
    (Required for new resource) The datacenter where this cluster will be deployed


  worker_num (False, int, 0)
    Number of worker nodes


  disk_encryption (False, bool, True)
    disc encryption done, if set to true.


  public_vlan_id (False, str, None)
    Public VLAN ID


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  ingress_hostname (False, str, None)
    None


  crn (False, str, None)
    CRN of resource instance


  resource_crn (False, str, None)
    The crn of the resource


  wait_time_minutes (False, int, None)
    None


  public_service_endpoint (False, bool, None)
    None


  default_pool_size (False, int, 1)
    The size of the default worker pool


  workers_info (False, list, None)
    The IDs of the worker node


  private_vlan_id (False, str, None)
    Private VLAN ID


  ingress_secret (False, str, None)
    None


  webhook (False, list, None)
    None


  private_service_endpoint (False, bool, None)
    None


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  billing (False, str, None)
    None


  resource_group_id (False, str, None)
    ID of the resource group.


  name (True, str, None)
    (Required for new resource) The cluster name


  region (False, str, None)
    The cluster region


  hardware (True, str, None)
    (Required for new resource) Hardware type


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  worker_pools (False, list, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  update_all_workers (False, bool, False)
    Updates all the woker nodes if sets to true


  server_url (False, str, None)
    None


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  kube_version (False, str, None)
    Kubernetes version info


  no_subnet (False, bool, False)
    Boolean value set to true when subnet creation is not required.


  is_trusted (False, bool, None)
    None


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  albs (False, list, None)
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

