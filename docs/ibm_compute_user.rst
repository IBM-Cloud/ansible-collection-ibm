
ibm_compute_user -- Configure IBM Cloud 'ibm_compute_user' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_compute_user' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.6
- Terraform v0.12.20



Parameters
----------

  state_ (False, str, None)
    (Required for new resource)


  user_status (False, str, ACTIVE)
    None


  password (False, str, None)
    None


  city (False, str, None)
    (Required for new resource)


  email (False, str, None)
    (Required for new resource)


  address1 (False, str, None)
    (Required for new resource)


  address2 (False, str, None)
    None


  timezone (False, str, None)
    (Required for new resource)


  last_name (False, str, None)
    (Required for new resource)


  first_name (False, str, None)
    (Required for new resource)


  country (False, str, None)
    (Required for new resource)


  permissions (False, list, None)
    None


  has_api_key (False, bool, False)
    None


  tags (False, list, None)
    None


  username (False, str, None)
    None


  api_key (False, str, None)
    None


  ibm_id (False, str, None)
    None


  company_name (False, str, None)
    (Required for new resource)


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

