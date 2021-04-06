
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

- IBM-Cloud terraform-provider-ibm v1.23.0
- Terraform v0.12.20



Parameters
----------

  service_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for services


  subnet_id (False, list, None)
    List of subnet IDs


  force_delete_storage (False, bool, False)
    Force the removal of a cluster and its persistent storage. Deleted data cannot be recovered


  patch_version (False, str, None)
    Kubernetes patch version


  wait_for_worker_update (False, bool, True)
    Wait for worker node to update during kube version update.


  name (True, str, None)
    (Required for new resource) The cluster name


  kms_config (False, list, None)
    Enables KMS on a given cluster


  labels (False, dict, None)
    list of labels to the default worker pool


  hardware (True, str, None)
    (Required for new resource) Hardware type


  wait_till (False, str, IngressReady)
    wait_till can be configured for Master Ready, One worker Ready or Ingress Ready


  pod_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for pods


  private_service_endpoint (False, bool, None)
    None


  datacenter (True, str, None)
    (Required for new resource) The datacenter where this cluster will be deployed


  public_vlan_id (False, str, None)
    Public VLAN ID


  private_vlan_id (False, str, None)
    Private VLAN ID


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  resource_group_id (False, str, None)
    ID of the resource group.


  gateway_enabled (False, bool, False)
    Set true for gateway enabled clusters


  update_all_workers (False, bool, False)
    Updates all the woker nodes if sets to true


  tags (False, list, None)
    Tags for the resource


  machine_type (False, str, None)
    Machine type


  public_service_endpoint (False, bool, None)
    None


  default_pool_size (False, int, 1)
    The size of the default worker pool


  workers_info (False, list, None)
    The IDs of the worker node


  disk_encryption (False, bool, True)
    disc encryption done, if set to true.


  kube_version (False, str, None)
    Kubernetes version info


  no_subnet (False, bool, False)
    Boolean value set to true when subnet creation is not required.


  webhook (False, list, None)
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

