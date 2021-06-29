
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

- IBM-Cloud terraform-provider-ibm v1.27.1
- Terraform v0.12.20



Parameters
----------

  wait_before_delete (False, bool, True)
    Enables stopping of instance before deleting and waits till deletion is complete


  network_interfaces (False, list, None)
    None


  vpc (True, str, None)
    (Required for new resource) VPC id


  primary_network_interface (True, list, None)
    (Required for new resource) Primary Network interface info


  user_data (False, str, None)
    User data given for the instance


  dedicated_host_group (False, str, None)
    Unique Identifier of the Dedicated Host Group where the instance will be placed


  force_recovery_time (False, int, None)
    Define timeout to force the instances to start/stop in minutes.


  name (True, str, None)
    (Required for new resource) Instance name


  image (True, str, None)
    (Required for new resource) image name


  dedicated_host (False, str, None)
    Unique Identifier of the Dedicated Host where the instance will be placed


  zone (True, str, None)
    (Required for new resource) Zone name


  boot_volume (False, list, None)
    None


  tags (False, list, None)
    list of tags for the instance


  auto_delete_volume (False, bool, None)
    Auto delete volume along with instance


  keys (True, list, None)
    (Required for new resource) SSH key Ids for the instance


  volumes (False, list, None)
    List of volumes


  profile (True, str, None)
    (Required for new resource) Profile info


  resource_group (False, str, None)
    Instance resource group


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

