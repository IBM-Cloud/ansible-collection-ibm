
ibm_container_nlb_dns -- Configure IBM Cloud 'ibm_container_nlb_dns' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_nlb_dns' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_nlb_dns

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  nlb_ips (True, list, None)
    (Required for new resource)


  resource_group_id (False, str, None)
    The ID of the resource group that the cluster is in. To check the resource group ID of the cluster, use the GET /v1/clusters/idOrName API. To list available resource group IDs, run ibmcloud resource groups.


  cluster (True, str, None)
    (Required for new resource) The name or ID of the cluster. To list the clusters that you have access to, use the `GET /v1/clusters` API or run `ibmcloud ks cluster ls`.


  nlb_host (True, str, None)
    (Required for new resource)


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

