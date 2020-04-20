
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

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster


  cluster (False, str, None)
    (Required for new resource) NA


  size_per_zone (False, int, None)
    (Required for new resource) NA


  hardware (False, str, shared)
    NA


  resource_group_id (False, str, None)
    ID of the resource group.


  zones (False, list, None)
    NA


  labels (False, dict, None)
    NA


  region (False, str, None)
    The worker pool region


  machine_type (False, str, None)
    (Required for new resource) NA


  worker_pool_name (False, str, None)
    (Required for new resource) NA


  disk_encryption (False, bool, True)
    NA


  state_ (False, str, None)
    NA


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

