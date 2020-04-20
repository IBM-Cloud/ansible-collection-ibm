
ibm_certificate_manager_order -- Configure IBM Cloud 'ibm_certificate_manager_order' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_certificate_manager_order' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  rotate_keys (False, bool, False)
    NA


  description (False, str, None)
    NA


  issuer (False, str, None)
    NA


  issuance_info (False, dict, None)
    NA


  name (False, str, None)
    (Required for new resource) NA


  domains (False, list, None)
    (Required for new resource) NA


  begins_on (False, int, None)
    NA


  imported (False, bool, None)
    NA


  certificate_manager_instance_id (False, str, None)
    (Required for new resource) NA


  algorithm (False, str, None)
    NA


  status (False, str, None)
    NA


  has_previous (False, str, None)
    NA


  domain_validation_method (False, str, dns - 01)
    NA


  dns_provider_instance_crn (False, str, None)
    NA


  key_algorithm (False, str, None)
    NA


  expires_on (False, int, None)
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

