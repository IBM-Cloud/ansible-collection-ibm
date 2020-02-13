
ibm_service_instance_info -- Retrieve IBM Cloud 'ibm_service_instance' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_service_instance' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  service_plan_guid (False, str, None)
    The uniquie identifier of the service offering plan type


  name (True, str, None)
    Service instance name for example, speech_to_text


  space_guid (True, str, None)
    The guid of the space in which the instance is present


  credentials (False, dict, None)
    The service broker-provided credentials to use this service.


  service_keys (False, list, None)
    Service keys asociated with the service instance


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

