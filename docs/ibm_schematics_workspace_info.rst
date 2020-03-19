
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

- IBM-Cloud terraform-provider-ibm v1.2.5
- Terraform v0.12.20



Parameters
----------

  template_id (False, list, None)
    The id of templates


  name (False, str, None)
    The name of workspace


  resource_group (False, str, None)
    The resource group of workspace


  types (False, list, None)
    None


  tags (False, list, None)
    None


  workspace_id (True, str, None)
    The id of workspace


  status (False, str, None)
    The status of workspace


  is_frozen (False, bool, None)
    None


  is_locked (False, bool, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this workspace


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

