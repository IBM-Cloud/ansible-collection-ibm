
ibm_hpcs_managed_key -- Configure IBM Cloud 'ibm_hpcs_managed_key' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_hpcs_managed_key' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/hpcs_managed_key

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  template_name (True, str, None)
    (Required for new resource) Name of the key template to use when creating a key.


  label (True, str, None)
    (Required for new resource) The label of the key.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  uko_vault (True, str, None)
    (Required for new resource) The UUID of the Vault in which the update is to take place.


  tags (False, list, None)
    Key-value pairs associated with the key.


  instance_id (True, str, None)
    (Required for new resource) The ID of the UKO instance this resource exists in.


  vault (True, list, None)
    (Required for new resource) ID of the Vault where the entity is to be created in.


  description (False, str, None)
    Description of the managed key.


  state_ (False, str, None)
    The state of the key.


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

