
ibm_container_cluster -- Configure IBM Cloud 'ibm_container_cluster' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_cluster' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_cluster

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.33.1
- Terraform v0.12.20



Parameters
----------

  resource_group_id (False, str, None)
    ID of the resource group.


  private_service_endpoint (False, bool, None)
    None


  labels (False, dict, None)
    list of labels to the default worker pool


  disk_encryption (False, bool, True)
    disc encryption done, if set to true.


  wait_for_worker_update (False, bool, True)
    Wait for worker node to update during kube version update.


  name (True, str, None)
    (Required for new resource) The cluster name


  taints (False, list, None)
    WorkerPool Taints


  kube_version (False, str, None)
    Kubernetes version info


  patch_version (False, str, None)
    Kubernetes patch version


  kms_config (False, list, None)
    Enables KMS on a given cluster


  machine_type (False, str, None)
    Machine type


  service_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for services


  webhook (False, list, None)
    None


  workers_info (False, list, None)
    The IDs of the worker node


  retry_patch_version (False, int, None)
    Argument which helps to retry the patch version updates on worker nodes. Increment the value to retry the patch updates if the previous apply fails


  update_all_workers (False, bool, False)
    Updates all the woker nodes if sets to true


  hardware (True, str, None)
    (Required for new resource) Hardware type


  wait_till (False, str, IngressReady)
    wait_till can be configured for Master Ready, One worker Ready or Ingress Ready


  no_subnet (False, bool, False)
    Boolean value set to true when subnet creation is not required.


  subnet_id (False, list, None)
    List of subnet IDs


  public_service_endpoint (False, bool, None)
    None


  gateway_enabled (False, bool, False)
    Set true for gateway enabled clusters


  default_pool_size (False, int, 1)
    The size of the default worker pool


  public_vlan_id (False, str, None)
    Public VLAN ID


  private_vlan_id (False, str, None)
    Private VLAN ID


  force_delete_storage (False, bool, False)
    Force the removal of a cluster and its persistent storage. Deleted data cannot be recovered


  datacenter (True, str, None)
    (Required for new resource) The datacenter where this cluster will be deployed


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  pod_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for pods


  tags (False, list, None)
    Tags for the resource


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

