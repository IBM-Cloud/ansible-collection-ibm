
ibm_schematics_policy -- Configure IBM Cloud 'ibm_schematics_policy' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_schematics_policy' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/schematics_policy

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  name (True, str, None)
    (Required for new resource) Name of Schematics customization policy.


  scoped_resources (False, list, None)
    List of scoped Schematics resources targeted by the policy.


  state_ (False, list, None)
    User defined status of the Schematics object.


  kind (False, str, None)
    Policy kind or categories for managing and deriving policy decision  * `agent_assignment_policy` Agent assignment policy for job execution.


  parameter (False, list, None)
    The parameter to tune the Schematics policy.


  description (False, str, None)
    The description of Schematics customization policy.


  resource_group (False, str, None)
    The resource group name for the policy.  By default, Policy will be created in `default` Resource Group.


  target (False, list, None)
    The objects for the Schematics policy.


  tags (False, list, None)
    Tags for the Schematics customization policy.


  location (False, str, None)
    List of locations supported by IBM Cloud Schematics service.  While creating your workspace or action, choose the right region, since it cannot be changed.  Note, this does not limit the location of the IBM Cloud resources, provisioned using Schematics.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

