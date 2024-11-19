
ibm_is_backup_policy_jobs_info -- Retrieve IBM Cloud 'ibm_is_backup_policy_jobs' resource
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_backup_policy_jobs' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_backup_policy_jobs

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  target_snapshots_crn (False, list, None)
    Filters the collection to backup policy jobs with the target snapshot with the specified CRN


  backup_policy_plan_id (False, str, None)
    Filters the collection to backup policy jobs with the backup plan with the specified identifier.


  status (False, str, None)
    Filters the collection to backup policy jobs with the specified status


  backup_policy_id (True, str, None)
    The backup policy identifier.


  source_id (False, str, None)
    Filters the collection to backup policy jobs with a source with the specified identifier


  target_snapshots_id (False, list, None)
    Filters the collection to resources with the target snapshot with the specified identifier


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

