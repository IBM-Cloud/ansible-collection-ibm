
ibm_is_ipsec_policy -- Configure IBM Cloud 'ibm_is_ipsec_policy' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_ipsec_policy' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_ipsec_policy

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  resource_group (False, str, None)
    Resource group info


  encryption_algorithm (True, str, None)
    (Required for new resource) Encryption algorithm


  pfs (True, str, None)
    (Required for new resource) PFS info


  key_lifetime (False, int, 3600)
    IPSEC key lifetime


  name (True, str, None)
    (Required for new resource) IPSEC name


  authentication_algorithm (True, str, None)
    (Required for new resource) Authentication alorothm


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

