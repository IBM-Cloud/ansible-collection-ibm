
ibm_dl_gateway_action -- Configure IBM Cloud 'ibm_dl_gateway_action' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dl_gateway_action' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/dl_gateway_action

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  customer_name (False, str, None)
    Customer name


  speed_mbps (False, int, None)
    Gateway speed in megabits per second


  bgp_asn (False, int, None)
    BGP ASN


  cross_connect_router (False, str, None)
    Cross connect router


  gateway (True, str, None)
    (Required for new resource) The Direct Link gateway identifier


  metered (False, bool, None)
    Metered billing option


  bgp_base_cidr (False, str, None)
    BGP base CIDR


  carrier_name (False, str, None)
    Carrier name


  resource_group (False, str, None)
    Gateway resource group


  authentication_key (False, str, None)
    BGP MD5 authentication key


  bfd_interval (False, int, None)
    BFD Interval


  name (False, str, None)
    The unique user-defined name for this gateway


  loa_reject_reason (False, str, None)
    Loa reject reason


  action (True, str, None)
    (Required for new resource) customer action on provider call


  global_ (False, bool, None)
    Gateways with global routing (true) can connect to networks outside their associated region


  location_name (False, str, None)
    Gateway location


  type (False, str, None)
    Gateway type


  bgp_cer_cidr (False, str, None)
    BGP customer edge router CIDR


  default_export_route_filter (False, str, None)
    The default directional route filter action that applies to routes that do not match any directional route filters


  default_import_route_filter (False, str, None)
    The default directional route filter action that applies to routes that do not match any directional route filters


  as_prepends (False, list, None)
    List of AS Prepend configuration information


  bfd_multiplier (False, int, None)
    BFD Multiplier


  connection_mode (False, str, None)
    Type of services this Gateway is attached to. Mode transit means this Gateway will be attached to Transit Gateway Service and direct means this Gateway will be attached to vpc or classic connection


  bgp_ibm_cidr (False, str, None)
    BGP IBM CIDR


  export_route_filters (False, list, None)
    List Export Route Filters for a Direct Link gateway


  import_route_filters (False, list, None)
    List Import Route Filters for a Direct Link gateway


  port (False, str, None)
    Gateway port


  tags (False, list, None)
    Tags for the direct link gateway


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

