
ibm_is_virtual_network_interface_floating_ip_info -- Retrieve IBM Cloud 'ibm_is_virtual_network_interface_floating_ip' resource
===============================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_virtual_network_interface_floating_ip' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_virtual_network_interface_floating_ip

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  deleted (False, list, None)
    If present, this property indicates the referenced resource has been deleted, and provides some supplementary information.


  virtual_network_interface (True, str, None)
    The virtual network interface identifier


  floating_ip (True, str, None)
    The floating IP identifier


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

