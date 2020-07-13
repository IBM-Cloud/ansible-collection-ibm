
ibm_dl_port_info -- Retrieve IBM Cloud 'ibm_dl_port' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_dl_port' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  location_name (False, str, None)
    Port location name identifier


  provider_name (False, str, None)
    Port's provider name


  supported_link_speeds (False, list, None)
    Port's supported speeds in megabits per second


  port_id (True, str, None)
    Port ID


  direct_link_count (False, int, None)
    Count of existing Direct Link gateways in this account on this port


  label (False, str, None)
    Port Label


  location_display_name (False, str, None)
    Port location long name


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

