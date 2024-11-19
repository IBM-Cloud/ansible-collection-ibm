
ibm_dl_provider_gateway -- Configure IBM Cloud 'ibm_dl_provider_gateway' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dl_provider_gateway' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/dl_provider_gateway

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  bgp_asn (True, int, None)
    (Required for new resource) BGP ASN


  speed_mbps (True, int, None)
    (Required for new resource) Gateway speed in megabits per second


  tags (False, list, None)
    Tags for the direct link gateway


  bgp_ibm_cidr (False, str, None)
    BGP IBM CIDR


  customer_account_id (True, str, None)
    (Required for new resource) Customer IBM Cloud account ID for the new gateway. A gateway object containing the pending create request will become available in the specified account.


  vlan (False, int, None)
    VLAN allocated for this gateway


  name (True, str, None)
    (Required for new resource) The unique user-defined name for this gateway


  bgp_cer_cidr (False, str, None)
    BGP customer edge router CIDR


  port (True, str, None)
    (Required for new resource) Gateway port


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

