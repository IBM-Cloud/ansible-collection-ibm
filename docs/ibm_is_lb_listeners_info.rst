
ibm_is_lb_listeners_info -- Retrieve IBM Cloud 'ibm_is_lb_listeners' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_lb_listeners' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_lb_listeners

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  lb (True, str, None)
    The load balancer identifier.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

