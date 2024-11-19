
ibm_is_image_export_job -- Configure IBM Cloud 'ibm_is_image_export_job' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_image_export_job' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_image_export_job

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  format (False, str, qcow2)
    The format to use for the exported image. If the image is encrypted, only `qcow2` is supported.


  storage_bucket (True, list, None)
    (Required for new resource) The name of the Cloud Object Storage bucket to export the image to.


  name (False, str, None)
    The user-defined name for this image export job. Names must be unique within the image this export job resides in. If unspecified, the name will be a hyphenated list of randomly-selected words prefixed with the first 16 characters of the parent image name.The exported image object name in Cloud Object Storage (`storage_object.name` in the response) will be based on this name. The object name will be unique within the bucket.


  image (True, str, None)
    (Required for new resource) The image identifier.


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

