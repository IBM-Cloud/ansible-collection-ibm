
ibm_is_vpn_gateway_connection_info -- Retrieve IBM Cloud 'ibm_is_vpn_gateway_connection' resource
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_vpn_gateway_connection' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_vpn_gateway_connection

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  vpn_gateway (False, str, None)
    The VPN gateway identifier.


  vpn_gateway_name (False, str, None)
    The VPN gateway name.


  vpn_gateway_connection (False, str, None)
    The VPN gateway connection identifier.


  vpn_gateway_connection_name (False, str, None)
    The VPN gateway connection name.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

