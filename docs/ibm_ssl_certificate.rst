
ibm_ssl_certificate -- Configure IBM Cloud 'ibm_ssl_certificate' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_ssl_certificate' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  technical_contact_same_as_org_address_flag (False, bool, False)
    NA


  administrative_contact_same_as_technical_flag (False, bool, False)
    NA


  billing_contact_same_as_technical_flag (False, bool, False)
    NA


  server_count (False, int, None)
    (Required for new resource) NA


  server_type (False, str, None)
    (Required for new resource) NA


  order_approver_email_address (False, str, None)
    (Required for new resource) NA


  organization_information (False, list, None)
    (Required for new resource) NA


  technical_contact (False, list, None)
    (Required for new resource) NA


  billing_contact (False, list, None)
    NA


  validity_months (False, int, None)
    (Required for new resource) NA


  ssl_type (False, str, None)
    (Required for new resource) NA


  certificate_signing_request (False, str, None)
    (Required for new resource) NA


  renewal_flag (False, bool, True)
    NA


  administrative_address_same_as_organization_flag (False, bool, False)
    NA


  billing_address_same_as_organization_flag (False, bool, False)
    NA


  administrative_contact (False, list, None)
    NA


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

