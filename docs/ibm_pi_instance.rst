
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

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  pi_proc_type (False, str, None)
    Instance processor type


  pi_storage_pool_affinity (False, bool, True)
    Indicates if all volumes attached to the server must reside in the same storage pool


  pi_pin_policy (False, str, none)
    Pin Policy of the instance


  pi_image_id (True, str, None)
    (Required for new resource) PI instance image id


  pi_replication_scheme (False, str, suffix)
    Replication scheme


  pi_virtual_optical_device (False, str, None)
    Virtual Machine's Cloud Initialization Virtual Optical Device


  pi_anti_affinity_volumes (False, list, None)
    List of volumes to base storage anti-affinity policy against; required if requesting anti-affinity and pi_anti_affinity_instances is not provided


  pi_sap_profile_id (False, str, None)
    SAP Profile ID for the amount of cores and memory


  pi_storage_pool (False, str, None)
    Storage Pool for server deployment; if provided then pi_storage_pool_affinity will be ignored; Only valid when you deploy one of the IBM supplied stock images. Storage pool for a custom image (an imported image or an image that is created from a VM capture) defaults to the storage pool the image was created in


  pi_placement_group_id (False, str, None)
    Placement group ID


  pi_deployment_type (False, str, None)
    Custom Deployment Type Information


  pi_shared_processor_pool (False, str, None)
    Shared Processor Pool the instance is deployed on


  pi_key_pair_name (False, str, None)
    SSH key name


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) This is the Power Instance id that is assigned to the account


  pi_health_status (False, str, OK)
    Allow the user to set the status of the lpar so that they can connect to it faster


  pi_ibmi_css (False, bool, None)
    IBM i Cloud Storage Solution


  pi_ibmi_pha (False, bool, None)
    IBM i Power High Availability


  pi_replicants (False, int, 1)
    PI Instance replicas count


  pi_boot_volume_replication_enabled (False, bool, None)
    Indicates if the boot volume should be replication enabled or not.


  pi_memory (False, float, None)
    Memory size


  pi_processors (False, float, None)
    Processors count


  pi_replication_sites (False, list, None)
    Indicates the replication sites of the boot volume.


  pi_virtual_cores_assigned (False, int, None)
    Virtual Cores Assigned to the PVMInstance


  pi_affinity_policy (False, str, None)
    Affinity policy for pvm instance being created; ignored if pi_storage_pool provided; for policy affinity requires one of pi_affinity_instance or pi_affinity_volume to be specified; for policy anti-affinity requires one of pi_anti_affinity_instances or pi_anti_affinity_volumes to be specified


  pi_deployment_target (False, list, None)
    The deployment of a dedicated host.


  pi_network (True, list, None)
    (Required for new resource) List of one or more networks to attach to the instance


  pi_sys_type (False, str, None)
    PI Instance system type


  pi_volume_ids (False, list, None)
    List of PI volumes


  pi_anti_affinity_instances (False, list, None)
    List of pvmInstances to base storage anti-affinity policy against; required if requesting anti-affinity and pi_anti_affinity_volumes is not provided


  pi_replication_policy (False, str, none)
    Replication policy for the PI Instance


  pi_user_tags (False, list, None)
    The user tags attached to this resource.


  pi_user_data (False, str, None)
    Base64 encoded data to be passed in for invoking a cloud init script


  pi_sap_deployment_type (False, str, None)
    Custom SAP Deployment Type Information


  pi_storage_type (False, str, None)
    Storage type for server deployment; if pi_storage_type is not provided the storage type will default to tier3


  pi_storage_connection (False, str, None)
    Storage Connectivity Group for server deployment


  pi_affinity_volume (False, str, None)
    Volume (ID or Name) to base storage affinity policy against; required if requesting affinity and pi_affinity_instance is not provided


  pi_ibmi_rds_users (False, int, None)
    IBM i Rational Dev Studio Number of User Licenses


  pi_instance_name (True, str, None)
    (Required for new resource) PI Instance name


  pi_affinity_instance (False, str, None)
    PVM Instance (ID or Name) to base storage affinity policy against; required if requesting storage affinity and pi_affinity_volume is not provided


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

