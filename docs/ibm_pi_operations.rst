
ibm_pi_operations -- Configure IBM Cloud 'ibm_pi_operations' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_operations' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.4
- Terraform v0.12.20



Parameters
----------

  pi_operation (False, str, None)
    (Required for new resource)


  pi_progress (False, float, None)
    Progress of the operation


  pi_cloud_instance_id (False, str, None)
    (Required for new resource)


  pi_status (False, str, None)
    None


  pi_instance_name (False, str, None)
    (Required for new resource)


  addresses (False, list, None)
    None


  pi_health_status (False, str, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

