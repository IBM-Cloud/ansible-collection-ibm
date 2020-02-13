
ibm_certificate_manager_import -- Configure IBM Cloud 'ibm_certificate_manager_import' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_certificate_manager_import' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  description (False, str, None)
    None


  issuer (False, str, None)
    None


  begins_on (False, int, None)
    None


  expires_on (False, int, None)
    None


  has_previous (False, str, None)
    None


  certificate_manager_instance_id (False, str, None)
    (Required for new resource)


  name (False, str, None)
    (Required for new resource)


  data (False, dict, None)
    (Required for new resource)


  key_algorithm (False, str, None)
    None


  algorithm (False, str, None)
    None


  imported (False, bool, None)
    None


  status (False, str, None)
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

