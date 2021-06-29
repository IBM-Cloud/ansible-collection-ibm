
ibm_pi_instance -- Configure IBM Cloud 'ibm_pi_instance' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_instance' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_instance

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.27.1
- Terraform v0.12.20



Parameters
----------

  pi_key_pair_name (True, str, None)
    (Required for new resource) SSH key name


  pi_memory (True, float, None)
    (Required for new resource) Memory size


  pi_health_status (False, str, OK)
    Allow the user to set the status of the lpar so that they can connect to it faster


  pi_processors (True, float, None)
    (Required for new resource) Processors count


  pi_image_id (True, str, None)
    (Required for new resource) PI instance image name


  pi_volume_ids (False, list, None)
    List of PI volumes


  pi_replicants (False, float, 1)
    PI Instance replicas count


  pi_replication_policy (False, str, none)
    Replication policy for the PI Instance


  pi_replication_scheme (False, str, suffix)
    Replication scheme


  pi_network_ids (True, list, None)
    (Required for new resource) List of Networks that have been configured for the account


  pi_instance_name (True, str, None)
    (Required for new resource) PI Instance name


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) This is the Power Instance id that is assigned to the account


  pi_sys_type (True, str, None)
    (Required for new resource) PI Instance system type


  pi_user_data (False, str, None)
    Base64 encoded data to be passed in for invoking a cloud init script


  pi_proc_type (True, str, None)
    (Required for new resource) Instance processor type


  pi_pin_policy (False, str, none)
    Pin Policy of the instance


  pi_virtual_cores_assigned (False, int, None)
    Virtual Cores Assigned to the PVMInstance


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

