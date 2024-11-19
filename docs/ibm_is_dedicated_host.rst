
ibm_is_dedicated_host -- Configure IBM Cloud 'ibm_is_dedicated_host' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_dedicated_host' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_dedicated_host

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  name (False, str, None)
    The unique user-defined name for this dedicated host. If unspecified, the name will be a hyphenated list of randomly-selected words.


  access_tags (False, list, None)
    List of access management tags


  instance_placement_enabled (False, bool, True)
    If set to true, instances can be placed on this dedicated host.


  profile (True, str, None)
    (Required for new resource) The Globally unique name of the dedicated host profile to use for this dedicated host.


  host_group (True, str, None)
    (Required for new resource) The unique identifier of the dedicated host group for this dedicated host.


  resource_group (False, str, None)
    The unique identifier for the resource group to use. If unspecified, the account's [default resourcegroup](https://cloud.ibm.com/apidocs/resource-manager#introduction) is used.


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

