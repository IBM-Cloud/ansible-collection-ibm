
ibm_sm_public_certificate_configuration_ca_lets_encrypt -- Configure IBM Cloud 'ibm_sm_public_certificate_configuration_ca_lets_encrypt' resource
=================================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_sm_public_certificate_configuration_ca_lets_encrypt' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/sm_public_certificate_configuration_ca_lets_encrypt

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  name (True, str, None)
    (Required for new resource) A human-readable unique name to assign to your configuration.To protect your privacy, do not use personal data, such as your name or location, as an name for your secret.


  lets_encrypt_preferred_chain (False, str, None)
    Prefer the chain with an issuer matching this Subject Common Name.


  lets_encrypt_private_key (True, str, None)
    (Required for new resource) The PEM encoded private key of your Lets Encrypt account.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  endpoint_type (False, str, None)
    public or private.


  lets_encrypt_environment (True, str, None)
    (Required for new resource) The configuration of the Let's Encrypt CA environment.


  instance_id (True, str, None)
    (Required for new resource) The ID of the Secrets Manager instance.


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

