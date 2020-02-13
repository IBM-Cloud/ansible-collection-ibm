
ibm_pi_tenant_info -- Retrieve IBM Cloud 'ibm_pi_tenant' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_pi_tenant' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  cloud_instances (False, list, None)
    None


  pi_cloud_instance_id (True, str, None)
    None


  creation_date (False, str, None)
    None


  enabled (False, bool, None)
    None


  tenant_name (False, str, None)
    None


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

