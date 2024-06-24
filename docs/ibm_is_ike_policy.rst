
ibm_is_ike_policy -- Configure IBM Cloud 'ibm_is_ike_policy' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_ike_policy' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_ike_policy

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  authentication_algorithm (True, str, None)
    (Required for new resource) Authentication algorithm type


  encryption_algorithm (True, str, None)
    (Required for new resource) Encryption alogorithm type


  key_lifetime (False, int, 28800)
    IKE Key lifetime


  name (True, str, None)
    (Required for new resource) IKE name


  dh_group (True, int, None)
    (Required for new resource) IKE DH group


  resource_group (False, str, None)
    IKE resource group ID


  ike_version (False, int, None)
    IKE version


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

