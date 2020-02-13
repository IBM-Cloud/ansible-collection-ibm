
ibm_pi_instance_ip_info -- Retrieve IBM Cloud 'ibm_pi_instance_ip' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_pi_instance_ip' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  pi_cloud_instance_id (True, str, None)
    None


  pi_network_name (True, str, None)
    None


  ip (False, str, None)
    None


  external_ip (False, str, None)
    None


  pi_instance_name (True, str, None)
    Server Name to be used for pvminstances


  ipoctet (False, str, None)
    None


  macaddress (False, str, None)
    None


  network_id (False, str, None)
    None


  type (False, str, None)
    None


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

