
ibm_pi_image -- Configure IBM Cloud 'ibm_pi_image' resource
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_image' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_image

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  pi_affinity_policy (False, str, None)
    Affinity policy for image; ignored if pi_image_storage_pool provided; for policy affinity requires one of pi_affinity_instance or pi_affinity_volume to be specified; for policy anti-affinity requires one of pi_anti_affinity_instances or pi_anti_affinity_volumes to be specified


  pi_affinity_volume (False, str, None)
    Volume (ID or Name) to base storage affinity policy against; required if requesting affinity and pi_affinity_instance is not provided


  pi_anti_affinity_volumes (False, list, None)
    List of volumes to base storage anti-affinity policy against; required if requesting anti-affinity and pi_anti_affinity_instances is not provided


  pi_user_tags (False, list, None)
    The user tags attached to this resource.


  pi_image_secret_key (False, str, None)
    Cloud Object Storage secret key; required for buckets with private access


  pi_image_bucket_region (False, str, None)
    Cloud Object Storage region


  pi_image_storage_pool (False, str, None)
    Storage pool where the image will be loaded, if provided then pi_affinity_policy will be ignored


  pi_affinity_instance (False, str, None)
    PVM Instance (ID or Name) to base storage affinity policy against; required if requesting storage affinity and pi_affinity_volume is not provided


  pi_image_storage_type (False, str, None)
    Type of storage; If not specified, default is tier3


  pi_image_name (True, str, None)
    (Required for new resource) Image name


  pi_image_id (False, str, None)
    Instance image id


  pi_image_access_key (False, str, None)
    Cloud Object Storage access key; required for buckets with private access


  pi_image_bucket_file_name (False, str, None)
    Cloud Object Storage image filename


  pi_anti_affinity_instances (False, list, None)
    List of pvmInstances to base storage anti-affinity policy against; required if requesting anti-affinity and pi_anti_affinity_volumes is not provided


  pi_image_import_details (False, list, None)
    None


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) PI cloud instance ID


  pi_image_bucket_name (False, str, None)
    Cloud Object Storage bucket name; bucket-name[/optional/folder]


  pi_image_bucket_access (False, str, public)
    Indicates if the bucket has public or private access


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

