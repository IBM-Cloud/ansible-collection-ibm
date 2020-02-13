
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

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  private_service_endpoint (False, bool, None)
    None


  refresh_api_servers (False, bool, True)
    None


  private_service_endpoint_url (False, str, None)
    None


  cluster (False, str, None)
    (Required for new resource)


  public_service_endpoint (False, bool, None)
    None


  public_service_endpoint_url (False, str, None)
    None


  reload_workers (False, bool, True)
    None


  resource_group_id (False, str, None)
    ID of the resource group.


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

