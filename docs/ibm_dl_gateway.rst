
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

- IBM-Cloud terraform-provider-ibm v1.25.0
- Terraform v0.12.20



Parameters
----------

  type (True, str, None)
    (Required for new resource) Gateway type


  loa_reject_reason (False, str, None)
    Loa reject reason


  tags (False, list, None)
    Tags for the direct link gateway


  cross_connect_router (False, str, None)
    Cross connect router


  name (True, str, None)
    (Required for new resource) The unique user-defined name for this gateway


  bgp_base_cidr (False, str, None)
    BGP base CIDR


  customer_name (False, str, None)
    Customer name


  resource_group (False, str, None)
    Gateway resource group


  location_name (False, str, None)
    Gateway location


  speed_mbps (True, int, None)
    (Required for new resource) Gateway speed in megabits per second


  bgp_cer_cidr (False, str, None)
    BGP customer edge router CIDR


  bgp_asn (True, int, None)
    (Required for new resource) BGP ASN


  metered (True, bool, None)
    (Required for new resource) Metered billing option


  global_ (True, bool, None)
    (Required for new resource) Gateways with global routing (true) can connect to networks outside their associated region


  bgp_ibm_cidr (False, str, None)
    BGP IBM CIDR


  macsec_config (False, list, None)
    MACsec configuration information


  port (False, str, None)
    Gateway port


  carrier_name (False, str, None)
    Carrier name


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

