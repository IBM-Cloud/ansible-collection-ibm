
ibm_logs_alert -- Configure IBM Cloud 'ibm_logs_alert' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_logs_alert' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/logs_alert

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  severity (True, str, None)
    (Required for new resource) Alert severity.


  active_when (False, list, None)
    When should the alert be active.


  instance_id (True, str, None)
    (Required for new resource) The ID of the logs instance.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  filters (True, list, None)
    (Required for new resource) Alert filters.


  meta_labels (False, list, None)
    The Meta labels to add to the alert.


  meta_labels_strings (False, list, None)
    The Meta labels to add to the alert as string with ':' separator.


  endpoint_type (False, str, None)
    public or private.


  is_active (True, bool, None)
    (Required for new resource) Alert is active.


  expiration (False, list, None)
    Alert expiration date.


  incident_settings (False, list, None)
    Incident settings, will create the incident based on this configuration.


  name (True, str, None)
    (Required for new resource) Alert name.


  description (False, str, None)
    Alert description.


  condition (True, list, None)
    (Required for new resource) Alert condition.


  notification_groups (True, list, None)
    (Required for new resource) Alert notification groups.


  notification_payload_filters (False, list, None)
    JSON keys to include in the alert notification, if left empty get the full log text in the alert notification.


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

