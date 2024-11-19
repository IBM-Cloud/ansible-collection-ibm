
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

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  tcp (False, list, None)
    None


  name (False, str, None)
    The user-defined name for this rule. Names must be unique within the network ACL the rule resides in. If unspecified, the name will be a hyphenated list of randomly-selected words.


  source (True, str, None)
    (Required for new resource) The source CIDR block. The CIDR block 0.0.0.0/0 applies to all addresses.


  destination (True, str, None)
    (Required for new resource) The destination CIDR block. The CIDR block 0.0.0.0/0 applies to all addresses.


  icmp (False, list, None)
    None


  udp (False, list, None)
    None


  network_acl (True, str, None)
    (Required for new resource) Network ACL id


  action (True, str, None)
    (Required for new resource) Whether to allow or deny matching traffic


  before (False, str, None)
    The rule that this rule is immediately before. If absent, this is the last rule.


  direction (True, str, None)
    (Required for new resource) Direction of traffic to enforce, either inbound or outbound


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

