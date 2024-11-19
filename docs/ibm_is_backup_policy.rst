
ibm_is_backup_policy -- Configure IBM Cloud 'ibm_is_backup_policy' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_backup_policy' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_backup_policy

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  scope (False, list, None)
    The scope for this backup policy.


  included_content (False, list, None)
    The included content for backups created using this policy


  name (True, str, None)
    (Required for new resource) The user-defined name for this backup policy. Names must be unique within the region this backup policy resides in. If unspecified, the name will be a hyphenated list of randomly-selected words.


  match_resource_type (False, str, volume)
    A resource type this backup policy applies to. Resources that have both a matching type and a matching user tag will be subject to the backup policy.


  resource_group (False, str, None)
    The unique identifier of the resource group to use. If unspecified, the account's [default resourcegroup](https://cloud.ibm.com/apidocs/resource-manager#introduction) is used.


  match_user_tags (True, list, None)
    (Required for new resource) The user tags this backup policy applies to. Resources that have both a matching user tag and a matching type will be subject to the backup policy.


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

