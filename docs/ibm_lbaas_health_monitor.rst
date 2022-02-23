
ibm_lbaas_health_monitor -- Configure IBM Cloud 'ibm_lbaas_health_monitor' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lbaas_health_monitor' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/lbaas_health_monitor

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.38.2
- Terraform v0.12.20



Parameters
----------

  port (True, int, None)
    (Required for new resource) Port number


  interval (False, int, 5)
    Interval value


  max_retries (False, int, 2)
    Maximum retry counts


  timeout (False, int, 2)
    Timeout in seconds


  url_path (False, str, /)
    URL Path


  monitor_id (True, str, None)
    (Required for new resource) Monitor ID


  lbaas_id (True, str, None)
    (Required for new resource) LBAAS id


  protocol (True, str, None)
    (Required for new resource) Protocol value


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

