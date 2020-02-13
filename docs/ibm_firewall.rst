
ibm_firewall -- Configure IBM Cloud 'ibm_firewall' resource
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_firewall' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  public_vlan_id (False, int, None)
    (Required for new resource)


  tags (False, list, None)
    None


  location (False, str, None)
    None


  primary_ip (False, str, None)
    None


  username (False, str, None)
    None


  password (False, str, None)
    None


  firewall_type (False, str, HARDWARE_FIREWALL_DEDICATED)
    None


  ha_enabled (False, bool, False)
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

