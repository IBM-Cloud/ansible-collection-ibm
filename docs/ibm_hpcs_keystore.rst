
ibm_hpcs_keystore -- Configure IBM Cloud 'ibm_hpcs_keystore' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_hpcs_keystore' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/hpcs_keystore

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.49.0
- Terraform v0.12.20



Parameters
----------

  ibm_variant (False, str, None)
    Possible IBM Cloud KMS variants.


  ibm_iam_endpoint (False, str, None)
    Endpoint of the IAM service for this IBM Cloud keystore.


  ibm_key_ring (False, str, None)
    The key ring of an IBM Cloud KMS Keystore.


  azure_service_name (False, str, None)
    Service name of the key vault instance from the Azure portal.


  ibm_api_key (False, str, None)
    The IBM Cloud API key to be used for connecting to this IBM Cloud keystore.


  ibm_instance_id (False, str, None)
    The instance ID of the IBM Cloud keystore.


  vault (True, list, None)
    (Required for new resource) Reference to a vault.


  azure_subscription_id (False, str, None)
    Subscription ID in Azure.


  description (False, str, None)
    Description of the keystore.


  aws_secret_access_key (False, str, None)
    The secret access key used for connecting to this instance of AWS KMS.


  azure_location (False, str, None)
    Location of the Azure Key Vault.


  azure_environment (False, str, None)
    Azure environment, usually 'Azure'.


  name (False, str, None)
    Name of the target keystore. It can be changed in the future.


  groups (False, list, None)
    List of groups that this keystore belongs to.


  azure_tenant (False, str, None)
    Azure tenant that the Key Vault is associated with,.


  ibm_api_endpoint (False, str, None)
    API endpoint of the IBM Cloud keystore.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  uko_vault (True, str, None)
    (Required for new resource) The UUID of the Vault in which the update is to take place.


  aws_region (False, str, None)
    AWS Region.


  azure_resource_group (False, str, None)
    Resource group in Azure.


  instance_id (True, str, None)
    (Required for new resource) The ID of the UKO instance this resource exists in.


  aws_access_key_id (False, str, None)
    The access key id used for connecting to this instance of AWS KMS.


  azure_service_principal_client_id (False, str, None)
    Azure service principal client ID.


  type (True, str, None)
    (Required for new resource) Type of keystore.


  azure_service_principal_password (False, str, None)
    Azure service principal password.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

