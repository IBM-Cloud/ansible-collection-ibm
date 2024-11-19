
ibm_sm_public_certificate_configuration_dns_cis -- Configure IBM Cloud 'ibm_sm_public_certificate_configuration_dns_cis' resource
=================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_sm_public_certificate_configuration_dns_cis' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/sm_public_certificate_configuration_dns_cis

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  cloud_internet_services_crn (True, str, None)
    (Required for new resource) A CRN that uniquely identifies an IBM Cloud resource.


  endpoint_type (False, str, None)
    public or private.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  name (True, str, None)
    (Required for new resource) A human-readable unique name to assign to your configuration.To protect your privacy, do not use personal data, such as your name or location, as an name for your secret.


  cloud_internet_services_apikey (False, str, None)
    An IBM Cloud API key that can to list domains in your Cloud Internet Services instance.To grant Secrets Manager the ability to view the Cloud Internet Services instance and all of its domains, the API key must be assigned the Reader service role on Internet Services (`internet-svcs`).If you need to manage specific domains, you can assign the Manager role. For production environments, it is recommended that you assign the Reader access role, and then use the[IAM Policy Management API](https://cloud.ibm.com/apidocs/iam-policy-management#create-policy) to control specific domains. For more information, see the [docs](https://cloud.ibm.com/docs/secrets-manager?topic=secrets-manager-prepare-order-certificates#authorize-specific-domains).


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

