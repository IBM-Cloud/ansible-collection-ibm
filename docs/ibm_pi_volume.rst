
ibm_pi_volume -- Configure IBM Cloud 'ibm_pi_volume' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_volume' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_volume

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.65.1
- Terraform v1.5.5



Parameters
----------

  pi_volume_shareable (False, bool, None)
    Flag to indicate if the volume can be shared across multiple instances.


  pi_volume_pool (False, str, None)
    Volume pool where the volume will be created; if provided then pi_affinity_policy values will be ignored


  pi_affinity_volume (False, str, None)
    Volume (ID or Name) to base volume affinity policy against; required if requesting affinity and pi_affinity_instance is not provided


  pi_affinity_instance (False, str, None)
    PVM Instance (ID or Name) to base volume affinity policy against; required if requesting affinity and pi_affinity_volume is not provided


  pi_volume_name (True, str, None)
    (Required for new resource) Volume Name to create


  pi_replication_enabled (False, bool, None)
    Indicates if the volume should be replication enabled or not


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) Cloud Instance ID - This is the service_instance_id.


  pi_volume_type (False, str, None)
    Type of disk, if disk type is not provided the disk type will default to tier3


  pi_affinity_policy (False, str, None)
    Affinity policy for data volume being created; ignored if pi_volume_pool provided; for policy affinity requires one of pi_affinity_instance or pi_affinity_volume to be specified; for policy anti-affinity requires one of pi_anti_affinity_instances or pi_anti_affinity_volumes to be specified


  pi_anti_affinity_volumes (False, list, None)
    List of volumes to base volume anti-affinity policy against; required if requesting anti-affinity and pi_anti_affinity_instances is not provided


  pi_anti_affinity_instances (False, list, None)
    List of pvmInstances to base volume anti-affinity policy against; required if requesting anti-affinity and pi_anti_affinity_volumes is not provided


  pi_volume_size (True, float, None)
    (Required for new resource) Size of the volume in GB


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

