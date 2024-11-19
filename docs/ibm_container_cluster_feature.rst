
ibm_container_cluster_feature -- Configure IBM Cloud 'ibm_container_cluster_feature' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_cluster_feature' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_cluster_feature

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  private_service_endpoint (False, bool, None)
    None


  refresh_api_servers (False, bool, True)
    Boolean value true of API server to be refreshed in K8S cluster


  reload_workers (False, bool, True)
    Boolean value set true if worker nodes to be reloaded


  resource_group_id (False, str, None)
    ID of the resource group.


  cluster (True, str, None)
    (Required for new resource) Cluster name of ID


  public_service_endpoint (False, bool, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

