
ibm_cm_object -- Configure IBM Cloud 'ibm_cm_object' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cm_object' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cm_object

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  name (True, str, None)
    (Required for new resource) The programmatic name of this object.


  kind (True, str, None)
    (Required for new resource) Kind of object. Options are "vpe", "preset_configuration", or "proxy_source".


  label_i18n (False, dict, None)
    A map of translated strings, by language code.


  tags (False, list, None)
    List of tags associated with this catalog.


  parent_id (False, str, None)
    The parent for this specific object.


  label (False, str, None)
    Display name in the requested language.


  short_description (False, str, None)
    Short description in the requested language.


  catalog_id (True, str, None)
    (Required for new resource) Catalog identifier.


  short_description_i18n (False, dict, None)
    A map of translated strings, by language code.


  data (False, str, None)
    Stringified map of data values for this object.


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

