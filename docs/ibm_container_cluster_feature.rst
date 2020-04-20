
ibm_container_cluster_feature -- Configure IBM Cloud 'ibm_container_cluster_feature' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_cluster_feature' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  public_service_endpoint_url (False, str, None)
    NA


  private_service_endpoint_url (False, str, None)
    NA


  refresh_api_servers (False, bool, True)
    NA


  reload_workers (False, bool, True)
    NA


  resource_group_id (False, str, None)
    ID of the resource group.


  cluster (False, str, None)
    (Required for new resource) NA


  public_service_endpoint (False, bool, None)
    NA


  private_service_endpoint (False, bool, None)
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

