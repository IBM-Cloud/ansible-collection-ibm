
ibm_resource_key_info -- Retrieve IBM Cloud 'ibm_resource_key' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_resource_key' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  credentials (False, dict, None)
    Credentials asociated with the key


  most_recent (False, bool, False)
    If true and multiple entries are found, the most recently created resource key is used. If false, an error is returned


  crn (False, str, None)
    crn of resource key


  name (True, str, None)
    The name of the resource key


  resource_instance_id (False, str, None)
    The id of the resource instance


  resource_alias_id (False, str, None)
    The id of the resource alias


  role (False, str, None)
    User role


  status (False, str, None)
    Status of resource key


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

