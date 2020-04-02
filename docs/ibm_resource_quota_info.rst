
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

- IBM-Cloud terraform-provider-ibm v1.3.0
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


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

