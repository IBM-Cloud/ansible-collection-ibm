
ibm_ssl_certificate -- Configure IBM Cloud 'ibm_ssl_certificate' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_ssl_certificate' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/ssl_certificate

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  validity_months (True, int, None)
    (Required for new resource) vslidity of the ssl certificate in month


  ssl_type (True, str, None)
    (Required for new resource) ssl type


  technical_contact_same_as_org_address_flag (False, bool, False)
    Technical contact same as org address flag


  administrative_address_same_as_organization_flag (False, bool, False)
    administrative address same as organization flag


  organization_information (True, list, None)
    (Required for new resource) Organization information


  billing_contact (False, list, None)
    None


  certificate_signing_request (True, str, None)
    (Required for new resource) certificate signing request info


  administrative_contact_same_as_technical_flag (False, bool, False)
    Administrative contact same as technical flag


  technical_contact (True, list, None)
    (Required for new resource) Technical contact info


  order_approver_email_address (True, str, None)
    (Required for new resource) Email address of the approver


  server_count (True, int, None)
    (Required for new resource) Server count


  server_type (True, str, None)
    (Required for new resource) server type


  renewal_flag (False, bool, True)
    Renewal flag


  billing_contact_same_as_technical_flag (False, bool, False)
    billing contact


  billing_address_same_as_organization_flag (False, bool, False)
    billing address same as organization flag


  administrative_contact (False, list, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

