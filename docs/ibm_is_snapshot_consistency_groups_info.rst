
ibm_is_snapshot_consistency_groups_info -- Retrieve IBM Cloud 'ibm_is_snapshot_consistency_groups' resource
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_snapshot_consistency_groups' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_snapshot_consistency_groups

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  resource_group (False, str, None)
    Filters the collection to resources with a `resource_group.id` property matching the specified identifier.


  name (False, str, None)
    Filters the collection to resources with a `name` property matching the exact specified name.


  backup_policy_plan (False, str, None)
    Filters the collection to backup policy jobs with a `backup_policy_plan.id` property matching the specified identifier.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

