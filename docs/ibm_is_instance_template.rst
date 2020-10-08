
ibm_is_instance_template -- Configure IBM Cloud 'ibm_is_instance_template' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_instance_template' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.13.1
- Terraform v0.12.20



Parameters
----------

  name (True, str, None)
    (Required for new resource) Instance Template name


  primary_network_interface (True, list, None)
    (Required for new resource) Primary Network interface info


  image (True, str, None)
    (Required for new resource) image name


  boot_volume (False, list, None)
    None


  user_data (False, str, None)
    User data given for the instance


  resource_group (False, str, None)
    Instance template resource group


  vpc (True, str, None)
    (Required for new resource) VPC id


  zone (True, str, None)
    (Required for new resource) Zone name


  profile (True, str, None)
    (Required for new resource) Profile info


  keys (True, list, None)
    (Required for new resource) SSH key Ids for the instance template


  volume_attachments (False, list, None)
    None


  network_interfaces (False, list, None)
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

