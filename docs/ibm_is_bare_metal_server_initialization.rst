
ibm_is_bare_metal_server_initialization -- Configure IBM Cloud 'ibm_is_bare_metal_server_initialization' resource
=================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_bare_metal_server_initialization' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_bare_metal_server_initialization

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  bare_metal_server (True, str, None)
    (Required for new resource) Bare metal server identifier


  image (True, str, None)
    (Required for new resource) The image to be used when provisioning the bare metal server.


  keys (True, list, None)
    (Required for new resource) SSH key Ids for the bare metal server


  user_data (False, str, None)
    Bare metal server user data to replace initialization


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

