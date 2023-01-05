
ibm_is_network_acl_rule -- Configure IBM Cloud 'ibm_is_network_acl_rule' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_network_acl_rule' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_network_acl_rule

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.47.1
- Terraform v0.12.20



Parameters
----------

  network_acl (True, str, None)
    (Required for new resource) Network ACL id


  direction (True, str, None)
    (Required for new resource) Direction of traffic to enforce, either inbound or outbound


  tcp (False, list, None)
    None


  udp (False, list, None)
    None


  action (True, str, None)
    (Required for new resource) Whether to allow or deny matching traffic


  source (True, str, None)
    (Required for new resource) The source CIDR block. The CIDR block 0.0.0.0/0 applies to all addresses.


  icmp (False, list, None)
    None


  destination (True, str, None)
    (Required for new resource) The destination CIDR block. The CIDR block 0.0.0.0/0 applies to all addresses.


  before (False, str, None)
    The rule that this rule is immediately before. If absent, this is the last rule.


  name (False, str, None)
    The user-defined name for this rule. Names must be unique within the network ACL the rule resides in. If unspecified, the name will be a hyphenated list of randomly-selected words.


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

