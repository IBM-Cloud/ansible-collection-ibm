
ibm_cis_alert -- Configure IBM Cloud 'ibm_cis_alert' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_alert' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cis_alert

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  mechanisms (True, list, None)
    (Required for new resource) Delivery mechanisms for the alert, can include an email, a webhook, or both.


  cis_id (True, str, None)
    (Required for new resource) CIS instance crn


  description (False, str, None)
    Policy Description


  enabled (True, bool, None)
    (Required for new resource) Is the alert policy active


  alert_type (True, str, None)
    (Required for new resource) Condition for the alert


  name (True, str, None)
    (Required for new resource) Policy name


  filters (False, str, None)
    Filters based on filter type


  conditions (False, str, None)
    Conditions based on filter type


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

