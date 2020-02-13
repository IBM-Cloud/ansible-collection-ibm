
ibm_cos_bucket_info -- Retrieve IBM Cloud 'ibm_cos_bucket' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_cos_bucket' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  s3_endpoint_private (False, str, None)
    Private endpoint for the COS bucket


  bucket_region (True, str, None)
    None


  resource_instance_id (True, str, None)
    None


  crn (False, str, None)
    CRN of resource instance


  region_location (False, str, None)
    None


  cross_region_location (False, str, None)
    None


  storage_class (False, str, None)
    None


  bucket_name (True, str, None)
    None


  bucket_type (True, str, None)
    None


  key_protect (False, str, None)
    CRN of the key you want to use data at rest encryption


  single_site_location (False, str, None)
    None


  s3_endpoint_public (False, str, None)
    Public endpoint for the COS bucket


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

