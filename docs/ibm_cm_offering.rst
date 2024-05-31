
ibm_cm_offering -- Configure IBM Cloud 'ibm_cm_offering' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cm_offering' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cm_offering

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.65.1
- Terraform v1.5.5



Parameters
----------

  long_description_i18n (False, dict, None)
    A map of translated strings, by language code.


  label (False, str, None)
    Display Name in the requested language.


  long_description (False, str, None)
    Long description in the requested language.


  provider_info (False, list, None)
    Information on the provider for this offering, or omitted if no provider information is given.


  share_with_all (False, bool, None)
    Denotes public availability of an Offering - if share_enabled is true.


  share_with_access_list (False, list, None)
    A list of account IDs to add to this offering's access list.


  publish_public_crn (False, str, None)
    The crn of the public catalog entry of this offering.


  short_description (False, str, None)
    Short description in the requested language.


  share_enabled (False, bool, None)
    Denotes sharing including access list availability of an Offering is enabled.


  deprecate (False, bool, None)
    Deprecate this offering.


  share_with_ibm (False, bool, None)
    Denotes IBM employee availability of an Offering - if share_enabled is true.


  image_pull_keys (False, list, None)
    Image pull keys for this offering.


  media (False, list, None)
    A list of media items related to this offering.


  features (False, list, None)
    list of features associated with this offering.


  portal_approval_record (False, str, None)
    The portal's approval record ID.


  disclaimer (False, str, None)
    A disclaimer for this offering.


  label_i18n (False, dict, None)
    A map of translated strings, by language code.


  offering_icon_url (False, str, None)
    URL for an icon associated with this offering.


  keywords (False, list, None)
    List of keywords associated with offering, typically used to search for it.


  short_description_i18n (False, dict, None)
    A map of translated strings, by language code.


  metadata (False, dict, None)
    Map of metadata values for this offering.


  offering_id (False, str, None)
    Offering identifier.  Provide this when an offering already exists and you wish to use it as a terraform resource.


  name (False, str, None)
    The programmatic name of this offering.


  offering_docs_url (False, str, None)
    URL for an additional docs with this offering.


  tags (False, list, None)
    List of tags associated with this catalog.


  public_original_crn (False, str, None)
    The original offering CRN that this publish entry came from.


  portal_ui_url (False, str, None)
    The portal UI URL.


  hidden (False, bool, None)
    Determine if this offering should be displayed in the Consumption UI.


  catalog_id (True, str, None)
    (Required for new resource) Catalog identifier.


  product_kind (False, str, None)
    The product kind.  Valid values are module, solution, or empty string.


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

