
ibm_is_instance_group_membership -- Configure IBM Cloud 'ibm_is_instance_group_membership' resource
===================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_instance_group_membership' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance_group_membership

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.27.2
- Terraform v0.12.20



Parameters
----------

  name (False, str, None)
    The user-defined name for this instance group membership. Names must be unique within the instance group.


  instance_group (True, str, None)
    (Required for new resource) The instance group identifier.


  instance_group_membership (True, str, None)
    (Required for new resource) The unique identifier for this instance group membership.


  action_delete (False, bool, False)
    The delete flag for this instance group membership. Must be set to true to delete instance group membership.


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

