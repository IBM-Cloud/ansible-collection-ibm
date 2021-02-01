
ibm_is_subnet -- Configure IBM Cloud 'ibm_is_subnet' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_subnet' resource

This module supports idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.20.0
- Terraform v0.12.20



Parameters
----------

  network_acl (False, str, None)
    The network ACL for this subnet


  total_ipv4_address_count (False, int, None)
    The total number of IPv4 addresses in this subnet.


  name (True, str, None)
    (Required for new resource) Subnet name


  ipv4_cidr_block (False, str, None)
    IPV4 subnet - CIDR block


  vpc (True, str, None)
    (Required for new resource) VPC instance ID


  ip_version (False, str, ipv4)
    The IP version(s) to support for this subnet.


  public_gateway (False, str, None)
    Public Gateway of the subnet


  zone (True, str, None)
    (Required for new resource) Subnet zone info


  resource_group (False, str, None)
    The resource group for this subnet


  routing_table (False, str, None)
    routing table id that is associated with the subnet


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

