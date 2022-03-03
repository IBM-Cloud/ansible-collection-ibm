
ibm_cos_bucket -- Configure IBM Cloud 'ibm_cos_bucket' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cos_bucket' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cos_bucket

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.39.1
- Terraform v0.12.20



Parameters
----------

  endpoint_type (False, str, public)
    public or private


  hard_quota (False, int, None)
    sets a maximum amount of storage (in bytes) available for a bucket


  key_protect (False, str, None)
    CRN of the key you want to use data at rest encryption


  storage_class (True, str, None)
    (Required for new resource) Storage class info


  expire_rule (False, list, None)
    Enable configuration expire_rule to COS Bucket after a defined period of time


  retention_rule (False, list, None)
    A retention policy is enabled at the IBM Cloud Object Storage bucket level. Minimum, maximum and default retention period are defined by this policy and apply to all objects in the bucket.


  resource_instance_id (True, str, None)
    (Required for new resource) resource instance ID


  metrics_monitoring (False, list, None)
    Enables sending metrics to IBM Cloud Monitoring.


  allowed_ip (False, list, None)
    List of IPv4 or IPv6 addresses


  activity_tracking (False, list, None)
    Enables sending log data to Activity Tracker and LogDNA to provide visibility into object read and write events


  noncurrent_version_expiration (False, list, None)
    Enable configuration expire_rule to COS Bucket after a defined period of time


  single_site_location (False, str, None)
    single site location info


  cross_region_location (False, str, None)
    Cros region location info


  region_location (False, str, None)
    Region Location info.


  abort_incomplete_multipart_upload_days (False, list, None)
    Enable abort incomplete multipart upload to COS Bucket after a defined period of time


  archive_rule (False, list, None)
    Enable configuration archive_rule (glacier/accelerated) to COS Bucket after a defined period of time


  bucket_name (True, str, None)
    (Required for new resource) COS Bucket name


  object_versioning (False, list, None)
    Protect objects from accidental deletion or overwrites. Versioning allows you to keep multiple versions of an object protecting from unintentional data loss.


  force_delete (False, bool, True)
    COS buckets need to be empty before they can be deleted. force_delete option empty the bucket and delete it.


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

