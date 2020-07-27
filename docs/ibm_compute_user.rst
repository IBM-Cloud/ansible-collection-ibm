
ibm_compute_user -- Configure IBM Cloud 'ibm_compute_user' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_compute_user' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.9.0
- Terraform v0.12.20



Parameters
----------

  state_ (True, str, None)
    (Required for new resource) Satate name


  user_status (False, str, ACTIVE)
    user status info


  has_api_key (False, bool, False)
    API Key info of the user


  first_name (True, str, None)
    (Required for new resource) First name of the user


  email (True, str, None)
    (Required for new resource) email address of the user


  country (True, str, None)
    (Required for new resource) Country name


  tags (False, list, None)
    Tags set for the resources


  last_name (True, str, None)
    (Required for new resource) Last name of the user


  company_name (True, str, None)
    (Required for new resource) comapany name


  city (True, str, None)
    (Required for new resource) City name


  address1 (True, str, None)
    (Required for new resource) Address info of the user


  address2 (False, str, None)
    Address info of the user


  timezone (True, str, None)
    (Required for new resource) time zone info


  password (False, str, None)
    password for the user


  permissions (False, list, None)
    set of persmissions assigned for the user


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

