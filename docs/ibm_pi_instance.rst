
ibm_pi_instance -- Configure IBM Cloud 'ibm_pi_instance' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_instance' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_instance

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.38.2
- Terraform v0.12.20



Parameters
----------

  pi_replication_scheme (False, str, suffix)
    Replication scheme


  pi_health_status (False, str, OK)
    Allow the user to set the status of the lpar so that they can connect to it faster


  pi_affinity_volume (False, str, None)
    Volume (ID or Name) to base storage affinity policy against; required if requesting affinity and pi_affinity_instance is not provided


  pi_anti_affinity_volumes (False, list, None)
    List of volumes to base storage anti-affinity policy against; required if requesting anti-affinity and pi_anti_affinity_instances is not provided


  pi_storage_pool_affinity (False, bool, True)
    Indicates if all volumes attached to the server must reside in the same storage pool


  pi_sap_profile_id (False, str, None)
    SAP Profile ID for the amount of cores and memory


  pi_processors (False, float, None)
    Processors count


  pi_proc_type (False, str, None)
    Instance processor type


  pi_volume_ids (False, list, None)
    List of PI volumes


  pi_affinity_instance (False, str, None)
    PVM Instance (ID or Name) to base storage affinity policy against; required if requesting storage affinity and pi_affinity_volume is not provided


  pi_network (True, list, None)
    (Required for new resource) List of one or more networks to attach to the instance


  pi_migratable (False, bool, None)
    set to true to enable migration of the PI instance


  pi_storage_pool (False, str, None)
    Storage Pool for server deployment; if provided then pi_affinity_policy and pi_storage_type will be ignored


  pi_instance_name (True, str, None)
    (Required for new resource) PI Instance name


  pi_replicants (False, int, 1)
    PI Instance replicas count


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) This is the Power Instance id that is assigned to the account


  pi_storage_type (False, str, None)
    Storage type for server deployment


  pi_affinity_policy (False, str, None)
    Affinity policy for pvm instance being created; ignored if pi_storage_pool provided; for policy affinity requires one of pi_affinity_instance or pi_affinity_volume to be specified; for policy anti-affinity requires one of pi_anti_affinity_instances or pi_anti_affinity_volumes to be specified


  pi_image_id (True, str, None)
    (Required for new resource) PI instance image id


  pi_storage_connection (False, str, None)
    Storage Connectivity Group for server deployment


  pi_placement_group_id (False, str, None)
    Placement group ID


  pi_user_data (False, str, None)
    Base64 encoded data to be passed in for invoking a cloud init script


  pi_replication_policy (False, str, none)
    Replication policy for the PI Instance


  pi_pin_policy (False, str, none)
    Pin Policy of the instance


  pi_key_pair_name (False, str, None)
    SSH key name


  pi_memory (False, float, None)
    Memory size


  pi_virtual_cores_assigned (False, int, None)
    Virtual Cores Assigned to the PVMInstance


  pi_license_repository_capacity (False, int, None)
    The VTL license repository capacity TB value


  pi_anti_affinity_instances (False, list, None)
    List of pvmInstances to base storage anti-affinity policy against; required if requesting anti-affinity and pi_anti_affinity_volumes is not provided


  pi_sys_type (False, str, None)
    PI Instance system type


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

