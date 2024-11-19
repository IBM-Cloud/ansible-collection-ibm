
ibm_pi_workspace -- Configure IBM Cloud 'ibm_pi_workspace' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_workspace' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_workspace

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  pi_datacenter (True, str, None)
    (Required for new resource) Target location or environment to create the resource instance.


  pi_name (True, str, None)
    (Required for new resource) A descriptive name used to identify the workspace.


  pi_plan (False, str, public)
    Plan associated with the offering; Valid values are public or private.


  pi_resource_group_id (True, str, None)
    (Required for new resource) The ID of the resource group where you want to create the workspace. You can retrieve the value from data source ibm_resource_group.


  pi_user_tags (False, list, None)
    List of user tags attached to the resource.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  zone (False, str, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environment variable 'IC_ZONE'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

