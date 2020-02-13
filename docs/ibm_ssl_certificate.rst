
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

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  server_type (False, str, None)
    (Required for new resource)


  validity_months (False, int, None)
    (Required for new resource)


  certificate_signing_request (False, str, None)
    (Required for new resource)


  ssl_type (False, str, None)
    (Required for new resource)


  billing_address_same_as_organization_flag (False, bool, False)
    None


  organization_information (False, list, None)
    (Required for new resource)


  billing_contact (False, list, None)
    None


  technical_contact_same_as_org_address_flag (False, bool, False)
    None


  technical_contact (False, list, None)
    (Required for new resource)


  server_count (False, int, None)
    (Required for new resource)


  renewal_flag (False, bool, True)
    None


  order_approver_email_address (False, str, None)
    (Required for new resource)


  administrative_contact_same_as_technical_flag (False, bool, False)
    None


  billing_contact_same_as_technical_flag (False, bool, False)
    None


  administrative_address_same_as_organization_flag (False, bool, False)
    None


  administrative_contact (False, list, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

