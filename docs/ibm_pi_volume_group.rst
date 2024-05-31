
ibm_pi_volume_group -- Configure IBM Cloud 'ibm_pi_volume_group' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_volume_group' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_volume_group

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.65.1
- Terraform v1.5.5



Parameters
----------

  pi_cloud_instance_id (True, str, None)
    (Required for new resource) Cloud Instance ID - This is the service_instance_id.


  pi_volume_group_name (False, str, None)
    Volume Group Name to create


  pi_consistency_group_name (False, str, None)
    The name of consistency group at storage controller level


  pi_volume_ids (True, list, None)
    (Required for new resource) List of volumes to add in volume group


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

