
ibm_cis_mtls_app -- Configure IBM Cloud 'ibm_cis_mtls_app' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_mtls_app' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cis_mtls_app

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.65.1
- Terraform v1.5.5



Parameters
----------

  session_duration (False, str, 24h)
    Duration for app validatidity


  cert_rule_val (False, str, CA root certificate)
    Policy certificate rule value


  domain_id (True, str, None)
    (Required for new resource) Associated CIS domain


  policy_name (False, str, mtls-policy)
    Policy Name


  cis_id (True, str, None)
    (Required for new resource) CIS instance crn


  domain (True, str, None)
    (Required for new resource) Associated host domain value


  policy_decision (False, str, non_identity)
    Policy Action


  name (True, str, None)
    (Required for new resource) App Name


  common_rule_val (False, str, None)
    Policy common rule value


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

