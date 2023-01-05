
ibm_is_instance -- Configure IBM Cloud 'ibm_is_instance' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_instance' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.48.0
- Terraform v0.12.20



Parameters
----------

  profile (False, str, None)
    Profile info


  auto_delete_volume (False, bool, None)
    Auto delete volume along with instance


  resource_group (False, str, None)
    Instance resource group


  instance_template (False, str, None)
    Id of the instance template


  keys (False, list, None)
    SSH key Ids for the instance


  tags (False, list, None)
    list of tags for the instance


  boot_volume (False, list, None)
    None


  name (True, str, None)
    (Required for new resource) Instance name


  zone (False, str, None)
    Zone name


  default_trusted_profile_target (False, str, None)
    The unique identifier or CRN of the default IAM trusted profile to use for this virtual server instance.


  wait_before_delete (False, bool, True)
    Enables stopping of instance before deleting and waits till deletion is complete


  total_volume_bandwidth (False, int, None)
    The amount of bandwidth (in megabits per second) allocated exclusively to instance storage volumes


  image (False, str, None)
    image id


  metadata_service_enabled (False, bool, None)
    Indicates whether the metadata service endpoint is available to the virtual server instance


  dedicated_host_group (False, str, None)
    Unique Identifier of the Dedicated Host Group where the instance will be placed


  availability_policy_host_failure (False, str, None)
    The availability policy to use for this virtual server instance


  force_recovery_time (False, int, None)
    Define timeout to force the instances to start/stop in minutes.


  vpc (False, str, None)
    VPC id


  force_action (False, bool, False)
    If set to true, the action will be forced immediately, and all queued actions deleted. Ignored for the start action.


  primary_network_interface (False, list, None)
    Primary Network interface info


  network_interfaces (False, list, None)
    None


  volumes (False, list, None)
    List of volumes


  user_data (False, str, None)
    User data given for the instance


  default_trusted_profile_auto_link (False, bool, None)
    If set to `true`, the system will create a link to the specified `target` trusted profile during instance creation. Regardless of whether a link is created by the system or manually using the IAM Identity service, it will be automatically deleted when the instance is deleted.


  dedicated_host (False, str, None)
    Unique Identifier of the Dedicated Host where the instance will be placed


  placement_group (False, str, None)
    Unique Identifier of the Placement Group for restricting the placement of the instance


  action (False, str, None)
    Enables stopping of instance before deleting and waits till deletion is complete


  catalog_offering (False, list, None)
    The catalog offering or offering version to use when provisioning this virtual server instance. If an offering is specified, the latest version of that offering will be used. The specified offering or offering version may be in a different account in the same enterprise, subject to IAM policies.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

