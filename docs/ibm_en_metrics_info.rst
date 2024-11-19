
ibm_en_metrics_info -- Retrieve IBM Cloud 'ibm_en_metrics' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_en_metrics' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/en_metrics

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  instance_id (True, str, None)
    Unique identifier for IBM Cloud Event Notifications instance.


  destination_type (True, str, None)
    Destination type. Allowed values are [smtp_custom].


  destination_id (False, str, None)
    Unique identifier for Destination.


  source_id (False, str, None)
    Unique identifier for Source.


  email_to (False, str, None)
    Receiver email id.


  notification_id (False, str, None)
    Notification Id.


  gte (True, str, None)
    GTE (greater than equal), start timestamp in UTC.


  lte (True, str, None)
    LTE (less than equal), end timestamp in UTC.


  subject (False, str, None)
    Email subject.


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

