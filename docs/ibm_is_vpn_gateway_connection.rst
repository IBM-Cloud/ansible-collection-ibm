
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

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  name (True, str, None)
    (Required for new resource) VPN Gateway connection name


  vpn_gateway (True, str, None)
    (Required for new resource) VPN Gateway info


  peer_address (True, str, None)
    (Required for new resource) VPN gateway connection peer address


  admin_state_up (False, bool, False)
    VPN gateway connection admin state


  peer_cidrs (False, list, None)
    VPN gateway connection peer CIDRs


  timeout (False, int, 120)
    Timeout for dead peer detection


  ike_policy (False, str, None)
    VPN gateway connection IKE Policy


  preshared_key (True, str, None)
    (Required for new resource) vpn gateway


  local_cidrs (False, list, None)
    VPN gateway connection local CIDRs


  action (False, str, none)
    Action detection for dead peer detection action


  interval (False, int, 30)
    Interval for dead peer detection interval


  ipsec_policy (False, str, None)
    IP security policy for vpn gateway connection


  status (False, str, None)
    VPN gateway connection status


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

