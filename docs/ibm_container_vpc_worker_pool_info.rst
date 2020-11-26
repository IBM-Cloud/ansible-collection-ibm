
ibm_container_vpc_worker_pool_info -- Retrieve IBM Cloud 'ibm_container_vpc_worker_pool' resource
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_vpc_worker_pool' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.15.0
- Terraform v0.12.20



Parameters
----------

  cluster (True, str, None)
    Cluster name


  worker_pool_name (True, str, None)
    worker pool name


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

