
ibm_is_images_info -- Retrieve IBM Cloud 'ibm_is_images' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_images' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_images

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  resource_group (False, str, None)
    The id of the resource group


  catalog_managed (False, bool, None)
    Lists images managed as part of a catalog offering. If an image is managed, accounts in the same enterprise with access to that catalog can specify the image's catalog offering version CRN to provision virtual server instances using the image


  name (False, str, None)
    The name of the image


  status (False, str, None)
    The status of the image


  visibility (False, str, None)
    Whether the image is publicly visible or private to the account


  user_data_format (False, list, None)
    Filters the collection to images with a user_data_format property matching one of the specified comma-separated values.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

