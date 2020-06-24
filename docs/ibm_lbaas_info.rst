
ibm_lbaas_info -- Retrieve IBM Cloud 'ibm_lbaas' resource
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_lbaas' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.8.0
- Terraform v0.12.20



Parameters
----------

  description (False, str, None)
    None


  status (False, str, None)
    None


  server_instances_up (False, int, None)
    None


  active_connections (False, int, None)
    None


  protocols (False, list, None)
    None


  datacenter (False, str, None)
    None


  server_instances_down (False, int, None)
    None


  vip (False, str, None)
    None


  use_system_public_ip_pool (False, bool, None)
    None


  ssl_ciphers (False, list, None)
    None


  server_instances (False, list, None)
    None


  name (True, str, None)
    None


  type (False, str, None)
    None


  health_monitors (False, list, None)
    None


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

