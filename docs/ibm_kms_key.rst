
ibm_kms_key -- Configure IBM Cloud 'ibm_kms_key' resource
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_kms_key' resource

This module supports idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.20.0
- Terraform v0.12.20



Parameters
----------

  key_name (True, str, None)
    (Required for new resource) Key name


  endpoint_type (False, str, public)
    public or private


  payload (False, str, None)
    None


  encrypted_nonce (False, str, None)
    Only for imported root key


  force_delete (False, bool, False)
    set to true to force delete the key


  standard_key (False, bool, False)
    Standard key type


  iv_value (False, str, None)
    Only for imported root key


  policies (False, list, None)
    Creates or updates one or more policies for the specified key


  instance_id (True, str, None)
    (Required for new resource) Key protect or hpcs instance GUID


  expiration_date (False, str, None)
    The date the key material expires. The date format follows RFC 3339. You can set an expiration date on any key on its creation. A key moves into the Deactivated state within one hour past its expiration date, if one is assigned. If you create a key without specifying an expiration date, the key does not expire


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

