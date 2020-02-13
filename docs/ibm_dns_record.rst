
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

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  host (False, str, None)
    (Required for new resource)


  refresh (False, int, None)
    None


  responsible_person (False, str, None)
    None


  type (False, str, None)
    (Required for new resource)


  protocol (False, str, None)
    None


  priority (False, int, 0)
    None


  weight (False, int, 0)
    None


  expire (False, int, None)
    None


  mx_priority (False, int, 0)
    None


  retry (False, int, None)
    None


  ttl (False, int, None)
    (Required for new resource)


  tags (False, list, None)
    None


  data (False, str, None)
    (Required for new resource)


  domain_id (False, int, None)
    (Required for new resource)


  minimum_ttl (False, int, None)
    None


  service (False, str, None)
    None


  port (False, int, None)
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

