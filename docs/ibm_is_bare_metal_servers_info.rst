
ibm_is_bare_metal_servers_info -- Retrieve IBM Cloud 'ibm_is_bare_metal_servers' resource
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_bare_metal_servers' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_bare_metal_servers

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  vpc_name (False, str, None)
    The vpc name this bare metal server is in


  name (False, str, None)
    The name of the bare metal server


  network_interfaces_subnet (False, str, None)
    The ID of the subnet of the bare metal server network interfaces


  network_interfaces_subnet_crn (False, str, None)
    The crn of the subnet of the bare metal server network interfaces


  resource_group (False, str, None)
    The unique identifier of the resource group this bare metal server belongs to


  vpc (False, str, None)
    The vpc ID this bare metal server is in


  vpc_crn (False, str, None)
    The vpc CRN this bare metal server is in


  network_interfaces_subnet_name (False, str, None)
    The name of the subnet of the bare metal server network interfaces


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

