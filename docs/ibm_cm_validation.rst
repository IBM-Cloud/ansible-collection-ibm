
ibm_cm_validation -- Configure IBM Cloud 'ibm_cm_validation' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cm_validation' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cm_validation

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.51.0
- Terraform v0.12.20



Parameters
----------

  x_auth_refresh_token (True, str, None)
    (Required for new resource) Authentication token used to submit validation job.


  override_values (False, dict, None)
    Override values during validation.


  environment_variables (False, list, None)
    Environment variables to include in the schematics workspace.


  version_locator (True, str, None)
    (Required for new resource) Version locator - the version that will be validated.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  revalidate_if_validated (False, bool, None)
    If the version should be revalidated if it is already validated.


  mark_version_consumable (False, bool, None)
    If the version should be marked as consumable or "ready to share".


  schematics (False, list, None)
    Other values to pass to the schematics workspace.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

