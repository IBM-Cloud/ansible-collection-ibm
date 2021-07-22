
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

- IBM-Cloud terraform-provider-ibm v1.27.2
- Terraform v0.12.20



Parameters
----------

  name (True, str, None)
    (Required for new resource) VPC name


  default_routing_table_name (False, str, None)
    Default routing table name


  resource_group (False, str, None)
    Resource group info


  default_security_group_name (False, str, None)
    Default security group name


  classic_access (False, bool, False)
    Set to true if classic access needs to enabled to VPC


  tags (False, list, None)
    List of tags


  address_prefix_management (False, str, auto)
    Address Prefix management value


  default_network_acl_name (False, str, None)
    Default Network ACL name


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

