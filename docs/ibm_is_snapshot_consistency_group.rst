
ibm_is_snapshot_consistency_group -- Configure IBM Cloud 'ibm_is_snapshot_consistency_group' resource
=====================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_snapshot_consistency_group' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_snapshot_consistency_group

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  access_tags (False, list, None)
    List of access management tags


  name (True, str, None)
    (Required for new resource) The name for this snapshot consistency group. The name is unique across all snapshot consistency groups in the region.


  tags (False, list, None)
    Snapshot Consistency Group tags list


  delete_snapshots_on_delete (False, bool, True)
    Indicates whether deleting the snapshot consistency group will also delete the snapshots in the group.


  snapshots (True, list, None)
    (Required for new resource) The member snapshots that are data-consistent with respect to captured time. (may be[deleted](https://cloud.ibm.com/apidocs/vpc#deleted-resources)).


  resource_group (False, str, None)
    Resource group Id


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

