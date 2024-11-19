
ibm_dl_gateway -- Configure IBM Cloud 'ibm_dl_gateway' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dl_gateway' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/dl_gateway

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  authentication_key (False, str, None)
    BGP MD5 authentication key


  customer_name (False, str, None)
    Customer name


  speed_mbps (True, int, None)
    (Required for new resource) Gateway speed in megabits per second


  bgp_cer_cidr (False, str, None)
    BGP customer edge router CIDR


  as_prepends (False, list, None)
    List of AS Prepend configuration information


  bfd_multiplier (False, int, None)
    BFD Multiplier


  global_ (True, bool, None)
    (Required for new resource) Gateways with global routing (true) can connect to networks outside their associated region


  type (True, str, None)
    (Required for new resource) Gateway type


  vlan (False, int, None)
    VLAN allocated for this gateway


  cross_connect_router (False, str, None)
    Cross connect router


  name (True, str, None)
    (Required for new resource) The unique user-defined name for this gateway


  bgp_asn (True, int, None)
    (Required for new resource) BGP ASN


  port (False, str, None)
    Gateway port


  loa_reject_reason (False, str, None)
    Loa reject reason


  resource_group (False, str, None)
    Gateway resource group


  tags (False, list, None)
    Tags for the direct link gateway


  bfd_interval (False, int, None)
    BFD Interval


  bgp_base_cidr (False, str, None)
    BGP base CIDR


  location_name (False, str, None)
    Gateway location


  metered (True, bool, None)
    (Required for new resource) Metered billing option


  import_route_filters (False, list, None)
    List Import Route Filters for a Direct Link gateway


  bfd_status (False, str, None)
    Gateway BFD status


  bfd_status_updated_at (False, str, None)
    Date and time BFD status was updated


  remove_vlan (False, bool, False)
    Remove VLAN allocated for this dedicated gateway


  export_route_filters (False, list, None)
    List Export Route Filters for a Direct Link gateway


  default_export_route_filter (False, str, None)
    The default directional route filter action that applies to routes that do not match any directional route filters


  default_import_route_filter (False, str, None)
    The default directional route filter action that applies to routes that do not match any directional route filters


  connection_mode (False, str, None)
    Type of services this Gateway is attached to. Mode transit means this Gateway will be attached to Transit Gateway Service and direct means this Gateway will be attached to vpc or classic connection


  carrier_name (False, str, None)
    Carrier name


  macsec_config (False, list, None)
    MACsec configuration information


  bgp_ibm_cidr (False, str, None)
    BGP IBM CIDR


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

