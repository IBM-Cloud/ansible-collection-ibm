
ibm_cos_bucket -- Configure IBM Cloud 'ibm_cos_bucket' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cos_bucket' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  resource_instance_id (False, str, None)
    (Required for new resource)


  crn (False, str, None)
    CRN of resource instance


  single_site_location (False, str, None)
    None


  region_location (False, str, None)
    None


  s3_endpoint_public (False, str, None)
    Public endpoint for the COS bucket


  bucket_name (False, str, None)
    (Required for new resource)


  key_protect (False, str, None)
    CRN of the key you want to use data at rest encryption


  cross_region_location (False, str, None)
    None


  storage_class (False, str, None)
    (Required for new resource)


  s3_endpoint_private (False, str, None)
    Private endpoint for the COS bucket


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

