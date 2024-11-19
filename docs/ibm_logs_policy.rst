
ibm_logs_policy -- Configure IBM Cloud 'ibm_logs_policy' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_logs_policy' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/logs_policy

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  description (False, str, None)
    Description of policy.


  priority (True, str, None)
    (Required for new resource) The data pipeline sources that match the policy rules will go through.


  instance_id (True, str, None)
    (Required for new resource) The ID of the logs instance.


  name (True, str, None)
    (Required for new resource) Name of policy.


  application_rule (False, list, None)
    Rule for matching with application.


  subsystem_rule (False, list, None)
    Rule for matching with application.


  log_rules (False, list, None)
    Log rules.


  archive_retention (False, list, None)
    Archive retention definition.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  endpoint_type (False, str, None)
    public or private.


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

