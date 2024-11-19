
ibm_sm_imported_certificate -- Configure IBM Cloud 'ibm_sm_imported_certificate' resource
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_sm_imported_certificate' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/sm_imported_certificate

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  version_custom_metadata (False, dict, None)
    The secret version metadata that a user can customize.


  private_key (False, str, None)
    (Optional) The PEM-encoded private key to associate with the certificate.


  secret_group_id (False, str, None)
    A v4 UUID identifier, or `default` secret group.


  instance_id (True, str, None)
    (Required for new resource) The ID of the Secrets Manager instance.


  labels (False, list, None)
    Labels that you can use to search for secrets in your instance.Up to 30 labels can be created.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  intermediate (False, str, None)
    (Optional) The PEM-encoded intermediate certificate to associate with the root certificate.


  endpoint_type (False, str, None)
    public or private.


  name (True, str, None)
    (Required for new resource) A human-readable name to assign to your secret.To protect your privacy, do not use personal data, such as your name or location, as a name for your secret.


  certificate (True, str, None)
    (Required for new resource) The PEM-encoded contents of your certificate.


  custom_metadata (False, dict, None)
    The secret metadata that a user can customize.


  description (False, str, None)
    An extended description of your secret.To protect your privacy, do not use personal data, such as your name or location, as a description for your secret group.


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

