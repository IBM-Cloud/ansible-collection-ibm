
ibm_is_bare_metal_server_initialization_info -- Retrieve IBM Cloud 'ibm_is_bare_metal_server_initialization' resource
=====================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_bare_metal_server_initialization' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_bare_metal_server_initialization

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  bare_metal_server (True, str, None)
    The bare metal server identifier


  private_key (False, str, None)
    Bare Metal Server Private Key file


  passphrase (False, str, None)
    Passphrase for Bare Metal Server Private Key file


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

