
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

- IBM-Cloud terraform-provider-ibm v1.5.2
- Terraform v0.12.20



Parameters
----------

  ssl_type (False, str, None)
    (Required for new resource) ssl type


  renewal_flag (False, bool, True)
    Renewal flag


  technical_contact_same_as_org_address_flag (False, bool, False)
    Technical contact same as org address flag


  server_type (False, str, None)
    (Required for new resource) server type


  validity_months (False, int, None)
    (Required for new resource) vslidity of the ssl certificate in month


  certificate_signing_request (False, str, None)
    (Required for new resource) certificate signing request info


  billing_contact_same_as_technical_flag (False, bool, False)
    billing contact


  billing_address_same_as_organization_flag (False, bool, False)
    billing address same as organization flag


  organization_information (False, list, None)
    (Required for new resource) Organization information


  server_count (False, int, None)
    (Required for new resource) Server count


  order_approver_email_address (False, str, None)
    (Required for new resource) Email address of the approver


  administrative_contact_same_as_technical_flag (False, bool, False)
    Administrative contact same as technical flag


  administrative_address_same_as_organization_flag (False, bool, False)
    administrative address same as organization flag


  technical_contact (False, list, None)
    (Required for new resource) Technical contact info


  billing_contact (False, list, None)
    None


  administrative_contact (False, list, None)
    None


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

