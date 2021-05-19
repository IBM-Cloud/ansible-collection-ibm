
ibm_satellite_location -- Configure IBM Cloud 'ibm_satellite_location' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_satellite_location' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/satellite_location

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.25.0
- Terraform v0.12.20



Parameters
----------

  logging_account_id (False, str, None)
    The account ID for IBM Log Analysis with LogDNA log forwarding


  zones (False, list, None)
    The names of at least three high availability zones to use for the location


  location (True, str, None)
    (Required for new resource) A unique name for the new Satellite location


  cos_config (False, list, None)
    COSBucket - IBM Cloud Object Storage bucket configuration details


  tags (False, list, None)
    List of tags associated with resource instance


  managed_from (True, str, None)
    (Required for new resource) The IBM Cloud metro from which the Satellite location is managed


  cos_credentials (False, list, None)
    COSAuthorization - IBM Cloud Object Storage authorization keys


  resource_group_id (False, str, None)
    ID of the resource group.


  description (False, str, None)
    A description of the new Satellite location


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

