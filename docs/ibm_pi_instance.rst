
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

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  pi_volume_ids (False, list, None)
    None


  pi_processors (False, float, None)
    (Required for new resource)


  pi_memory (False, float, None)
    (Required for new resource)


  pi_replication_scheme (False, str, suffix)
    None


  addresses (False, list, None)
    None


  instance_id (False, str, None)
    None


  pi_proc_type (False, str, None)
    (Required for new resource)


  pi_replicants (False, float, 1)
    None


  pi_cloud_instance_id (False, str, None)
    (Required for new resource) This is the Power Instance id that is assigned to the account


  min_processors (False, float, None)
    None


  pi_network_ids (False, list, None)
    (Required for new resource) Set of Networks that have been configured for the account


  pi_user_data (False, str, None)
    Base64 encoded data to be passed in for invoking a cloud init script


  pi_progress (False, float, None)
    Progress of the operation


  migratable (False, bool, None)
    None


  health_status (False, str, None)
    None


  pi_image_id (False, str, None)
    (Required for new resource)


  pi_replication_policy (False, str, none)
    None


  status (False, str, None)
    None


  pi_instance_name (False, str, None)
    (Required for new resource)


  pi_key_pair_name (False, str, None)
    (Required for new resource)


  pi_sys_type (False, str, None)
    (Required for new resource)


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

