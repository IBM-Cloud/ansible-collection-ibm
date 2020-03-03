
ibm_cis_healthcheck -- Configure IBM Cloud 'ibm_cis_healthcheck' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_healthcheck' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.3
- Terraform v0.12.20



Parameters
----------

  cis_id (False, str, None)
    (Required for new resource) CIS instance crn


  expected_codes (False, str, None)
    (Required for new resource) expected_codes


  method (False, str, GET)
    method


  timeout (False, int, 5)
    timeout


  interval (False, int, 60)
    interval


  allow_insecure (False, bool, True)
    allow_insecure


  type (False, str, http)
    type


  modified_on (False, str, None)
    None


  description (False, str, None)
    description


  retries (False, int, 2)
    retries


  created_on (False, str, None)
    None


  path (False, str, /)
    path


  expected_body (False, str, None)
    (Required for new resource) expected_body


  follow_redirects (False, bool, True)
    follow_redirects


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

