
ibm_app_config_segment -- Configure IBM Cloud 'ibm_app_config_segment' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_app_config_segment' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/app_config_segment

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  tags (False, str, None)
    Tags associated with the segments.


  guid (True, str, None)
    (Required for new resource) GUID of the App Configuration service. Get it from the service instance credentials section of the dashboard.


  name (True, str, None)
    (Required for new resource) Segment name.


  rules (True, list, None)
    (Required for new resource) List of rules that determine if the entity belongs to the segment during feature / property evaluation. An entity is identified by an unique identifier and the attributes that it defines.


  segment_id (True, str, None)
    (Required for new resource) Segment id.


  description (False, str, None)
    Segment description.


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

