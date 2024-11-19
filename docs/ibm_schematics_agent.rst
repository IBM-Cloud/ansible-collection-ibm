
ibm_schematics_agent -- Configure IBM Cloud 'ibm_schematics_agent' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_schematics_agent' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/schematics_agent

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  schematics_location (True, str, None)
    (Required for new resource) List of locations supported by IBM Cloud Schematics service.  While creating your workspace or action, choose the right region, since it cannot be changed.  Note, this does not limit the location of the IBM Cloud resources, provisioned using Schematics.


  tags (False, list, None)
    Tags for the agent.


  agent_inputs (False, list, None)
    Additional input variables for the agent.


  user_state (False, list, None)
    User defined status of the agent.


  name (True, str, None)
    (Required for new resource) The name of the agent (must be unique, for an account).


  resource_group (True, str, None)
    (Required for new resource) The resource-group name for the agent.  By default, agent will be registered in Default Resource Group.


  version (True, str, None)
    (Required for new resource) Agent version.


  agent_location (True, str, None)
    (Required for new resource) The location where agent is deployed in the user environment.


  agent_infrastructure (True, list, None)
    (Required for new resource) The infrastructure parameters used by the agent.


  description (False, str, None)
    Agent description.


  agent_metadata (False, list, None)
    The metadata of an agent.


  run_destroy_resources (False, int, None)
    Argument which helps to run destroy resources job. Increment the value to destroy resources associated with agent deployment.


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

