
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

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  uko_vault (True, str, None)
    (Required for new resource) The UUID of the Vault in which the update is to take place.


  aws_region (False, str, None)
    AWS Region.


  aws_access_key_id (False, str, None)
    The access key id used for connecting to this instance of AWS KMS.


  type (True, str, None)
    (Required for new resource) Type of keystore.


  azure_resource_group (False, str, None)
    Resource group in Azure.


  azure_location (False, str, None)
    Location of the Azure Key Vault.


  ibm_iam_endpoint (False, str, None)
    Endpoint of the IAM service for this IBM Cloud keystore.


  google_credentials (False, str, None)
    The value of the JSON key represented in the Base64 format.


  google_private_key_id (False, str, None)
    The private key id associated with this keystore.


  aws_secret_access_key (False, str, None)
    The secret access key used for connecting to this instance of AWS KMS.


  azure_service_principal_client_id (False, str, None)
    Azure service principal client ID.


  groups (False, list, None)
    List of groups that this keystore belongs to.


  dry_run (False, bool, False)
    Do not create a keystore, only verify if keystore created with given parameters can be communciated with successfully.


  azure_service_principal_password (False, str, None)
    Azure service principal password.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  google_location (False, str, None)
    Location represents the geographical region where a Cloud KMS resource is stored and can be accessed. A key's location impacts the performance of applications using the key.


  azure_tenant (False, str, None)
    Azure tenant that the Key Vault is associated with,.


  vault (True, list, None)
    (Required for new resource) Reference to a vault.


  ibm_instance_id (False, str, None)
    The instance ID of the IBM Cloud keystore.


  ibm_key_ring (False, str, None)
    The key ring of an IBM Cloud KMS Keystore.


  azure_service_name (False, str, None)
    Service name of the key vault instance from the Azure portal.


  azure_subscription_id (False, str, None)
    Subscription ID in Azure.


  azure_environment (False, str, None)
    Azure environment, usually 'Azure'.


  ibm_api_endpoint (False, str, None)
    API endpoint of the IBM Cloud keystore.


  ibm_api_key (False, str, None)
    The IBM Cloud API key to be used for connecting to this IBM Cloud keystore.


  description (False, str, None)
    Description of the keystore.


  instance_id (True, str, None)
    (Required for new resource) The ID of the UKO instance this resource exists in.


  google_project_id (False, str, None)
    The project id associated with this keystore.


  google_key_ring (False, str, None)
    A key ring organizes keys in a specific Google Cloud location and allows you to manage access control on groups of keys.


  ibm_variant (False, str, None)
    Possible IBM Cloud KMS variants.


  name (False, str, None)
    Name of the target keystore. It can be changed in the future.


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

