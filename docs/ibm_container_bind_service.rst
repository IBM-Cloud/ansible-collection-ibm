
ibm_container_bind_service -- Configure IBM Cloud 'ibm_container_bind_service' resource
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_bind_service' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  namespace_id (False, str, None)
    (Required for new resource)


  role (False, str, None)
    None


  resource_group_id (False, str, None)
    ID of the resource group.


  service_instance_name (False, str, None)
    None


  service_instance_id (False, str, None)
    None


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  key (False, str, None)
    None


  cluster_name_id (False, str, None)
    (Required for new resource)


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  region (False, str, None)
    The cluster region


  tags (False, list, None)
    None


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


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

