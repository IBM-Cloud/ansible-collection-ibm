
ibm_pi_public_network_info -- Retrieve IBM Cloud 'ibm_pi_public_network' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_pi_public_network' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.0
- Terraform v0.12.20



Parameters
----------

  type (False, str, None)
    None


  vlan_id (False, int, None)
    None


  pi_network_name (False, str, None)
    Network Name to be used for pvminstances


  pi_cloud_instance_id (True, str, None)
    None


  network_id (False, str, None)
    None


  name (False, str, None)
    None


  zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environment variable 'IC_ZONE'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

