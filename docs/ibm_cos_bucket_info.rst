
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

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  single_site_location (False, str, None)
    None


  cross_region_location (False, str, None)
    None


  bucket_region (True, str, None)
    None


  key_protect (False, str, None)
    CRN of the key you want to use data at rest encryption


  metrics_monitoring (False, list, None)
    None


  s3_endpoint_private (False, str, None)
    Private endpoint for the COS bucket


  bucket_name (True, str, None)
    None


  bucket_type (True, str, None)
    None


  resource_instance_id (True, str, None)
    None


  crn (False, str, None)
    CRN of resource instance


  region_location (False, str, None)
    None


  s3_endpoint_public (False, str, None)
    Public endpoint for the COS bucket


  storage_class (False, str, None)
    None


  allowed_ip (False, list, None)
    List of IPv4 or IPv6 addresses


  activity_tracking (False, list, None)
    None


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

