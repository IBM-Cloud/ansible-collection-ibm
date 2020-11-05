
ibm_container_bind_service -- Configure IBM Cloud 'ibm_container_bind_service' resource
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_bind_service' resource

This module supports idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.14.0
- Terraform v0.12.20



Parameters
----------

  cluster_name_id (True, str, None)
    (Required for new resource) Cluster name or ID


  tags (False, list, None)
    List of tags for the resource


  service_instance_name (False, str, None)
    serivice instance name


  namespace_id (True, str, None)
    (Required for new resource) namespace ID


  key (False, str, None)
    Key info


  role (False, str, None)
    Role info


  service_instance_id (False, str, None)
    Service instance ID


  resource_group_id (False, str, None)
    ID of the resource group.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

