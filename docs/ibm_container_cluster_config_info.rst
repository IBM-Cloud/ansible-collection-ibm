
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

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  calico_config_file_path (False, str, None)
    The absolute path to the calico network config file


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  config_dir (False, str, None)
    The directory where the cluster config to be downloaded. Default is home directory


  region (False, str, None)
    The cluster region


  resource_group_id (False, str, None)
    ID of the resource group.


  cluster_name_id (True, str, None)
    The name/id of the cluster


  download (False, bool, True)
    If set to false will not download the config, otherwise they are downloaded each time but onto the same path for a given cluster name/id


  admin (False, bool, False)
    If set to true will download the config for admin


  network (False, bool, False)
    If set to true will download the Calico network config with the Admin config


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  config_file_path (False, str, None)
    The absolute path to the kubernetes config yml file


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

