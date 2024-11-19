
ibm_is_bare_metal_server -- Configure IBM Cloud 'ibm_is_bare_metal_server' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_bare_metal_server' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_bare_metal_server

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  trusted_platform_module (False, list, None)
    None


  user_data (False, str, None)
    User data given for the bare metal server


  zone (True, str, None)
    (Required for new resource) Zone name


  access_tags (False, list, None)
    List of access management tags


  bandwidth (False, int, None)
    The total bandwidth (in megabits per second)


  delete_type (False, str, hard)
    Enables stopping type of the bare metal server before deleting


  primary_network_interface (False, list, None)
    Primary Network interface info


  network_interfaces (False, list, None)
    None


  tags (False, list, None)
    Tags for the Bare metal server


  enable_secure_boot (False, bool, None)
    Indicates whether secure boot is enabled. If enabled, the image must support secure boot or the server will fail to boot.


  network_attachments (False, list, None)
    The network attachments for this bare metal server, including the primary network attachment.


  resource_group (False, str, None)
    Resource group name


  keys (True, list, None)
    (Required for new resource) SSH key Ids for the bare metal server


  profile (True, str, None)
    (Required for new resource) profile name


  name (False, str, None)
    Bare metal server name


  action (False, str, None)
    This restart/start/stops a bare metal server.


  primary_network_attachment (False, list, None)
    The primary network attachment.


  image (True, str, None)
    (Required for new resource) image id


  vpc (False, str, None)
    The VPC the bare metal server is to be a part of


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

