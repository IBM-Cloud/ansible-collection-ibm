
ibm_appid_cloud_directory_template -- Configure IBM Cloud 'ibm_appid_cloud_directory_template' resource
=======================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_appid_cloud_directory_template' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/appid_cloud_directory_template

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  tenant_id (True, str, None)
    (Required for new resource) The AppID instance GUID


  template_name (True, str, None)
    (Required for new resource) The type of email template. This can be `USER_VERIFICATION`, `WELCOME`, `PASSWORD_CHANGED`, `RESET_PASSWORD` or `MFA_VERIFICATION`


  language (False, str, en)
    Preferred language for resource. Format as described at RFC5646. According to the configured languages codes returned from the `GET /management/v4/{tenantId}/config/ui/languages API`.


  subject (True, str, None)
    (Required for new resource) The subject of the email


  html_body (False, str, None)
    The HTML body of the email


  plain_text_body (False, str, None)
    The text body of the email.


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

