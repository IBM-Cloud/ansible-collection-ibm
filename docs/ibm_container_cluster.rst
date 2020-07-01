
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

  workers_info (False, list, None)
    The IDs of the worker node


  update_all_workers (False, bool, False)
    Updates all the woker nodes if sets to true


  public_vlan_id (False, str, None)
    Public VLAN ID


  worker_pools (False, list, None)
    None


  private_service_endpoint (False, bool, None)
    None


  resource_crn (False, str, None)
    The crn of the resource


  datacenter (True, str, None)
    (Required for new resource) The datacenter where this cluster will be deployed


  webhook (False, list, None)
    None


  resource_name (False, str, None)
    The name of the resource


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  disk_encryption (False, bool, True)
    disc encryption done, if set to true.


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  resource_status (False, str, None)
    The status of the resource


  region (False, str, None)
    The cluster region


  worker_num (False, int, 0)
    Number of worker nodes


  machine_type (False, str, None)
    Machine type


  private_vlan_id (False, str, None)
    Private VLAN ID


  subnet_id (False, list, None)
    List of subnet IDs


  resource_group_id (False, str, None)
    ID of the resource group.


  name (True, str, None)
    (Required for new resource) The cluster name


  kube_version (False, str, None)
    Kubernetes version info


  is_trusted (False, bool, None)
    None


  server_url (False, str, None)
    None


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  tags (False, list, None)
    Tags for the resource


  albs (False, list, None)
    None


  default_pool_size (False, int, 1)
    The size of the default worker pool


  hardware (True, str, None)
    (Required for new resource) Hardware type


  ingress_hostname (False, str, None)
    None


  no_subnet (False, bool, False)
    Boolean value set to true when subnet creation is not required.


  ingress_secret (False, str, None)
    None


  public_service_endpoint_url (False, str, None)
    None


  crn (False, str, None)
    CRN of resource instance


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  billing (False, str, None)
    None


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  wait_time_minutes (False, int, None)
    None


  public_service_endpoint (False, bool, None)
    None


  private_service_endpoint_url (False, str, None)
    None


  gateway_enabled (False, bool, False)
    Set true for gateway enabled clusters


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

