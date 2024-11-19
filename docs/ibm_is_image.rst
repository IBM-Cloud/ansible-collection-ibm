
ibm_is_image -- Configure IBM Cloud 'ibm_is_image' resource
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_image' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_image

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  href (False, str, None)
    Image Href value


  deprecation_at (False, str, None)
    The deprecation date and time (UTC) for this image. If absent, no deprecation date and time has been set.


  encryption_key (False, str, None)
    The CRN of the Key Protect Root Key or Hyper Protect Crypto Service Root Key for this resource


  deprecate (False, bool, None)
    Set to deprecate. You can set an image to `deprecated` as a warning to transition away from soon-to-be obsolete images. Deprecated images can be used to provision resources.


  source_volume (False, str, None)
    Image volume id


  obsolete (False, bool, None)
    Set to obsolete. You can set an image to `obsolete` as a warning to transition away from soon-to-be deleted images. You can't use obsolete images to provision resources.


  operating_system (False, str, None)
    Image Operating system


  access_tags (False, list, None)
    List of access management tags


  name (True, str, None)
    (Required for new resource) Image name


  encrypted_data_key (False, str, None)
    A base64-encoded, encrypted representation of the key that was used to encrypt the data for this image


  obsolescence_at (False, str, None)
    The obsolescence date and time (UTC) for this image. If absent, no obsolescence date and time has been set.


  tags (False, list, None)
    Tags for the image


  resource_group (False, str, None)
    The resource group for this image


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

