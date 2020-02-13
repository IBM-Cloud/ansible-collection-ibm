
ibm_service_key -- Configure IBM Cloud 'ibm_service_key' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_service_key' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  name (False, str, None)
    (Required for new resource) The name of the service key


  service_instance_guid (False, str, None)
    (Required for new resource) The guid of the service instance for which to create service key


  parameters (False, dict, None)
    Arbitrary parameters to pass along to the service broker. Must be a JSON object


  credentials (False, dict, None)
    Credentials asociated with the key


  tags (False, list, None)
    None


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

