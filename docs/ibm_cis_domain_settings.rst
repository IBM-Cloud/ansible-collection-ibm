
ibm_cis_domain_settings -- Configure IBM Cloud 'ibm_cis_domain_settings' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_domain_settings' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cis_domain_settings

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.38.2
- Terraform v0.12.20



Parameters
----------

  max_upload (False, int, None)
    Maximum upload


  minify (False, list, None)
    Minify setting


  ip_geolocation (False, str, None)
    ip_geolocation setting


  image_size_optimization (False, str, None)
    image_size_optimization setting


  origin_error_page_pass_thru (False, str, None)
    origin_error_page_pass_thru setting


  response_buffering (False, str, None)
    response_buffering setting


  server_side_exclude (False, str, None)
    server_side_exclude setting


  websockets (False, str, None)
    websockets setting


  cname_flattening (False, str, None)
    cname_flattening setting


  prefetch_preload (False, str, None)
    prefetch_preload setting


  cipher (False, list, None)
    Cipher settings


  mobile_redirect (False, list, None)
    None


  domain_id (True, str, None)
    (Required for new resource) Associated CIS domain


  browser_check (False, str, None)
    browser_check setting


  tls_client_auth (False, str, None)
    tls_client_auth setting


  security_header (False, list, None)
    Security Header Setting


  dnssec (False, str, None)
    DNS Sec setting


  min_tls_version (False, str, 1.1)
    Minimum version of TLS required


  automatic_https_rewrites (False, str, None)
    automatic_https_rewrites setting


  always_use_https (False, str, None)
    always_use_https setting


  ipv6 (False, str, None)
    ipv6 setting


  http2 (False, str, None)
    http2 setting


  brotli (False, str, None)
    brotli setting


  pseudo_ipv4 (False, str, None)
    pseudo_ipv4 setting


  waf (False, str, None)
    WAF setting


  ssl (False, str, None)
    SSL/TLS setting


  true_client_ip_header (False, str, None)
    true_client_ip_header setting


  cis_id (True, str, None)
    (Required for new resource) CIS instance crn


  hotlink_protection (False, str, None)
    hotlink_protection setting


  image_load_optimization (False, str, None)
    image_load_optimization setting


  script_load_optimization (False, str, None)
    script_load_optimization setting


  challenge_ttl (False, int, None)
    Challenge TTL setting


  opportunistic_encryption (False, str, None)
    opportunistic_encryption setting


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

