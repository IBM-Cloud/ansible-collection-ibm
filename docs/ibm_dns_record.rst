
ibm_dns_record -- Configure IBM Cloud 'ibm_dns_record' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dns_record' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.3
- Terraform v0.12.20



Parameters
----------

  retry (False, int, None)
    None


  service (False, str, None)
    None


  expire (False, int, None)
    None


  mx_priority (False, int, 0)
    None


  responsible_person (False, str, None)
    None


  protocol (False, str, None)
    None


  port (False, int, None)
    None


  type (False, str, None)
    (Required for new resource)


  priority (False, int, 0)
    None


  tags (False, list, None)
    None


  data (False, str, None)
    (Required for new resource)


  domain_id (False, int, None)
    (Required for new resource)


  refresh (False, int, None)
    None


  weight (False, int, 0)
    None


  host (False, str, None)
    (Required for new resource)


  minimum_ttl (False, int, None)
    None


  ttl (False, int, None)
    (Required for new resource)


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

