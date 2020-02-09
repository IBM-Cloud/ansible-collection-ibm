
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

- IBM-Cloud terraform-provider-ibm v1.2.0
- Terraform v0.12.20



Parameters
----------

  status (False, str, None)
    None


  volumeid (False, str, None)
    None


  replicationpolicy (False, str, None)
    None


  processors (False, int, None)
    None


  name (False, str, None)
    None


  pi_cloud_instance_id (True, str, None)
    None


  state (False, str, None)
    None


  replicants (False, int, None)
    None


  shareable (False, bool, None)
    None


  healthstatus (False, str, None)
    None


  addresses (False, list, None)
    None


  proctype (False, str, None)
    None


  pi_instance_name (True, str, None)
    Server Name to be used for pvminstances


  health (False, list, None)
    None


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

