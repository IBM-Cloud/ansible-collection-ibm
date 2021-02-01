
ibm_cdn -- Configure IBM Cloud 'ibm_cdn' resource
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cdn' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.16.1
- Terraform v0.12.20



Parameters
----------

  header (False, str, None)
    Header info


  respect_headers (False, bool, True)
    respect headers info


  path (False, str, /*)
    Path details


  host_name (True, str, None)
    (Required for new resource) Host name


  bucket_name (False, str, None)
    Bucket name


  file_extension (False, str, None)
    File extension info


  certificate_type (False, str, None)
    Certificate type


  performance_configuration (False, str, General web delivery)
    performance configuration info


  origin_address (True, str, None)
    (Required for new resource) origin address info


  origin_type (False, str, HOST_SERVER)
    Origin type info


  protocol (False, str, HTTP)
    Protocol name


  cache_key_query_rule (False, str, include-all)
    query rule info


  vendor_name (False, str, akamai)
    Vendor name


  https_port (False, int, 443)
    HTTPS port number


  cname (False, str, None)
    cname info


  http_port (False, int, 80)
    HTTP port number


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

