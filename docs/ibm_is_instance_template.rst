
ibm_is_instance_template -- Configure IBM Cloud 'ibm_is_instance_template' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_instance_template' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance_template

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.30.0
- Terraform v0.12.20



Parameters
----------

  image (True, str, None)
    (Required for new resource) image name


  dedicated_host_group (False, str, None)
    Unique Identifier of the Dedicated Host Group where the instance will be placed


  resource_group (False, str, None)
    Instance template resource group


  name (True, str, None)
    (Required for new resource) Instance Template name


  keys (True, list, None)
    (Required for new resource) SSH key Ids for the instance template


  network_interfaces (False, list, None)
    None


  vpc (True, str, None)
    (Required for new resource) VPC id


  primary_network_interface (True, list, None)
    (Required for new resource) Primary Network interface info


  profile (True, str, None)
    (Required for new resource) Profile info


  user_data (False, str, None)
    User data given for the instance


  boot_volume (False, list, None)
    None


  dedicated_host (False, str, None)
    Unique Identifier of the Dedicated Host where the instance will be placed


  zone (True, str, None)
    (Required for new resource) Zone name


  volume_attachments (False, list, None)
    None


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

