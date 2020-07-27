
ibm_container_cluster -- Configure IBM Cloud 'ibm_container_cluster' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_cluster' resource

This module supports idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.9.0
- Terraform v0.12.20



Parameters
----------

  disk_encryption (False, bool, True)
    disc encryption done, if set to true.


  no_subnet (False, bool, False)
    Boolean value set to true when subnet creation is not required.


  is_trusted (False, bool, None)
    None


  subnet_id (False, list, None)
    List of subnet IDs


  worker_num (False, int, 0)
    Number of worker nodes


  machine_type (False, str, None)
    Machine type


  hardware (True, str, None)
    (Required for new resource) Hardware type


  webhook (False, list, None)
    None


  private_vlan_id (False, str, None)
    Private VLAN ID


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  update_all_workers (False, bool, False)
    Updates all the woker nodes if sets to true


  billing (False, str, None)
    None


  name (True, str, None)
    (Required for new resource) The cluster name


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  wait_time_minutes (False, int, None)
    None


  datacenter (True, str, None)
    (Required for new resource) The datacenter where this cluster will be deployed


  default_pool_size (False, int, 1)
    The size of the default worker pool


  public_vlan_id (False, str, None)
    Public VLAN ID


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


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

