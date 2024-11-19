
ibm_is_backup_policy_plan -- Configure IBM Cloud 'ibm_is_backup_policy_plan' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_backup_policy_plan' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_backup_policy_plan

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  backup_policy_id (True, str, None)
    (Required for new resource) The backup policy identifier.


  name (False, str, None)
    The user-defined name for this backup policy plan. Names must be unique within the backup policy this plan resides in. If unspecified, the name will be a hyphenated list of randomly-selected words.


  attach_user_tags (False, list, None)
    User tags to attach to each backup (snapshot) created by this plan. If unspecified, no user tags will be attached.


  deletion_trigger (False, list, None)
    None


  active (False, bool, None)
    Indicates whether the plan is active.


  clone_policy (False, list, None)
    None


  remote_region_policy (False, list, None)
    Backup policy plan cross region rule.


  cron_spec (True, str, None)
    (Required for new resource) The cron specification for the backup schedule.


  copy_user_tags (False, bool, True)
    Indicates whether to copy the source's user tags to the created backups (snapshots).


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

