
ibm_cis_domain_settings -- Configure IBM Cloud 'ibm_cis_domain_settings' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_domain_settings' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.5
- Terraform v0.12.20



Parameters
----------

  min_tls_version (False, str, 1.1)
    Minimum version of TLS required


  cname_flattening (False, str, None)
    cname_flattening setting


  opportunistic_encryption (False, str, None)
    opportunistic_encryption setting


  automatic_https_rewrites (False, str, None)
    automatic_https_rewrites setting


  waf (False, str, None)
    WAF setting


  certificate_status (False, str, None)
    Certificate status


  ssl (False, str, None)
    SSL/TLS setting


  cis_id (False, str, None)
    (Required for new resource) CIS instance crn


  domain_id (False, str, None)
    (Required for new resource) Associated CIS domain


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

