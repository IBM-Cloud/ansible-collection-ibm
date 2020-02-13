
ibm_container_vpc_worker_pool -- Configure IBM Cloud 'ibm_container_vpc_worker_pool' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_vpc_worker_pool' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  labels (False, dict, None)
    None


  resource_group_id (False, str, None)
    ID of the resource group.


  vpc_id (False, str, None)
    (Required for new resource) The vpc id where the cluster is


  worker_count (False, int, None)
    (Required for new resource) The number of workers


  cluster (False, str, None)
    (Required for new resource)


  flavor (False, str, None)
    (Required for new resource)


  worker_pool_name (False, str, None)
    (Required for new resource)


  zones (False, list, None)
    (Required for new resource)


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

