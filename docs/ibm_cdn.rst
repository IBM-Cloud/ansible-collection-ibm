
ibm_cdn -- Configure IBM Cloud 'ibm_cdn' resource
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cdn' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  host_name (False, str, None)
    (Required for new resource) NA


  vendor_name (False, str, akamai)
    NA


  http_port (False, int, 80)
    NA


  cache_key_query_rule (False, str, include-all)
    NA


  bucket_name (False, str, None)
    NA


  protocol (False, str, HTTP)
    NA


  https_port (False, int, 443)
    NA


  respect_headers (False, bool, True)
    NA


  performance_configuration (False, str, General web delivery)
    NA


  origin_type (False, str, HOST_SERVER)
    NA


  origin_address (False, str, None)
    (Required for new resource) NA


  cname (False, str, None)
    NA


  header (False, str, None)
    NA


  certificate_type (False, str, None)
    NA


  status (False, str, None)
    NA


  file_extension (False, str, None)
    NA


  path (False, str, /*)
    NA


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

