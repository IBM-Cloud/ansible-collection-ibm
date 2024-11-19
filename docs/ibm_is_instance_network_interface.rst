
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

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  primary_ip (False, list, None)
    The primary IP address to bind to the network interface. This can be specified using an existing reserved IP, or a prototype object for a new reserved IP.


  allow_ip_spoofing (False, bool, False)
    Indicates whether source IP spoofing is allowed on this interface. If false, source IP spoofing is prevented on this interface. If true, source IP spoofing is allowed on this interface.


  security_groups (False, list, None)
    None


  subnet (True, str, None)
    (Required for new resource) The unique identifier of the subnet.


  name (True, str, None)
    (Required for new resource) The user-defined name for this network interface. If unspecified, the name will be a hyphenated list of randomly-selected words.


  floating_ip (False, str, None)
    The ID of the floating IP to attach to this network interface


  instance (True, str, None)
    (Required for new resource) The unique identifier of the instance.


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

