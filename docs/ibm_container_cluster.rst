
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

- IBM-Cloud terraform-provider-ibm v1.19.0
- Terraform v0.12.20



Parameters
----------

  private_vlan_id (False, str, None)
    Private VLAN ID


  force_delete_storage (False, bool, False)
    Force the removal of a cluster and its persistent storage. Deleted data cannot be recovered


  labels (False, dict, None)
    list of labels to the default worker pool


  private_service_endpoint (False, bool, None)
    None


  name (True, str, None)
    (Required for new resource) The cluster name


  public_vlan_id (False, str, None)
    Public VLAN ID


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  webhook (False, list, None)
    None


  tags (False, list, None)
    Tags for the resource


  kms_config (False, list, None)
    Enables KMS on a given cluster


  workers_info (False, list, None)
    The IDs of the worker node


  hardware (True, str, None)
    (Required for new resource) Hardware type


  machine_type (False, str, None)
    Machine type


  gateway_enabled (False, bool, False)
    Set true for gateway enabled clusters


  update_all_workers (False, bool, False)
    Updates all the woker nodes if sets to true


  no_subnet (False, bool, False)
    Boolean value set to true when subnet creation is not required.


  subnet_id (False, list, None)
    List of subnet IDs


  resource_group_id (False, str, None)
    ID of the resource group.


  datacenter (True, str, None)
    (Required for new resource) The datacenter where this cluster will be deployed


  wait_for_worker_update (False, bool, True)
    Wait for worker node to update during kube version update.


  public_service_endpoint (False, bool, None)
    None


  default_pool_size (False, int, 1)
    The size of the default worker pool


  disk_encryption (False, bool, True)
    disc encryption done, if set to true.


  kube_version (False, str, None)
    Kubernetes version info


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

