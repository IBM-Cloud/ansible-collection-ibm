
ibm_pi_volume -- Configure IBM Cloud 'ibm_pi_volume' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_volume' resource

This module supports idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.10.0
- Terraform v0.12.20



Parameters
----------

  pi_volume_size (True, float, None)
    (Required for new resource) Size of the volume in GB


  pi_volume_type (True, str, None)
    (Required for new resource) Volume type


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) Cloud Instance ID - This is the service_instance_id.


  pi_volume_name (True, str, None)
    (Required for new resource) Volume Name to create


  pi_volume_shareable (False, bool, None)
    Flag to indicate if the volume can be shared across multiple instances?


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

