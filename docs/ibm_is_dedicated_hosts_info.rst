
ibm_is_dedicated_hosts_info -- Retrieve IBM Cloud 'ibm_is_dedicated_hosts' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_dedicated_hosts' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_dedicated_hosts

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  zone (False, str, None)
    The zone name this dedicated host is in


  name (False, str, None)
    The name of the dedicated host


  host_group (False, str, None)
    The unique identifier of the dedicated host group this dedicated host belongs to


  resource_group (False, str, None)
    The unique identifier of the resource group this dedicated host belongs to


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

