
ibm_tg_connection -- Configure IBM Cloud 'ibm_tg_connection' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_tg_connection' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/tg_connection

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  base_connection_id (False, str, None)
    The ID of a network_type 'classic' connection a tunnel is configured over. This field only applies to network type 'gre_tunnel' connections.


  base_network_type (False, str, None)
    The type of network the unbound gre tunnel is targeting. This field is required for network type 'unbound_gre_tunnel'.


  local_tunnel_ip (False, str, None)
    The local tunnel IP address. This field only applies to network type 'gre_tunnel' and 'unbound_gre_tunnel' connections.


  remote_gateway_ip (False, str, None)
    The remote gateway IP address. This field only applies to network type 'gre_tunnel' and 'unbound_gre_tunnel' connections.


  tunnels (False, list, None)
    List of GRE tunnels for a transit gateway redundant GRE tunnel connection. This field is required for 'redundant_gre' connections


  gateway (True, str, None)
    (Required for new resource) The Transit Gateway identifier


  name (False, str, None)
    The user-defined name for this transit gateway. If unspecified, the name will be the network name (the name of the VPC in the case of network type 'vpc', and the word Classic, in the case of network type 'classic').


  local_gateway_ip (False, str, None)
    The local gateway IP address. This field only applies to network type 'gre_tunnel' and 'unbound_gre_tunnel' connections.


  zone (False, str, None)
    Location of GRE tunnel. This field only applies to network type 'gre_tunnel' and 'unbound_gre_tunnel' connections.


  network_type (True, str, None)
    (Required for new resource) Defines what type of network is connected via this connection. Allowable values (classic,directlink,vpc,gre_tunnel,unbound_gre_tunnel,power_virtual_server,redundant_gre)


  network_id (False, str, None)
    The ID of the network being connected via this connection. This field is required for some types, such as 'vpc' or 'directlink' or 'power_virtual_server'. The value of this is the CRN of the VPC or direct link or power_virtual_server gateway to be connected. This field is required to be unspecified for network type 'classic', 'gre_tunnel', and 'unbound_gre_tunnel'.


  remote_bgp_asn (False, int, None)
    The remote network BGP ASN. This field only applies to network type 'gre_tunnel' and 'unbound_gre_tunnel' connections.


  remote_tunnel_ip (False, str, None)
    The remote tunnel IP address. This field only applies to network type 'gre_tunnel' and 'unbound_gre_tunnel' connections.


  network_account_id (False, str, None)
    The ID of the account which owns the network that is being connected. Generally only used if the network is in a different account than the gateway. This field is required for type 'unbound_gre_tunnel' when the associated_network_type is 'classic' and the GRE tunnel is in a different account than the gateway.


  default_prefix_filter (False, str, None)
    Whether to permit or deny the prefix filter


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

