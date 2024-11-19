
ibm_pi_image_export -- Configure IBM Cloud 'ibm_pi_image_export' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_image_export' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_image_export

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  pi_image_secret_key (True, str, None)
    (Required for new resource) Cloud Object Storage secret key; required for buckets with private access


  pi_image_bucket_region (True, str, None)
    (Required for new resource) Cloud Object Storage region


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) PI cloud instance ID


  pi_image_id (True, str, None)
    (Required for new resource) Instance image id


  pi_image_bucket_name (True, str, None)
    (Required for new resource) Cloud Object Storage bucket name; bucket-name[/optional/folder]


  pi_image_access_key (True, str, None)
    (Required for new resource) Cloud Object Storage access key; required for buckets with private access


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

