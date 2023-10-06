
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

- IBM-Cloud terraform-provider-ibm v1.50.0
- Terraform v0.12.20



Parameters
----------

  resource_group (False, str, None)
    Filters the snapshot collection by resources group id


  name (False, str, None)
    Filters the snapshot collection by snapshot name


  source_image (False, str, None)
    Filters the snapshot collection by source image id


  source_volume (False, str, None)
    Filters the snapshot collection by source volume id


  backup_policy_plan_id (False, str, None)
    Filters the collection to backup policy jobs with the backup plan with the specified identifier


  tag (False, str, None)
    Filters the collection to resources with the exact tag value


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

