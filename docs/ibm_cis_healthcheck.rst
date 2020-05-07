
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

- IBM-Cloud terraform-provider-ibm v1.5.2
- Terraform v0.12.20



Parameters
----------

  path (False, str, None)
    path


  type (False, str, http)
    type


  method (False, str, None)
    method


  retries (False, int, 2)
    retries


  interval (False, int, 60)
    interval


  expected_body (False, str, None)
    expected_body


  expected_codes (False, str, None)
    expected_codes


  description (False, str, None)
    description


  modified_on (False, str, None)
    None


  port (False, int, None)
    None


  cis_id (False, str, None)
    (Required for new resource) CIS instance crn


  allow_insecure (False, bool, False)
    allow_insecure


  timeout (False, int, 5)
    timeout


  follow_redirects (False, bool, None)
    follow_redirects


  created_on (False, str, None)
    None


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

