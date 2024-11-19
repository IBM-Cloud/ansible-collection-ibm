
ibm_is_instance_group_manager_action -- Configure IBM Cloud 'ibm_is_instance_group_manager_action' resource
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_instance_group_manager_action' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance_group_manager_action

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  membership_count (False, int, None)
    The number of members the instance group should have at the scheduled time.


  run_at (False, str, None)
    The date and time the scheduled action will run.


  max_membership_count (False, int, None)
    The maximum number of members in a managed instance group


  instance_group (True, str, None)
    (Required for new resource) instance group ID


  cron_spec (False, str, None)
    The cron specification for a recurring scheduled action. Actions can be applied a maximum of one time within a 5 min period.


  min_membership_count (False, int, 1)
    The minimum number of members in a managed instance group


  target_manager (False, str, None)
    The unique identifier for this instance group manager of type autoscale.


  name (False, str, None)
    instance group manager action name


  instance_group_manager (True, str, None)
    (Required for new resource) Instance group manager ID of type scheduled


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

