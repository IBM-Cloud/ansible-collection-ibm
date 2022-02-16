
ibm_cm_version -- Configure IBM Cloud 'ibm_cm_version' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cm_version' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cm_version

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.38.2
- Terraform v0.12.20



Parameters
----------

  catalog_identifier (True, str, None)
    (Required for new resource) Catalog identifier.


  offering_id (True, str, None)
    (Required for new resource) Offering identification.


  zipurl (False, str, None)
    URL path to zip location.  If not specified, must provide content in the body of this call.


  target_version (False, str, None)
    The semver value for this new version, if not found in the zip url package content.


  target_kinds (False, list, None)
    Target kinds.  Current valid values are 'iks', 'roks', 'vcenter', and 'terraform'.


  tags (False, list, None)
    Tags array.


  content (False, str, None)
    byte array representing the content to be imported.  Only supported for OVA images at this time.


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

