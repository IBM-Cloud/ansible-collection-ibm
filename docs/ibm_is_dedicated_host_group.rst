
ibm_is_dedicated_host_group -- Configure IBM Cloud 'ibm_is_dedicated_host_group' resource
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_dedicated_host_group' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_dedicated_host_group

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  resource_group (False, str, None)
    The unique identifier of the resource group to use. If unspecified, the account's [default resourcegroup](https://cloud.ibm.com/apidocs/resource-manager#introduction) is used.


  zone (True, str, None)
    (Required for new resource) The globally unique name of the zone this dedicated host group will reside in.


  class_ (True, str, None)
    (Required for new resource) The dedicated host profile class for hosts in this group.


  family (True, str, None)
    (Required for new resource) The dedicated host profile family for hosts in this group.


  name (False, str, None)
    The unique user-defined name for this dedicated host group. If unspecified, the name will be a hyphenated list of randomly-selected words.


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

