
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

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  admin_state_up (False, bool, False)
    NA


  action (False, str, none)
    NA


  ipsec_policy (False, str, None)
    NA


  ike_policy (False, str, None)
    NA


  name (False, str, None)
    (Required for new resource) NA


  peer_address (False, str, None)
    (Required for new resource) NA


  preshared_key (False, str, None)
    (Required for new resource) NA


  local_cidrs (False, list, None)
    NA


  peer_cidrs (False, list, None)
    NA


  interval (False, int, 30)
    NA


  timeout (False, int, 120)
    NA


  status (False, str, None)
    NA


  vpn_gateway (False, str, None)
    (Required for new resource) NA


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, any, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

