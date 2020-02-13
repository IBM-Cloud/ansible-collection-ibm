
ibm_compute_ssl_certificate -- Configure IBM Cloud 'ibm_compute_ssl_certificate' resource
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_compute_ssl_certificate' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  validity_end (False, str, None)
    None


  create_date (False, str, None)
    None


  tags (False, list, None)
    None


  intermediate_certificate (False, str, None)
    None


  organization_name (False, str, None)
    None


  validity_begin (False, str, None)
    None


  validity_days (False, int, None)
    None


  key_size (False, int, None)
    None


  modify_date (False, str, None)
    None


  certificate (False, str, None)
    (Required for new resource)


  private_key (False, str, None)
    (Required for new resource)


  common_name (False, str, None)
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

