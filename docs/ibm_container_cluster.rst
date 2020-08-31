
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

- IBM-Cloud terraform-provider-ibm v1.11.0
- Terraform v0.12.20



Parameters
----------

  datacenter (True, str, None)
    (Required for new resource) The datacenter where this cluster will be deployed


  kube_version (False, str, None)
    Kubernetes version info


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  machine_type (False, str, None)
    Machine type


  subnet_id (False, list, None)
    List of subnet IDs


  webhook (False, list, None)
    None


  public_service_endpoint (False, bool, None)
    None


  gateway_enabled (False, bool, False)
    Set true for gateway enabled clusters


  hardware (True, str, None)
    (Required for new resource) Hardware type


  tags (False, list, None)
    Tags for the resource


  default_pool_size (False, int, 1)
    The size of the default worker pool


  no_subnet (False, bool, False)
    Boolean value set to true when subnet creation is not required.


  resource_group_id (False, str, None)
    ID of the resource group.


  disk_encryption (False, bool, True)
    disc encryption done, if set to true.


  private_vlan_id (False, str, None)
    Private VLAN ID


  private_service_endpoint (False, bool, None)
    None


  name (True, str, None)
    (Required for new resource) The cluster name


  workers_info (False, list, None)
    The IDs of the worker node


  update_all_workers (False, bool, False)
    Updates all the woker nodes if sets to true


  public_vlan_id (False, str, None)
    Public VLAN ID


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

