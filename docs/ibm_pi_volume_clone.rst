
ibm_pi_volume_clone -- Configure IBM Cloud 'ibm_pi_volume_clone' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_volume_clone' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_volume_clone

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  pi_target_storage_tier (False, str, None)
    The storage tier for the cloned volume(s).


  pi_replication_enabled (False, bool, None)
    Indicates whether the cloned volume should have replication enabled. If no value is provided, it will default to the replication status of the source volume(s).


  pi_volume_ids (True, list, None)
    (Required for new resource) List of volumes to be cloned.


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) The GUID of the service instance associated with an account.


  pi_volume_clone_name (True, str, None)
    (Required for new resource) The base name of the newly cloned volume(s).


  pi_user_tags (False, list, None)
    The user tags attached to this resource.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  zone (False, str, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environment variable 'IC_ZONE'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

