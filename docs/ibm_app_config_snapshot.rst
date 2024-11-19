
ibm_app_config_snapshot -- Configure IBM Cloud 'ibm_app_config_snapshot' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_app_config_snapshot' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/app_config_snapshot

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  git_config_id (True, str, None)
    (Required for new resource) Git config id. Allowed special characters are dot ( . ), hyphen( - ), underscore ( _ ) only


  git_token (True, str, None)
    (Required for new resource) Git token, this needs to be provided with enough permission to write and update the file.


  git_config_name (True, str, None)
    (Required for new resource) Git config name. Allowed special characters are dot ( . ), hyphen( - ), underscore ( _ ) only


  git_branch (True, str, None)
    (Required for new resource) Branch name to which you need to write or update the configuration.


  action (False, str, None)
    action promote


  guid (True, str, None)
    (Required for new resource) GUID of the App Configuration service. Get it from the service instance credentials section of the dashboard.


  environment_id (True, str, None)
    (Required for new resource) Environment id.


  git_url (True, str, None)
    (Required for new resource) Git url which will be used to connect to the github account.


  git_file_path (True, str, None)
    (Required for new resource) Git file path, this is a path where your configuration file will be written.


  collection_id (True, str, None)
    (Required for new resource) Collection id.


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

