
ibm_is_public_gateway -- Configure IBM Cloud 'ibm_is_public_gateway' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_public_gateway' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_public_gateway

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  resource_group (False, str, None)
    Public gateway resource group info


  zone (True, str, None)
    (Required for new resource) Public gateway zone info


  access_tags (False, list, None)
    List of access management tags


  floating_ip (False, dict, None)
    None


  vpc (True, str, None)
    (Required for new resource) Public gateway VPC info


  tags (False, list, None)
    Service tags for the public gateway instance


  name (True, str, None)
    (Required for new resource) Name of the Public gateway instance


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

