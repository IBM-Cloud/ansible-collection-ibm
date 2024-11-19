
ibm_is_vpn_gateway -- Configure IBM Cloud 'ibm_is_vpn_gateway' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_vpn_gateway' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_vpn_gateway

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  tags (False, list, None)
    VPN Gateway tags list


  access_tags (False, list, None)
    List of access management tags


  subnet (True, str, None)
    (Required for new resource) VPNGateway subnet info


  name (True, str, None)
    (Required for new resource) VPN Gateway instance name


  mode (False, str, route)
    mode in VPN gateway(route/policy)


  resource_group (False, str, None)
    The resource group for this VPN gateway


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

