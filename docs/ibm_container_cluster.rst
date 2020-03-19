
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

- IBM-Cloud terraform-provider-ibm v1.2.5
- Terraform v0.12.20



Parameters
----------

  kube_version (False, str, None)
    None


  ingress_secret (False, str, None)
    None


  ingress_hostname (False, str, None)
    None


  public_service_endpoint (False, bool, None)
    None


  private_service_endpoint (False, bool, None)
    None


  resource_crn (False, str, None)
    The crn of the resource


  name (False, str, None)
    (Required for new resource) The cluster name


  region (False, str, None)
    The cluster region


  disk_encryption (False, bool, True)
    None


  subnet_id (False, list, None)
    None


  public_vlan_id (False, str, None)
    None


  wait_time_minutes (False, int, 90)
    None


  public_service_endpoint_url (False, str, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  resource_status (False, str, None)
    The status of the resource


  datacenter (False, str, None)
    (Required for new resource) The datacenter where this cluster will be deployed


  default_pool_size (False, int, 1)
    The size of the default worker pool


  private_vlan_id (False, str, None)
    None


  no_subnet (False, bool, False)
    None


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  albs (False, list, None)
    None


  private_service_endpoint_url (False, str, None)
    None


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  workers_info (False, list, None)
    The IDs of the worker node


  machine_type (False, str, None)
    None


  billing (False, str, None)
    None


  is_trusted (False, bool, None)
    None


  tags (False, list, None)
    None


  worker_pools (False, list, None)
    None


  worker_num (False, int, 0)
    Number of worker nodes


  update_all_workers (False, bool, False)
    None


  server_url (False, str, None)
    None


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  gateway_enabled (False, bool, False)
    Set true for gateway enabled clusters


  crn (False, str, None)
    CRN of resource instance


  resource_name (False, str, None)
    The name of the resource


  hardware (False, str, None)
    (Required for new resource)


  webhook (False, list, None)
    None


  resource_group_id (False, str, None)
    ID of the resource group.


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


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

