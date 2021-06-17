
ibm_container_worker_pool_zone_attachment -- Configure IBM Cloud 'ibm_container_worker_pool_zone_attachment' resource
=====================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_worker_pool_zone_attachment' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_worker_pool_zone_attachment

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.26.2
- Terraform v0.12.20



Parameters
----------

  worker_pool (True, str, None)
    (Required for new resource) Workerpool name


  resource_group_id (False, str, None)
    ID of the resource group.


  wait_till_albs (False, bool, True)
    wait_till_albs can be configured to wait for albs during the worker pool zone attachment.


  cluster (True, str, None)
    (Required for new resource) cluster name or ID


  private_vlan_id (False, str, None)
    None


  public_vlan_id (False, str, None)
    None


  zone (True, str, None)
    (Required for new resource) Zone name


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

