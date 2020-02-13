
ibm_resource_key -- Configure IBM Cloud 'ibm_resource_key' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_resource_key' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  name (False, str, None)
    (Required for new resource) The name of the resource key


  role (False, str, None)
    (Required for new resource) Name of the user role.Valid roles are Writer, Reader, Manager, Administrator, Operator, Viewer, Editor.


  resource_alias_id (False, str, None)
    The id of the resource alias for which to create resource key


  status (False, str, None)
    Status of resource key


  tags (False, list, None)
    None


  resource_instance_id (False, str, None)
    The id of the resource instance for which to create resource key


  parameters (False, dict, None)
    Arbitrary parameters to pass. Must be a JSON object


  credentials (False, dict, None)
    Credentials asociated with the key


  crn (False, str, None)
    crn of resource key


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

