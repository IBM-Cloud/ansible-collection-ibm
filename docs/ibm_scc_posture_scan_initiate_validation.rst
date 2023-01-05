
ibm_scc_posture_scan_initiate_validation -- Configure IBM Cloud 'ibm_scc_posture_scan_initiate_validation' resource
===================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_scc_posture_scan_initiate_validation' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/scc_posture_scan_initiate_validation

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.47.1
- Terraform v0.12.20



Parameters
----------

  scope_id (True, str, None)
    (Required for new resource) The unique ID of the scope.


  profile_id (True, str, None)
    (Required for new resource) The unique ID of the profile.


  group_profile_id (False, str, None)
    The ID of the profile group.


  name (False, str, None)
    The name of a scheduled scan.


  description (False, str, None)
    The description of a scheduled scan.


  frequency (False, int, None)
    The frequency at which a scan is run specified in milliseconds.


  no_of_occurrences (False, int, None)
    The number of times that a scan should be run.


  end_time (False, str, None)
    The date on which a scan should stop running specified in UTC.


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

