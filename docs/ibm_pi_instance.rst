
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

- IBM-Cloud terraform-provider-ibm v1.7.1
- Terraform v0.12.20



Parameters
----------

  pi_image_id (False, str, None)
    (Required for new resource) PI instance image name


  status (False, str, None)
    PI instance status


  min_processors (False, float, None)
    Minimum number of the CPUs


  max_memory (False, float, None)
    Maximum memory size


  pi_user_data (False, str, None)
    Base64 encoded data to be passed in for invoking a cloud init script


  pi_volume_ids (False, list, None)
    List of PI volumes


  pi_pin_policy (False, str, none)
    Pin Policy of the instance


  migratable (False, bool, None)
    set to true to enable migration of the PI instance


  max_processors (False, float, None)
    Maximum number of processors


  pin_policy (False, str, None)
    PIN Policy of the Instance


  pi_cloud_instance_id (False, str, None)
    (Required for new resource) This is the Power Instance id that is assigned to the account


  instance_id (False, str, None)
    Instance ID


  reboot_for_resource_change (False, str, None)
    Flag to be passed for CPU/Memory changes that require a reboot to take effect


  addresses (False, list, None)
    None


  health_status (False, str, None)
    PI Instance health status


  min_memory (False, float, None)
    Minimum memory


  pi_key_pair_name (False, str, None)
    (Required for new resource) SSH key name


  pi_memory (False, float, None)
    (Required for new resource) Memory size


  pi_replicants (False, float, 1)
    PI Instance repicas count


  pi_replication_scheme (False, str, suffix)
    Replication scheme


  pi_progress (False, float, None)
    Progress of the operation


  pi_sys_type (False, str, None)
    (Required for new resource) PI Instance system type


  pi_network_ids (False, list, None)
    (Required for new resource) Set of Networks that have been configured for the account


  pi_processors (False, float, None)
    (Required for new resource) Processors count


  pi_instance_name (False, str, None)
    (Required for new resource) PI Instance name


  pi_proc_type (False, str, None)
    (Required for new resource) Instance processor type


  pi_replication_policy (False, str, none)
    Replication policy for the PI INstance


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

