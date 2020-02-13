
ibm_cis_global_load_balancer -- Configure IBM Cloud 'ibm_cis_global_load_balancer' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_global_load_balancer' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  domain_id (False, str, None)
    (Required for new resource) Associated CIS domain


  name (False, str, None)
    (Required for new resource) name


  fallback_pool_id (False, str, None)
    (Required for new resource) name


  description (False, str, None)
    None


  session_affinity (False, str, none)
    None


  created_on (False, str, None)
    None


  modified_on (False, str, None)
    None


  cis_id (False, str, None)
    (Required for new resource) CIS instance crn


  default_pool_ids (False, list, None)
    (Required for new resource)


  ttl (False, int, None)
    None


  proxied (False, bool, False)
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

