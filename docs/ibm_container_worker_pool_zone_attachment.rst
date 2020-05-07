
ibm_container_worker_pool_zone_attachment -- Configure IBM Cloud 'ibm_container_worker_pool_zone_attachment' resource
=====================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_worker_pool_zone_attachment' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.2
- Terraform v0.12.20



Parameters
----------

  worker_pool (False, str, None)
    (Required for new resource) Workerpool name


  private_vlan_id (False, str, None)
    None


  public_vlan_id (False, str, None)
    None


  resource_group_id (False, str, None)
    ID of the resource group.


  region (False, str, None)
    The zone region


  worker_count (False, int, None)
    None


  zone (False, str, None)
    (Required for new resource) Zone name


  cluster (False, str, None)
    (Required for new resource) cluster name or ID


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

