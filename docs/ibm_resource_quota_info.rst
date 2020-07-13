
ibm_resource_quota_info -- Retrieve IBM Cloud 'ibm_resource_quota' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_resource_quota' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  type (False, str, None)
    Type of the quota.


  max_apps (False, int, None)
    Defines the total app limit.


  max_instances_per_app (False, int, None)
    Defines the total instances limit per app.


  max_app_instance_memory (False, str, None)
    Defines the total memory of app instance.


  total_app_memory (False, str, None)
    Defines the total memory for app.


  max_service_instances (False, int, None)
    Defines the total service instances limit.


  vsi_limit (False, int, None)
    Defines the VSI limit.


  name (True, str, None)
    Resource quota name, for example Trial Quota


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

