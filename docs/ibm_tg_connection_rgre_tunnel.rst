
ibm_tg_connection_rgre_tunnel -- Configure IBM Cloud 'ibm_tg_connection_rgre_tunnel' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_tg_connection_rgre_tunnel' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/tg_connection_rgre_tunnel

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  name (True, str, None)
    (Required for new resource) The user-defined name for this tunnel connection.


  remote_bgp_asn (False, int, None)
    The remote network BGP ASN.


  network_id (False, str, None)
    The ID of the network being connected via this connection. This field is required for some types, such as 'vpc' or 'directlink' or 'power_virtual_server'. The value of this is the CRN of the VPC or direct link or power_virtual_server gateway to be connected. This field is required to be unspecified for network type 'classic', 'gre_tunnel', and 'unbound_gre_tunnel'.


  connection_id (True, str, None)
    (Required for new resource) The Transit Gateway Connection identifier


  local_gateway_ip (True, str, None)
    (Required for new resource) The local gateway IP address.


  zone (True, str, None)
    (Required for new resource) Location of GRE tunnel.


  base_network_type (False, str, None)
    The type of the base network for the RGRE. It should be i.e classic or VPC


  local_bgp_asn (False, int, None)
    The local network BGP ASN.


  gateway (True, str, None)
    (Required for new resource) The Transit Gateway identifier


  local_tunnel_ip (True, str, None)
    (Required for new resource) The local tunnel IP address.


  remote_gateway_ip (True, str, None)
    (Required for new resource) The remote gateway IP address.


  remote_tunnel_ip (True, str, None)
    (Required for new resource) The remote tunnel IP address.


  network_account_id (False, str, None)
    The ID of the account which owns the network that is being connected. Generally only used if the network is in a different account than the gateway. This field is required for type 'unbound_gre_tunnel' when the associated_network_type is 'classic' and the GRE tunnel is in a different account than the gateway.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

