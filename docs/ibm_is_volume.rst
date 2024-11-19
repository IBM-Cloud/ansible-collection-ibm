
ibm_is_volume -- Configure IBM Cloud 'ibm_is_volume' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_volume' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_volume

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  profile (True, str, None)
    (Required for new resource) Volume profile name


  capacity (False, int, None)
    Volume capacity value


  resource_group (False, str, None)
    Resource group name


  access_tags (False, list, None)
    Access management tags for the volume instance


  encryption_key (False, str, None)
    Volume encryption key info


  source_snapshot_crn (False, str, None)
    The crn for this snapshot


  name (True, str, None)
    (Required for new resource) Volume name


  zone (True, str, None)
    (Required for new resource) Zone name


  iops (False, int, None)
    IOPS value for the Volume


  source_snapshot (False, str, None)
    The unique identifier for this snapshot


  delete_all_snapshots (False, bool, None)
    Deletes all snapshots created from this volume


  tags (False, list, None)
    UserTags for the volume instance


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

