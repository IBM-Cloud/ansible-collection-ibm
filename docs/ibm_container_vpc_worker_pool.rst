
ibm_container_vpc_worker_pool -- Configure IBM Cloud 'ibm_container_vpc_worker_pool' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_vpc_worker_pool' resource

This module supports idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.21.1
- Terraform v0.12.20



Parameters
----------

  vpc_id (True, str, None)
    (Required for new resource) The vpc id where the cluster is


  cluster (True, str, None)
    (Required for new resource) Cluster name


  worker_pool_name (True, str, None)
    (Required for new resource) worker pool name


  labels (False, dict, None)
    Labels


  resource_group_id (False, str, None)
    ID of the resource group.


  worker_count (True, int, None)
    (Required for new resource) The number of workers


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  flavor (True, str, None)
    (Required for new resource) cluster node falvor


  zones (True, list, None)
    (Required for new resource) Zones info


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

