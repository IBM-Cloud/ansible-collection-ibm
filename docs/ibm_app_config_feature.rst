
ibm_app_config_feature -- Configure IBM Cloud 'ibm_app_config_feature' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_app_config_feature' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/app_config_feature

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  environment_id (True, str, None)
    (Required for new resource) Environment Id.


  guid (True, str, None)
    (Required for new resource) GUID of the App Configuration service. Get it from the service instance credentials section of the dashboard.


  enabled_value (True, str, None)
    (Required for new resource) Value of the feature when it is enabled. The value can be BOOLEAN, STRING or a NUMERIC value as per the `type` attribute.


  tags (False, str, None)
    Tags associated with the feature.


  name (True, str, None)
    (Required for new resource) Feature name.


  feature_id (True, str, None)
    (Required for new resource) Feature id.


  description (False, str, None)
    Feature description.


  format (False, str, None)
    Format of the feature (TEXT, JSON, YAML).


  type (True, str, None)
    (Required for new resource) Type of the feature (BOOLEAN, STRING, NUMERIC).


  disabled_value (True, str, None)
    (Required for new resource) Value of the feature when it is disabled. The value can be BOOLEAN, STRING or a NUMERIC value as per the `type` attribute.


  rollout_percentage (False, int, None)
    Rollout percentage of the feature.


  segment_rules (False, list, None)
    Specify the targeting rules that is used to set different feature flag values for different segments.


  collections (False, list, None)
    List of collection id representing the collections that are associated with the specified feature flag.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


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

