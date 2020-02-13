
ibm_pi_volume -- Configure IBM Cloud 'ibm_pi_volume' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_volume' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  pi_volume_name (False, str, None)
    (Required for new resource) Volume Name to create


  pi_volume_shareable (False, bool, None)
    Flag to indicate if the volume can be shared across multiple instances?


  pi_volume_size (False, float, None)
    (Required for new resource) Size of the volume in GB


  pi_volume_type (False, str, None)
    (Required for new resource)


  pi_cloud_instance_id (False, str, None)
    (Required for new resource)  Cloud Instance ID - This is the service_instance_id.


  volume_status (False, str, None)
    None


  volume_id (False, str, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

