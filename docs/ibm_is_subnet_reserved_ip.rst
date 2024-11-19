
ibm_is_subnet_reserved_ip -- Configure IBM Cloud 'ibm_is_subnet_reserved_ip' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_subnet_reserved_ip' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_subnet_reserved_ip

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  subnet (True, str, None)
    (Required for new resource) The subnet identifier.


  auto_delete (False, bool, None)
    If set to true, this reserved IP will be automatically deleted


  target (False, str, None)
    The unique identifier for target.


  target_crn (False, str, None)
    The crn for target.


  name (False, str, None)
    The user-defined or system-provided name for this reserved IP.


  address (False, str, None)
    The address for this reserved IP.


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

