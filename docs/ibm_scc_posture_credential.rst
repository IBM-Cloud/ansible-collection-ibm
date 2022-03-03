
ibm_scc_posture_credential -- Configure IBM Cloud 'ibm_scc_posture_credential' resource
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_scc_posture_credential' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/scc_posture_credential

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.39.1
- Terraform v0.12.20



Parameters
----------

  name (True, str, None)
    (Required for new resource) Credentials name.


  description (True, str, None)
    (Required for new resource) Credentials description.


  display_fields (True, list, None)
    (Required for new resource) Details the fields on the credential. This will change as per credential type selected.


  group (True, list, None)
    (Required for new resource) Credential group details.


  purpose (True, str, None)
    (Required for new resource) Purpose for which the credential is created.


  enabled (True, bool, None)
    (Required for new resource) Credentials status enabled/disbaled.


  type (True, str, None)
    (Required for new resource) Credentials type.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

