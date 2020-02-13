
ibm_kp_key -- Configure IBM Cloud 'ibm_kp_key' resource
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_kp_key' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  resource_name (False, str, None)
    The name of the resource


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about the resource


  key_protect_id (False, str, None)
    (Required for new resource)


  key_id (False, str, None)
    None


  key_name (False, str, None)
    (Required for new resource)


  iv_value (False, str, None)
    Only for imported root key


  resource_crn (False, str, None)
    The crn of the resource


  resource_status (False, str, None)
    The status of the resource


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  standard_key (False, bool, False)
    None


  payload (False, str, None)
    None


  encrypted_nonce (False, str, None)
    Only for imported root key


  crn (False, str, None)
    Crn of the key


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

