
ibm_is_instance_network_interface_reserved_ip_info -- Retrieve IBM Cloud 'ibm_is_instance_network_interface_reserved_ip' resource
=================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_instance_network_interface_reserved_ip' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_instance_network_interface_reserved_ip

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  instance (True, str, None)
    The instance identifier.


  reserved_ip (True, str, None)
    The reserved IP identifier.


  network_interface (True, str, None)
    The instance network interface identifier.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

