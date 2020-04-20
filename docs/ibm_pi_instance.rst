
ibm_pi_instance -- Configure IBM Cloud 'ibm_pi_instance' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_instance' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  max_processors (False, float, None)
    NA


  max_memory (False, float, None)
    NA


  pi_user_data (False, str, None)
    Base64 encoded data to be passed in for invoking a cloud init script


  pi_processors (False, float, None)
    (Required for new resource) NA


  pi_proc_type (False, str, None)
    (Required for new resource) NA


  pi_replicants (False, float, 1)
    NA


  pi_progress (False, float, None)
    Progress of the operation


  pi_cloud_instance_id (False, str, None)
    (Required for new resource) This is the Power Instance id that is assigned to the account


  min_processors (False, float, None)
    NA


  pi_volume_ids (False, list, None)
    NA


  health_status (False, str, None)
    NA


  instance_id (False, str, None)
    NA


  pi_replication_policy (False, str, none)
    NA


  pi_replication_scheme (False, str, suffix)
    NA


  status (False, str, None)
    NA


  min_memory (False, float, None)
    NA


  pi_instance_name (False, str, None)
    (Required for new resource) NA


  pi_key_pair_name (False, str, None)
    (Required for new resource) NA


  pi_memory (False, float, None)
    (Required for new resource) NA


  pi_sys_type (False, str, None)
    (Required for new resource) NA


  migratable (False, bool, None)
    NA


  pi_network_ids (False, list, None)
    (Required for new resource) Set of Networks that have been configured for the account


  addresses (False, list, None)
    NA


  pi_image_id (False, str, None)
    (Required for new resource) NA


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environment variable 'IC_ZONE'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

