
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

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  username (False, str, None)
    NA


  last_name (False, str, None)
    (Required for new resource) NA


  country (False, str, None)
    (Required for new resource) NA


  password (False, str, None)
    NA


  permissions (False, list, None)
    NA


  has_api_key (False, bool, False)
    NA


  api_key (False, str, None)
    NA


  first_name (False, str, None)
    (Required for new resource) NA


  email (False, str, None)
    (Required for new resource) NA


  address1 (False, str, None)
    (Required for new resource) NA


  address2 (False, str, None)
    NA


  state_ (False, str, None)
    (Required for new resource) NA


  user_status (False, str, ACTIVE)
    NA


  ibm_id (False, str, None)
    NA


  company_name (False, str, None)
    (Required for new resource) NA


  city (False, str, None)
    (Required for new resource) NA


  timezone (False, str, None)
    (Required for new resource) NA


  tags (False, list, None)
    NA


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

