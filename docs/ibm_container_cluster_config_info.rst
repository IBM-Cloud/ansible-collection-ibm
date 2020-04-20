
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

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  download (False, bool, True)
    If set to false will not download the config, otherwise they are downloaded each time but onto the same path for a given cluster name/id


  host (False, str, None)
    NA


  org_guid (False, str, None)
    The bluemix organization guid this cluster belongs to


  region (False, str, None)
    The cluster region


  config_file_path (False, str, None)
    The absolute path to the kubernetes config yml file


  admin_certificate (False, str, None)
    NA


  space_guid (False, str, None)
    The bluemix space guid this cluster belongs to


  config_dir (False, str, None)
    The directory where the cluster config to be downloaded. Default is home directory


  network (False, bool, False)
    If set to true will download the Calico network config with the Admin config


  calico_config_file_path (False, str, None)
    The absolute path to the calico network config file


  admin_key (False, str, None)
    NA


  resource_group_id (False, str, None)
    ID of the resource group.


  cluster_name_id (True, str, None)
    The name/id of the cluster


  admin (False, bool, False)
    If set to true will download the config for admin


  ca_certificate (False, str, None)
    NA


  token (False, str, None)
    NA


  account_guid (False, str, None)
    The bluemix account guid this cluster belongs to


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

