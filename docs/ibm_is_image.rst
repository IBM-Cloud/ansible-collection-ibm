
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

- IBM-Cloud terraform-provider-ibm v1.34.0
- Terraform v0.12.20



Parameters
----------

  href (False, str, None)
    Image Href value


  encrypted_data_key (False, str, None)
    A base64-encoded, encrypted representation of the key that was used to encrypt the data for this image


  encryption_key (False, str, None)
    The CRN of the Key Protect Root Key or Hyper Protect Crypto Service Root Key for this resource


  source_volume (False, str, None)
    Image volume id


  name (True, str, None)
    (Required for new resource) Image name


  operating_system (False, str, None)
    Image Operating system


  resource_group (False, str, None)
    The resource group for this image


  tags (False, list, None)
    Tags for the image


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

