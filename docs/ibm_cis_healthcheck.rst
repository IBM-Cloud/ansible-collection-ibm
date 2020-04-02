
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

- IBM-Cloud terraform-provider-ibm v1.3.0
- Terraform v0.12.20



Parameters
----------

  cis_id (False, str, None)
    (Required for new resource) CIS instance crn


  type (False, str, http)
    type


  allow_insecure (False, bool, True)
    allow_insecure


  timeout (False, int, 5)
    timeout


  retries (False, int, 2)
    retries


  path (False, str, /)
    path


  expected_body (False, str, None)
    (Required for new resource) expected_body


  expected_codes (False, str, None)
    (Required for new resource) expected_codes


  description (False, str, None)
    description


  follow_redirects (False, bool, True)
    follow_redirects


  modified_on (False, str, None)
    None


  method (False, str, GET)
    method


  interval (False, int, 60)
    interval


  created_on (False, str, None)
    None


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

