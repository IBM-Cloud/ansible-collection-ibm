
ibm_pi_volume_attach -- Configure IBM Cloud 'ibm_pi_volume_attach' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_volume_attach' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.6
- Terraform v0.12.20



Parameters
----------

  status (False, str, None)
    None


  pi_volume_shareable (False, bool, None)
    None


  volumeattachid (False, str, None)
    None


  pi_cloud_instance_id (False, str, None)
    (Required for new resource) Cloud Instance ID - This is the service_instance_id.


  pi_volume_attach_name (False, str, None)
    (Required for new resource) Name of the volume to attach. Note these  volumes should have been created


  pi_instance_name (False, str, None)
    (Required for new resource)


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

