
ibm_app_config_property -- Configure IBM Cloud 'ibm_app_config_property' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_app_config_property' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/app_config_property

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.49.0
- Terraform v0.12.20



Parameters
----------

  guid (True, str, None)
    (Required for new resource) GUID of the App Configuration service. Get it from the service instance credentials section of the dashboard.


  environment_id (True, str, None)
    (Required for new resource) Environment Id.


  type (True, str, None)
    (Required for new resource) Type of the Property  (BOOLEAN, STRING, NUMERIC).


  name (True, str, None)
    (Required for new resource) Property name.


  value (True, str, None)
    (Required for new resource) Value of the Property. The value can be Boolean, String or a Numeric value as per the `type` attribute.


  format (False, str, None)
    Format of the feature (TEXT, JSON, YAML).


  tags (False, str, None)
    Tags associated with the property.


  segment_rules (False, list, None)
    Specify the targeting rules that is used to set different property values for different segments.


  collections (False, list, None)
    List of collection id representing the collections that are associated with the specified property.


  property_id (True, str, None)
    (Required for new resource) Property id.


  description (False, str, None)
    Property description.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


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

