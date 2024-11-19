
ibm_container_worker_pool -- Configure IBM Cloud 'ibm_container_worker_pool' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_worker_pool' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_worker_pool

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  resource_group_id (False, str, None)
    ID of the resource group.


  orphan_on_delete (False, bool, None)
    Orphan the workerpool resource instead of deleting it


  operating_system (False, str, None)
    The operating system of the workers in the worker pool.


  disk_encryption (False, bool, True)
    worker node disk encrypted if set to true


  import_on_create (False, bool, None)
    Import an existing workerpool from the cluster instead of creating a new


  hardware (False, str, shared)
    Hardware type


  machine_type (True, str, None)
    (Required for new resource) worker nodes machine type


  worker_pool_name (True, str, None)
    (Required for new resource) worker pool name


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  labels (False, dict, None)
    list of labels to worker pool


  taints (False, list, None)
    WorkerPool Taints


  cluster (True, str, None)
    (Required for new resource) Cluster name


  size_per_zone (True, int, None)
    (Required for new resource) Number of nodes per zone


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

