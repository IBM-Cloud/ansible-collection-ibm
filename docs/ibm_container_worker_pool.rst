
ibm_container_worker_pool -- Configure IBM Cloud 'ibm_container_worker_pool' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_worker_pool' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  resource_group_id (False, str, None)
    ID of the resource group.


  cluster (False, str, None)
    (Required for new resource)


  machine_type (False, str, None)
    (Required for new resource)


  hardware (False, str, shared)
    None


  state_ (False, str, None)
    None


  zones (False, list, None)
    None


  region (False, str, None)
    The worker pool region


  worker_pool_name (False, str, None)
    (Required for new resource)


  size_per_zone (False, int, None)
    (Required for new resource)


  disk_encryption (False, bool, True)
    None


  labels (False, dict, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


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

