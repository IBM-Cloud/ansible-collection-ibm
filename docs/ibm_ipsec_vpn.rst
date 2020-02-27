
ibm_ipsec_vpn -- Configure IBM Cloud 'ibm_ipsec_vpn' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_ipsec_vpn' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.2
- Terraform v0.12.20



Parameters
----------

  remote_subnet (False, list, None)
    None


  datacenter (False, str, None)
    (Required for new resource)


  internal_peer_ip_address (False, str, None)
    None


  phase_one (False, list, None)
    None


  phase_two (False, list, None)
    None


  address_translation (False, list, None)
    None


  internal_subnet_id (False, int, None)
    None


  remote_subnet_id (False, int, None)
    None


  name (False, str, None)
    None


  preshared_key (False, str, None)
    None


  customer_peer_ip (False, str, None)
    None


  service_subnet_id (False, int, None)
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

