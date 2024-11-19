
ibm_container_bind_service_info -- Retrieve IBM Cloud 'ibm_container_bind_service' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_bind_service' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/container_bind_service

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  service_instance_id (False, str, None)
    Service instance ID


  service_instance_name (False, str, None)
    serivice instance name


  namespace_id (True, str, None)
    namespace ID


  cluster_name_id (True, str, None)
    Cluster name or ID


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

