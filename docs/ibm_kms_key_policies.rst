
ibm_kms_key_policies -- Configure IBM Cloud 'ibm_kms_key_policies' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_kms_key_policies' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/kms_key_policies

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.51.0
- Terraform v0.12.20



Parameters
----------

  rotation (False, list, None)
    Specifies the key rotation time interval in months, with a minimum of 1, and a maximum of 12


  dual_auth_delete (False, list, None)
    Data associated with the dual authorization delete policy.


  instance_id (True, str, None)
    (Required for new resource) Key protect or hpcs instance GUID


  key_id (False, str, None)
    Key ID


  alias (False, str, None)
    None


  endpoint_type (False, str, public)
    public or private


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

