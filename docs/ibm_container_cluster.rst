
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

- IBM-Cloud terraform-provider-ibm v1.12.0
- Terraform v0.12.20



Parameters
----------

  gateway_enabled (False, bool, False)
    Set true for gateway enabled clusters


  disk_encryption (False, bool, True)
    disc encryption done, if set to true.


  no_subnet (False, bool, False)
    Boolean value set to true when subnet creation is not required.


  public_service_endpoint (False, bool, None)
    None


  name (True, str, None)
    (Required for new resource) The cluster name


  hardware (True, str, None)
    (Required for new resource) Hardware type


  machine_type (False, str, None)
    Machine type


  resource_group_id (False, str, None)
    ID of the resource group.


  tags (False, list, None)
    Tags for the resource


  kms_config (False, list, None)
    Enables KMS on a given cluster


  public_vlan_id (False, str, None)
    Public VLAN ID


  webhook (False, list, None)
    None


  private_service_endpoint (False, bool, None)
    None


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  subnet_id (False, list, None)
    List of subnet IDs


  datacenter (True, str, None)
    (Required for new resource) The datacenter where this cluster will be deployed


  default_pool_size (False, int, 1)
    The size of the default worker pool


  workers_info (False, list, None)
    The IDs of the worker node


  kube_version (False, str, None)
    Kubernetes version info


  private_vlan_id (False, str, None)
    Private VLAN ID


  update_all_workers (False, bool, False)
    Updates all the woker nodes if sets to true


  force_delete_storage (False, bool, False)
    Force the removal of a cluster and its persistent storage. Deleted data cannot be recovered


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

