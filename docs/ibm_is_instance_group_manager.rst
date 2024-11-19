
ibm_is_instance_group_manager -- Configure IBM Cloud 'ibm_is_instance_group_manager' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_instance_group_manager' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance_group_manager

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  name (False, str, None)
    instance group manager name


  aggregation_window (False, int, 90)
    The time window in seconds to aggregate metrics prior to evaluation


  cooldown (False, int, 300)
    The duration of time in seconds to pause further scale actions after scaling has taken place


  max_membership_count (False, int, None)
    The maximum number of members in a managed instance group


  min_membership_count (False, int, 1)
    The minimum number of members in a managed instance group


  enable_manager (False, bool, True)
    enable instance group manager


  instance_group (True, str, None)
    (Required for new resource) instance group ID


  manager_type (False, str, autoscale)
    The type of instance group manager.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

