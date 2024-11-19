
ibm_schematics_state_info -- Retrieve IBM Cloud 'ibm_schematics_state' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_schematics_state' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/schematics_state

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  workspace_id (True, str, None)
    The ID of the workspace for which you want to retrieve the Terraform statefile URL.  To find the workspace ID, use the GET /v1/workspaces API.


  location (False, str, None)
    The Region of the workspace.


  template_id (True, str, None)
    The ID of the Terraform template for which you want to retrieve the Terraform statefile.  When you create a workspace, the Terraform template that your workspace points to is assigned a unique ID.  To find this ID, use the GET /v1/workspaces API and review the template_data.id value.


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

