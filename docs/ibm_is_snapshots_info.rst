
ibm_is_snapshots_info -- Retrieve IBM Cloud 'ibm_is_snapshots' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_snapshots' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_snapshots

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  resource_group (False, str, None)
    Filters the snapshot collection by resources group id


  source_volume (False, str, None)
    Filters the snapshot collection by source volume id


  tag (False, str, None)
    Filters the collection to resources with the exact tag value


  snapshot_copies_name (False, str, None)
    Filters the collection to snapshots with copies with the exact specified name.


  source_snapshot_remote_region_name (False, str, None)
    Filters the collection to snapshots with a source snapshot with the exact remote region name.


  snapshot_copies_id (False, str, None)
    Filters the collection to snapshots with copies with the specified identifier.


  source_image (False, str, None)
    Filters the snapshot collection by source image id


  backup_policy_plan_id (False, str, None)
    Filters the collection to backup policy jobs with the backup plan with the specified identifier


  source_snapshot_id (False, str, None)
    Filters the collection to resources with the source snapshot with the specified identifier.


  snapshot_source_volume_remote_region_name (False, str, None)
    Filters the collection to snapshots with a source snapshot with the exact remote region name.


  snapshot_consistency_group_crn (False, str, None)
    Filters the collection to resources with a source snapshot with the exact snapshot consistency group crn.


  name (False, str, None)
    Filters the snapshot collection by snapshot name


  snapshot_copies_crn (False, str, None)
    Filters the collection to snapshots with copies with the specified CRN.


  snapshot_copies_remote_region_name (False, str, None)
    Filters the collection to snapshots with copies with the exact remote region name.


  snapshot_consistency_group_id (False, str, None)
    Filters the collection to resources with a source snapshot with the exact snapshot consistency group id.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

