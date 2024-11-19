
ibm_hpcs_key_template -- Configure IBM Cloud 'ibm_hpcs_key_template' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_hpcs_key_template' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/hpcs_key_template

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  name (True, str, None)
    (Required for new resource) Name of the template, it will be referenced when creating managed keys.


  key (True, list, None)
    (Required for new resource) Properties describing the properties of the managed key.


  uko_vault (True, str, None)
    (Required for new resource) The UUID of the Vault in which the update is to take place.


  vault (True, list, None)
    (Required for new resource) ID of the Vault where the entity is to be created in.


  keystores (True, list, None)
    (Required for new resource) An array describing the type and group of target keystores the managed key is to be installed in.


  description (False, str, None)
    Description of the key template.


  instance_id (True, str, None)
    (Required for new resource) The ID of the UKO instance this resource exists in.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

