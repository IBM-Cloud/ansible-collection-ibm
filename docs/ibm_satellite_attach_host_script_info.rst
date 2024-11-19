
ibm_satellite_attach_host_script_info -- Retrieve IBM Cloud 'ibm_satellite_attach_host_script' resource
=======================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_satellite_attach_host_script' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/satellite_attach_host_script

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  host_link_agent_endpoint (False, str, None)
    The satellite link agent endpoint, required for reduced firewall attach script


  labels (False, list, None)
    List of labels for the attach host


  host_provider (False, str, None)
    None


  custom_script (False, str, None)
    The custom script that has to be appended to generated host script file


  location (True, str, None)
    A unique name for the new Satellite location


  coreos_host (False, bool, None)
    If true, returns a CoreOS ignition file for the host. Otherwise, returns a RHEL attach script


  script_dir (False, str, None)
    The directory where the satellite attach host script to be downloaded. Default is home directory


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

