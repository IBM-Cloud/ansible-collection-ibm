
ibm_config_aggregator_settings -- Configure IBM Cloud 'ibm_config_aggregator_settings' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_config_aggregator_settings' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/config_aggregator_settings

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  resource_collection_regions (True, list, None)
    (Required for new resource) The list of regions across which the resource collection is enabled.


  additional_scope (False, list, None)
    The additional scope that enables resource collection for Enterprise acccounts.


  instance_id (True, str, None)
    (Required for new resource) The ID of the configuration aggregator instance.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  resource_collection_enabled (True, bool, None)
    (Required for new resource) The field denoting if the resource collection is enabled.


  trusted_profile_id (True, str, None)
    (Required for new resource) The trusted profile id that provides Reader access to the App Configuration instance to collect resource metadata.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

