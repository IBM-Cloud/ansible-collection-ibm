
ibm_pi_shared_processor_pool -- Configure IBM Cloud 'ibm_pi_shared_processor_pool' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_shared_processor_pool' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_shared_processor_pool

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  pi_shared_processor_pool_placement_group_id (False, str, None)
    Placement group the shared processor pool is created in


  spp_placement_groups (False, list, None)
    SPP placement groups the shared processor pool are in


  pi_shared_processor_pool_name (True, str, None)
    (Required for new resource) Name of the shared processor pool


  pi_shared_processor_pool_host_group (True, str, None)
    (Required for new resource) Host group of the shared processor pool


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) PI cloud instance ID


  pi_host_id (False, str, None)
    The host id of a host in a host group (only available for dedicated hosts)


  pi_shared_processor_pool_reserved_cores (True, int, None)
    (Required for new resource) The amount of reserved cores for the shared processor pool


  pi_user_tags (False, list, None)
    The user tags attached to this resource.


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

