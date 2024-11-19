
ibm_schematics_job -- Configure IBM Cloud 'ibm_schematics_job' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_schematics_job' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/schematics_job

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  job_env_settings (False, list, None)
    Environment variables used by the Job while performing Action or Workspace.


  command_parameter (False, str, None)
    Schematics job command parameter (playbook-name).


  tags (False, list, None)
    User defined tags, while running the job.


  location (False, str, None)
    List of locations supported by IBM Cloud Schematics service.  While creating your workspace or action, choose the right region, since it cannot be changed.  Note, this does not limit the location of the IBM Cloud resources, provisioned using Schematics.


  data (False, list, None)
    Job data.


  log_summary (False, list, None)
    Job log summary record.


  command_object (True, str, None)
    (Required for new resource) Name of the Schematics automation resource.


  bastion (False, list, None)
    Describes a bastion resource.


  command_object_id (True, str, None)
    (Required for new resource) Job command object id (workspace-id, action-id).


  command_name (True, str, None)
    (Required for new resource) Schematics job command name.


  command_options (False, list, None)
    Command line options for the command.


  job_inputs (False, list, None)
    Job inputs used by Action or Workspace.


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

