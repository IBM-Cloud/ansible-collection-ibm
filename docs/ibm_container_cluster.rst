
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

- IBM-Cloud terraform-provider-ibm v1.10.0
- Terraform v0.12.20



Parameters
----------

  public_vlan_id (False, str, None)
    Public VLAN ID


  webhook (False, list, None)
    None


  default_pool_size (False, int, 1)
    The size of the default worker pool


  private_vlan_id (False, str, None)
    Private VLAN ID


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  gateway_enabled (False, bool, False)
    Set true for gateway enabled clusters


  name (True, str, None)
    (Required for new resource) The cluster name


  no_subnet (False, bool, False)
    Boolean value set to true when subnet creation is not required.


  machine_type (False, str, None)
    Machine type


  subnet_id (False, list, None)
    List of subnet IDs


  datacenter (True, str, None)
    (Required for new resource) The datacenter where this cluster will be deployed


  disk_encryption (False, bool, True)
    disc encryption done, if set to true.


  update_all_workers (False, bool, False)
    Updates all the woker nodes if sets to true


  hardware (True, str, None)
    (Required for new resource) Hardware type


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

