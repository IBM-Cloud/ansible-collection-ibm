
ibm_pi_vpn_connection -- Configure IBM Cloud 'ibm_pi_vpn_connection' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_vpn_connection' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_vpn_connection

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  pi_cloud_instance_id (True, str, None)
    (Required for new resource) PI cloud instance ID


  pi_vpn_connection_name (True, str, None)
    (Required for new resource) Name of the VPN Connection


  pi_ike_policy_id (True, str, None)
    (Required for new resource) Unique identifier of IKE Policy selected for this VPN Connection


  pi_vpn_connection_mode (True, str, None)
    (Required for new resource) Mode used by this VPN Connection, either 'policy' or 'route'


  pi_ipsec_policy_id (True, str, None)
    (Required for new resource) Unique identifier of IPSec Policy selected for this VPN Connection


  pi_networks (True, list, None)
    (Required for new resource) Set of network IDs to attach to this VPN connection


  pi_peer_gateway_address (True, str, None)
    (Required for new resource) Peer Gateway address


  pi_peer_subnets (True, list, None)
    (Required for new resource) Set of CIDR of peer subnets


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  zone (False, str, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environment variable 'IC_ZONE'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

