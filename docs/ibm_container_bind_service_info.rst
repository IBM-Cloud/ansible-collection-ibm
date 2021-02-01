
ibm_container_bind_service_info -- Retrieve IBM Cloud 'ibm_container_bind_service' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_bind_service' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.19.0
- Terraform v0.12.20



Parameters
----------

  cluster_name_id (True, str, None)
    Cluster name or ID


  service_instance_id (False, str, None)
    Service instance ID


  service_instance_name (False, str, None)
    serivice instance name


  namespace_id (True, str, None)
    namespace ID


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

