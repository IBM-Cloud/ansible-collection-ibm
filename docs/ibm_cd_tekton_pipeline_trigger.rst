
ibm_cd_tekton_pipeline_trigger -- Configure IBM Cloud 'ibm_cd_tekton_pipeline_trigger' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cd_tekton_pipeline_trigger' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cd_tekton_pipeline_trigger

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.47.1
- Terraform v0.12.20



Parameters
----------

  event_listener (True, str, None)
    (Required for new resource) Event listener name. The name of the event listener to which the trigger is associated. The event listeners are defined in the definition repositories of the Tekton pipeline.


  max_concurrent_runs (False, int, None)
    Defines the maximum number of concurrent runs for this trigger. Omit this property to disable the concurrency limit.


  timezone (False, str, None)
    Only needed for timer triggers. Timezone for timer trigger.


  scm_source (False, list, None)
    SCM source repository for a Git trigger. Only needed for Git triggers.


  events (False, list, None)
    Only needed for Git triggers. Events object defines the events to which this Git trigger listens.


  name (True, str, None)
    (Required for new resource) Trigger name.


  disabled (False, bool, None)
    Flag whether the trigger is disabled. If omitted the trigger is enabled by default.


  worker (False, list, None)
    Worker used to run the trigger. If not specified the trigger will use the default pipeline worker.


  cron (False, str, None)
    Only needed for timer triggers. Cron expression for timer trigger.


  tags (False, list, None)
    Trigger tags array.


  secret (False, list, None)
    Only needed for generic webhook trigger type. Secret used to start generic webhook trigger.


  pipeline_id (True, str, None)
    (Required for new resource) The Tekton pipeline ID.


  type (True, str, None)
    (Required for new resource) Trigger type.


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

