
ibm_onboarding_catalog_product -- Configure IBM Cloud 'ibm_onboarding_catalog_product' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_onboarding_catalog_product' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/onboarding_catalog_product

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  name (True, str, None)
    (Required for new resource) The programmatic name of this product.


  overview_ui (False, list, None)
    The object that contains the service details from the Overview page in global catalog.


  product_id (True, str, None)
    (Required for new resource) The unique ID of the product.


  env (False, str, None)
    The environment to fetch this object from.


  object_id (False, str, None)
    The desired ID of the global catalog object.


  images (False, list, None)
    Images from the global catalog entry that help illustrate the service.


  active (True, bool, None)
    (Required for new resource) Whether the service is active.


  kind (True, str, None)
    (Required for new resource) The kind of the global catalog object.


  object_provider (True, list, None)
    (Required for new resource) The provider or owner of the product.


  disabled (True, bool, None)
    (Required for new resource) Determines the global visibility for the catalog entry, and its children. If it is not enabled, all plans are disabled.


  tags (True, list, None)
    (Required for new resource) A list of tags that carry information about your product. These tags can be used to find your product in the IBM Cloud catalog.


  metadata (False, list, None)
    The global catalog service metadata object.


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

