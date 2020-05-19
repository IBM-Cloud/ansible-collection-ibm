
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

- IBM-Cloud terraform-provider-ibm v1.5.3
- Terraform v0.12.20



Parameters
----------

  last_name (False, str, None)
    (Required for new resource) Last name of the user


  city (False, str, None)
    (Required for new resource) City name


  state_ (False, str, None)
    (Required for new resource) Satate name


  permissions (False, list, None)
    set of persmissions assigned for the user


  company_name (False, str, None)
    (Required for new resource) comapany name


  address2 (False, str, None)
    Address info of the user


  has_api_key (False, bool, False)
    API Key info of the user


  username (False, str, None)
    user name


  email (False, str, None)
    (Required for new resource) email address of the user


  timezone (False, str, None)
    (Required for new resource) time zone info


  api_key (False, str, None)
    API key for the user


  ibm_id (False, str, None)
    IBM ID of the  user


  first_name (False, str, None)
    (Required for new resource) First name of the user


  address1 (False, str, None)
    (Required for new resource) Address info of the user


  country (False, str, None)
    (Required for new resource) Country name


  user_status (False, str, ACTIVE)
    user status info


  password (False, str, None)
    password for the user


  tags (False, list, None)
    Tags set for the resources


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

