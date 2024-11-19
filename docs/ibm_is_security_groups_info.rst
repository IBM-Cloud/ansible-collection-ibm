
ibm_is_security_groups_info -- Retrieve IBM Cloud 'ibm_is_security_groups' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_security_groups' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_security_groups

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  vpc_id (False, str, None)
    vpc identifier.


  vpc_crn (False, str, None)
    vpc crn


  vpc_name (False, str, None)
    vpc name.


  resource_group (False, str, None)
    resource group identifier.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

