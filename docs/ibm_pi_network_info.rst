
ibm_pi_network_info -- Retrieve IBM Cloud 'ibm_pi_network' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_pi_network' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  pi_network_name (True, str, None)
    Network Name to be used for pvminstances


  pi_cloud_instance_id (True, str, None)
    None


  vlan_id (False, int, None)
    None


  available_ip_count (False, float, None)
    None


  used_ip_count (False, float, None)
    None


  used_ip_percent (False, float, None)
    None


  cidr (False, str, None)
    None


  type (False, str, None)
    None


  gateway (False, str, None)
    None


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

