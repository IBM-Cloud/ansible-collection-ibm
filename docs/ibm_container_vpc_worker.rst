
ibm_container_vpc_worker -- Configure IBM Cloud 'ibm_container_vpc_worker' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_vpc_worker' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_vpc_worker

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.49.0
- Terraform v0.12.20



Parameters
----------

  replace_worker (True, str, None)
    (Required for new resource) Worker name/id that needs to be replaced


  resource_group_id (False, str, None)
    ID of the resource group.


  kube_config_path (False, str, None)
    Path of downloaded cluster config


  check_ptx_status (False, bool, False)
    Check portworx status after worker replace


  ptx_timeout (False, str, 15m)
    Timeout for checking ptx pods/status


  cluster_name (True, str, None)
    (Required for new resource) Cluster name


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

