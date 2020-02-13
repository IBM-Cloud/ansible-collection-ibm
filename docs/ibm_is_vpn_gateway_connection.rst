
ibm_is_vpn_gateway_connection -- Configure IBM Cloud 'ibm_is_vpn_gateway_connection' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_vpn_gateway_connection' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  vpn_gateway (False, str, None)
    (Required for new resource)


  peer_address (False, str, None)
    (Required for new resource)


  peer_cidrs (False, list, None)
    None


  action (False, str, none)
    None


  ike_policy (False, str, None)
    None


  status (False, str, None)
    None


  name (False, str, None)
    (Required for new resource)


  admin_state_up (False, bool, False)
    None


  local_cidrs (False, list, None)
    None


  interval (False, int, 30)
    None


  timeout (False, int, 120)
    None


  ipsec_policy (False, str, None)
    None


  preshared_key (False, str, None)
    (Required for new resource)


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, any, 2)
    IBM Cloud infrastructure generation.


  ibmcloud_api_key (False, any, None)
    (Required when generation = 2) The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environmental variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environmental variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

