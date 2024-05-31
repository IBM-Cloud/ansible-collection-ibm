
ibm_en_destination_safari -- Configure IBM Cloud 'ibm_en_destination_safari' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_en_destination_safari' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/en_destination_safari

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.65.1
- Terraform v1.5.5



Parameters
----------

  icon_32x32 (False, str, None)
    The Certificate File.


  icon_128x128 (False, str, None)
    The Certificate File.


  icon_128x128_2x (False, str, None)
    The Certificate File.


  icon_128x128_content_type (False, str, None)
    The Certificate File.


  config (False, list, None)
    Payload describing a destination configuration.


  description (False, str, None)
    The Destination description.


  certificate (True, str, None)
    (Required for new resource) The Certificate File.


  icon_16x16 (False, str, None)
    The Certificate File.


  icon_32x32_content_type (False, str, None)
    The Certificate File.


  icon_128x128_2x_content_type (False, str, None)
    The Certificate File.


  name (True, str, None)
    (Required for new resource) The Destintion name.


  icon_16x16_content_type (False, str, None)
    The Certificate File.


  icon_16x16_2x_content_type (False, str, None)
    The Certificate File.


  icon_32x32_2x_content_type (False, str, None)
    The Certificate File.


  icon_32x32_2x (False, str, None)
    The Certificate File.


  type (True, str, None)
    (Required for new resource) The type of Destination type push_ios.


  collect_failed_events (False, bool, None)
    Whether to collect the failed event in Cloud Object Storage bucket


  icon_16x16_2x (False, str, None)
    The Certificate File.


  instance_guid (True, str, None)
    (Required for new resource) Unique identifier for IBM Cloud Event Notifications instance.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


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

