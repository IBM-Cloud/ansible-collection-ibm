
ibm_satellite_storage_configuration -- Configure IBM Cloud 'ibm_satellite_storage_configuration' resource
=========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_satellite_storage_configuration' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/satellite_storage_configuration

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  location (True, str, None)
    (Required for new resource) Location ID.


  storage_template_name (True, str, None)
    (Required for new resource) The Storage Template Name.


  storage_class_parameters (False, list, None)
    None


  update_assignments (False, bool, False)
    Set to update all assignments during a configuration update.


  user_secret_parameters (True, dict, None)
    (Required for new resource) User Secret Parameters to pass as a Map of string key-value.


  delete_assignments (False, bool, False)
    Set to delete all assignments during a configuration destroy.


  config_name (True, str, None)
    (Required for new resource) Name of the Storage Configuration.


  storage_template_version (True, str, None)
    (Required for new resource) The Storage Template Version.


  user_config_parameters (True, dict, None)
    (Required for new resource) User Config Parameters to pass as a Map of string key-value.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


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

