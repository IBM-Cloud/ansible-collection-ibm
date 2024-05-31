
ibm_is_vpn_gateway_connection -- Configure IBM Cloud 'ibm_is_vpn_gateway_connection' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_vpn_gateway_connection' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_vpn_gateway_connection

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.65.1
- Terraform v1.5.5



Parameters
----------

  ipsec_policy (False, str, None)
    IP security policy for vpn gateway connection


  ike_policy (False, str, None)
    VPN gateway connection IKE Policy


  name (True, str, None)
    (Required for new resource) VPN Gateway connection name


  peer_address (True, str, None)
    (Required for new resource) VPN gateway connection peer address


  local_cidrs (False, list, None)
    VPN gateway connection local CIDRs


  peer_cidrs (False, list, None)
    VPN gateway connection peer CIDRs


  vpn_gateway (True, str, None)
    (Required for new resource) VPN Gateway info


  preshared_key (True, str, None)
    (Required for new resource) vpn gateway


  admin_state_up (False, bool, False)
    VPN gateway connection admin state


  action (False, str, restart)
    Action detection for dead peer detection action


  interval (False, int, 2)
    Interval for dead peer detection interval


  timeout (False, int, 10)
    Timeout for dead peer detection


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

