
ibm_cm_catalog -- Configure IBM Cloud 'ibm_cm_catalog' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cm_catalog' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cm_catalog

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.50.0
- Terraform v0.12.20



Parameters
----------

  kind (False, str, None)
    Kind of catalog. Supported kinds are offering and vpe.


  short_description_i18n (False, dict, None)
    A map of translated strings, by language code.


  tags (False, list, None)
    List of tags associated with this catalog.


  metadata (False, dict, None)
    Catalog specific metadata.


  resource_group_id (False, str, None)
    Resource group id the catalog is owned by.


  features (False, list, None)
    List of features associated with this catalog.


  short_description (False, str, None)
    Description in the requested language.


  catalog_icon_url (False, str, None)
    URL for an icon associated with this catalog.


  disabled (False, bool, None)
    Denotes whether a catalog is disabled.


  label (False, str, None)
    Display Name in the requested language.


  label_i18n (False, dict, None)
    A map of translated strings, by language code.


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

