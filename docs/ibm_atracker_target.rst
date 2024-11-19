
ibm_atracker_target -- Configure IBM Cloud 'ibm_atracker_target' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_atracker_target' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/atracker_target

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  cos_endpoint (False, list, None)
    Property values for a Cloud Object Storage Endpoint.


  eventstreams_endpoint (False, list, None)
    Property values for an Event Streams Endpoint in requests.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  target_type (True, str, None)
    (Required for new resource) The type of the target. It can be cloud_object_storage, logdna, event_streams, or cloud_logs. Based on this type you must include cos_endpoint, logdna_endpoint, eventstreams_endpoint or cloudlogs_endpoint.


  name (True, str, None)
    (Required for new resource) The name of the target. The name must be 1000 characters or less, and cannot include any special characters other than `(space) - . _ :`.


  logdna_endpoint (False, list, None)
    Property values for a LogDNA Endpoint.


  cloudlogs_endpoint (False, list, None)
    Property values for an IBM Cloud Logs endpoint in requests.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

