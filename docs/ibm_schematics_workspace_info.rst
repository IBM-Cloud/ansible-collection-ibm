
ibm_schematics_workspace_info -- Retrieve IBM Cloud 'ibm_schematics_workspace' resource
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_schematics_workspace' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  is_locked (False, bool, None)
    None


  crn (False, str, None)
    cloud resource name of the workspace


  template_id (False, list, None)
    The id of templates


  status (False, str, None)
    The status of workspace


  is_frozen (False, bool, None)
    None


  workspace_id (True, str, None)
    The id of workspace


  location (False, str, None)
    The location of workspace


  tags (False, list, None)
    None


  resource_group (False, str, None)
    The resource group of workspace


  types (False, list, None)
    None


  description (False, str, None)
    The description of workspace


  catalog_ref (False, dict, None)
    Catalog references


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this workspace


  name (False, str, None)
    The name of workspace


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

