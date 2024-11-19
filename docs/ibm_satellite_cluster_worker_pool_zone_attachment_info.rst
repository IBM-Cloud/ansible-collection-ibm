
ibm_satellite_cluster_worker_pool_zone_attachment_info -- Retrieve IBM Cloud 'ibm_satellite_cluster_worker_pool_zone_attachment' resource
=========================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_satellite_cluster_worker_pool_zone_attachment' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/satellite_cluster_worker_pool_zone_attachment

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  worker_pool (True, str, None)
    worker pool name


  zone (True, str, None)
    worker pool zone name


  resource_group_id (False, str, None)
    The ID of the resource group that the Satellite location is in. To list the resource group ID of the location, use the `GET /v2/satellite/getController` API method.


  cluster (True, str, None)
    Name or id of the cluster


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

