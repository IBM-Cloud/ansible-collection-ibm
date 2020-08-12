
ibm_container_cluster_config_info -- Retrieve IBM Cloud 'ibm_container_cluster_config' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_cluster_config' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.10.0
- Terraform v0.12.20



Parameters
----------

  resource_group_id (False, str, None)
    ID of the resource group.


  download (False, bool, True)
    If set to false will not download the config, otherwise they are downloaded each time but onto the same path for a given cluster name/id


  network (False, bool, False)
    If set to true will download the Calico network config with the Admin config


  cluster_name_id (True, str, None)
    The name/id of the cluster


  admin (False, bool, False)
    If set to true will download the config for admin


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

