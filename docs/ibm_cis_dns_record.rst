
ibm_cis_dns_record -- Configure IBM Cloud 'ibm_cis_dns_record' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_dns_record' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.2
- Terraform v0.12.20



Parameters
----------

  priority (False, int, None)
    None


  proxied (False, bool, False)
    None


  proxiable (False, bool, None)
    None


  cis_id (False, str, None)
    (Required for new resource) CIS object id


  name (False, str, None)
    (Required for new resource)


  data (False, dict, None)
    None


  created_on (False, str, None)
    None


  modified_on (False, str, None)
    None


  domain_id (False, str, None)
    (Required for new resource) Associated CIS domain


  type (False, str, None)
    (Required for new resource)


  content (False, str, None)
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

