
ibm_is_snapshot -- Configure IBM Cloud 'ibm_is_snapshot' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_snapshot' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_snapshot

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  source_snapshot_crn (False, str, None)
    Source Snapshot CRN


  resource_group (False, str, None)
    Resource group info


  tags (False, list, None)
    User Tags for the snapshot


  clones (False, list, None)
    Zones for creating the snapshot clone


  name (False, str, None)
    Snapshot name


  encryption_key (False, str, None)
    A reference to the root key used to wrap the data encryption key for the source volume.


  source_volume (False, str, None)
    Snapshot source volume


  access_tags (False, list, None)
    List of access management tags


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

