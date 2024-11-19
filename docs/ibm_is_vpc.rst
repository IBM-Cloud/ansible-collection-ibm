
ibm_is_vpc -- Configure IBM Cloud 'ibm_is_vpc' resource
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_vpc' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_vpc

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  no_sg_acl_rules (False, bool, False)
    Delete all rules attached with default security group and default acl


  default_security_group_name (False, str, None)
    Default security group name


  access_tags (False, list, None)
    List of access management tags


  dns (False, list, None)
    The DNS configuration for this VPC.


  default_routing_table_name (False, str, None)
    Default routing table name


  tags (False, list, None)
    List of tags


  address_prefix_management (False, str, auto)
    Address Prefix management value


  name (True, str, None)
    (Required for new resource) VPC name


  default_network_acl_name (False, str, None)
    Default Network ACL name


  resource_group (False, str, None)
    Resource group info


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

