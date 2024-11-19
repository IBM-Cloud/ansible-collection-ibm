
ibm_pi_snapshot -- Configure IBM Cloud 'ibm_pi_snapshot' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_snapshot' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_snapshot

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  pi_volume_ids (False, list, None)
    A list of volume IDs of the instance that will be part of the snapshot. If none are provided, then all the volumes of the instance will be part of the snapshot.


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) The GUID of the service instance associated with an account.


  pi_description (False, str, None)
    Description of the PVM instance snapshot.


  pi_instance_name (True, str, None)
    (Required for new resource) The name of the instance you want to take a snapshot of.


  pi_snap_shot_name (True, str, None)
    (Required for new resource) The unique name of the snapshot.


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

