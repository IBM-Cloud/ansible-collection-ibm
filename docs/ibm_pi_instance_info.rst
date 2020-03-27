
ibm_pi_instance_info -- Retrieve IBM Cloud 'ibm_pi_instance' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_pi_instance' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.6
- Terraform v0.12.20



Parameters
----------

  status (False, str, None)
    None


  minproc (False, int, None)
    None


  maxproc (False, int, None)
    None


  pi_cloud_instance_id (True, str, None)
    None


  volumes (False, list, None)
    None


  state (False, str, None)
    None


  processors (False, int, None)
    None


  proctype (False, str, None)
    None


  maxmem (False, int, None)
    None


  pi_instance_name (True, str, None)
    Server Name to be used for pvminstances


  health_status (False, str, None)
    None


  addresses (False, list, None)
    None


  minmem (False, int, None)
    None


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

