
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

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  path (False, str, /*)
    None


  cache_key_query_rule (False, str, include-all)
    None


  protocol (False, str, HTTP)
    None


  respect_headers (False, bool, True)
    None


  performance_configuration (False, str, General web delivery)
    None


  vendor_name (False, str, akamai)
    None


  origin_address (False, str, None)
    (Required for new resource)


  http_port (False, int, 80)
    None


  status (False, str, None)
    None


  https_port (False, int, 443)
    None


  cname (False, str, None)
    None


  file_extension (False, str, None)
    None


  certificate_type (False, str, None)
    None


  host_name (False, str, None)
    (Required for new resource)


  bucket_name (False, str, None)
    None


  header (False, str, None)
    None


  origin_type (False, str, HOST_SERVER)
    None


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

