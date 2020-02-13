
ibm_service_key_info -- Retrieve IBM Cloud 'ibm_service_key' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_service_key' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  credentials (False, dict, None)
    Credentials asociated with the key


  name (True, str, None)
    The name of the service key


  service_instance_name (True, str, None)
    Service instance name for example, speech_to_text


  space_guid (True, str, None)
    The guid of the space in which the service instance is present


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

