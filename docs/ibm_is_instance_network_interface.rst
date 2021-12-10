
ibm_is_instance_network_interface -- Configure IBM Cloud 'ibm_is_instance_network_interface' resource
=====================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_instance_network_interface' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance_network_interface

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.37.1
- Terraform v0.12.20



Parameters
----------

  floating_ip (False, str, None)
    The ID of the floating IP to attach to this network interface


  primary_ipv4_address (False, str, None)
    The primary IPv4 address. If specified, it must be an available address on the network interface's subnet. If unspecified, an available address on the subnet will be automatically selected.


  subnet (True, str, None)
    (Required for new resource) The unique identifier of the subnet.


  security_groups (False, list, None)
    None


  name (True, str, None)
    (Required for new resource) The user-defined name for this network interface. If unspecified, the name will be a hyphenated list of randomly-selected words.


  instance (True, str, None)
    (Required for new resource) The unique identifier of the instance.


  allow_ip_spoofing (False, bool, False)
    Indicates whether source IP spoofing is allowed on this interface. If false, source IP spoofing is prevented on this interface. If true, source IP spoofing is allowed on this interface.


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

