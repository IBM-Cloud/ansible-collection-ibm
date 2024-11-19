
ibm_is_snapshot_consistency_group_info -- Retrieve IBM Cloud 'ibm_is_snapshot_consistency_group' resource
=========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_snapshot_consistency_group' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_snapshot_consistency_group

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  name (False, str, None)
    The name for this snapshot consistency group. The name is unique across all snapshot consistency groups in the region.


  tags (False, list, None)
    Snapshot Consistency Group tags list


  access_tags (False, list, None)
    List of access management tags


  identifier (False, str, None)
    The snapshot consistency group identifier.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

