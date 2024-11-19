
ibm_is_bare_metal_server_network_interface_floating_ip -- Configure IBM Cloud 'ibm_is_bare_metal_server_network_interface_floating_ip' resource
===============================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_bare_metal_server_network_interface_floating_ip' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_bare_metal_server_network_interface_floating_ip

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  network_interface (True, str, None)
    (Required for new resource) Bare metal server network interface identifier


  floating_ip (True, str, None)
    (Required for new resource) The floating ip identifier of the network interface associated with the bare metal server


  bare_metal_server (True, str, None)
    (Required for new resource) Bare metal server identifier


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

