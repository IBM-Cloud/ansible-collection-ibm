
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

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  ingress_secret (False, str, None)
    NA


  no_subnet (False, bool, False)
    NA


  webhook (False, list, None)
    NA


  public_service_endpoint_url (False, str, None)
    NA


  resource_crn (False, str, None)
    The crn of the resource


  ingress_hostname (False, str, None)
    NA


  datacenter (False, str, None)
    (Required for new resource) The datacenter where this cluster will be deployed


  albs (False, list, None)
    NA


  public_service_endpoint (False, bool, None)
    NA


  gateway_enabled (False, bool, False)
    Set true for gateway enabled clusters


  crn (False, str, None)
    CRN of resource instance


  resource_status (False, str, None)
    The status of the resource


  name (False, str, None)
    (Required for new resource) The cluster name


  private_vlan_id (False, str, None)
    NA


  wait_time_minutes (False, int, 90)
    NA


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  kube_version (False, str, None)
    NA


  subnet_id (False, list, None)
    NA


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  hardware (False, str, None)
    (Required for new resource) NA


  workers_info (False, list, None)
    The IDs of the worker node


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  private_service_endpoint (False, bool, None)
    NA


  is_trusted (False, bool, None)
    NA


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  worker_num (False, int, 0)
    Number of worker nodes


  machine_type (False, str, None)
    NA


  billing (False, str, None)
    NA


  public_vlan_id (False, str, None)
    NA


  server_url (False, str, None)
    NA


  tags (False, list, None)
    NA


  disk_encryption (False, bool, True)
    NA


  default_pool_size (False, int, 1)
    The size of the default worker pool


  update_all_workers (False, bool, False)
    NA


  resource_group_id (False, str, None)
    ID of the resource group.


  worker_pools (False, list, None)
    NA


  private_service_endpoint_url (False, str, None)
    NA


  resource_name (False, str, None)
    The name of the resource


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  region (False, str, None)
    The cluster region


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

