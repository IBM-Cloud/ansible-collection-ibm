
ibm_container_vpc_worker_pool -- Configure IBM Cloud 'ibm_container_vpc_worker_pool' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_vpc_worker_pool' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_vpc_worker_pool

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.49.0
- Terraform v0.12.20



Parameters
----------

  resource_group_id (False, str, None)
    ID of the resource group.


  host_pool_id (False, str, None)
    The ID of the dedicated host pool associated with the worker pool


  kms_instance_id (False, str, None)
    Instance ID for boot volume encryption


  kms_account_id (False, str, None)
    Account ID of kms instance holder - if not provided, defaults to the account in use


  flavor (True, str, None)
    (Required for new resource) cluster node falvor


  zones (True, list, None)
    (Required for new resource) Zones info


  labels (False, dict, None)
    Labels


  worker_pool_name (True, str, None)
    (Required for new resource) worker pool name


  crk (False, str, None)
    Root Key ID for boot volume encryption


  cluster (True, str, None)
    (Required for new resource) Cluster name


  worker_count (True, int, None)
    (Required for new resource) The number of workers


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  taints (False, list, None)
    WorkerPool Taints


  vpc_id (True, str, None)
    (Required for new resource) The vpc id where the cluster is


  operating_system (False, str, None)
    The operating system of the workers in the worker pool.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

