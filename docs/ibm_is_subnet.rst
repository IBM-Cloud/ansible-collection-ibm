
ibm_is_subnet -- Configure IBM Cloud 'ibm_is_subnet' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_subnet' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_subnet

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  tags (False, list, None)
    List of tags


  network_acl (False, str, None)
    The network ACL for this subnet


  resource_group (False, str, None)
    The resource group for this subnet


  ip_version (False, str, ipv4)
    The IP version(s) to support for this subnet.


  access_tags (False, list, None)
    List of access management tags


  zone (True, str, None)
    (Required for new resource) Subnet zone info


  routing_table_crn (False, str, None)
    routing table crn that is associated with the subnet.


  ipv4_cidr_block (False, str, None)
    IPV4 subnet - CIDR block


  total_ipv4_address_count (False, int, None)
    The total number of IPv4 addresses in this subnet.


  public_gateway (False, str, None)
    Public Gateway of the subnet


  name (True, str, None)
    (Required for new resource) Subnet name


  vpc (True, str, None)
    (Required for new resource) VPC instance ID


  routing_table (False, str, None)
    routing table id that is associated with the subnet


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

