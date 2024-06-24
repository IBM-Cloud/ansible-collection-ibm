
ibm_is_vpc_dns_resolution_binding -- Configure IBM Cloud 'ibm_is_vpc_dns_resolution_binding' resource
=====================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_vpc_dns_resolution_binding' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_vpc_dns_resolution_binding

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  vpc (True, list, None)
    (Required for new resource) The VPC bound to for DNS resolution.The VPC may be remote and therefore may not be directly retrievable.


  vpc_id (True, str, None)
    (Required for new resource) The VPC identifier.


  name (False, str, None)
    The name for this DNS resolution binding. The name is unique across all DNS resolution bindings for the VPC.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

