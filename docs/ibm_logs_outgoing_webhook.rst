
ibm_logs_outgoing_webhook -- Configure IBM Cloud 'ibm_logs_outgoing_webhook' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_logs_outgoing_webhook' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/logs_outgoing_webhook

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  url (False, str, None)
    The URL of the outbound webhook.


  name (True, str, None)
    (Required for new resource) The name of the outbound webhook.


  ibm_event_notifications (False, list, None)
    The configuration of an IBM Event Notifications outbound webhook.


  instance_id (True, str, None)
    (Required for new resource) The ID of the logs instance.


  endpoint_type (False, str, None)
    public or private.


  type (True, str, None)
    (Required for new resource) Outbound webhook type.


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

