
ibm_pi_snapshot -- Configure IBM Cloud 'ibm_pi_snapshot' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_snapshot' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.21.2
- Terraform v0.12.20



Parameters
----------

  pi_volume_ids (False, list, None)
    List of PI volumes


  pi_snap_shot_name (True, str, None)
    (Required for new resource) Unique name of the snapshot


  pi_instance_name (True, str, None)
    (Required for new resource) Instance name / id of the pvm


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) Cloud Instance ID - This is the service_instance_id.


  description (False, str, None)
    Snapshot description


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

