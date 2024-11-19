
ibm_container_cluster_config_info -- Retrieve IBM Cloud 'ibm_container_cluster_config' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_cluster_config' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/container_cluster_config

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  download (False, bool, True)
    If set to false will not download the config, otherwise they are downloaded each time but onto the same path for a given cluster name/id


  endpoint_type (False, str, None)
    It can specify what kind of server URL will be used for the cluster context


  resource_group_id (False, str, None)
    ID of the resource group.


  admin (False, bool, False)
    If set to true will download the config for admin


  network (False, bool, False)
    If set to true will download the Calico network config with the Admin config


  config_dir (False, str, None)
    The directory where the cluster config to be downloaded. Default is home directory


  cluster_name_id (True, str, None)
    The name/id of the cluster


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

