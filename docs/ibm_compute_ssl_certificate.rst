
ibm_compute_ssl_certificate -- Configure IBM Cloud 'ibm_compute_ssl_certificate' resource
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_compute_ssl_certificate' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  create_date (False, str, None)
    certificate creation date


  modify_date (False, str, None)
    certificate modificatiob date


  intermediate_certificate (False, str, None)
    Intermediate certificate value


  private_key (True, str, None)
    (Required for new resource) SSL Private Key


  organization_name (False, str, None)
    Organization name


  validity_begin (False, str, None)
    Validity begins from


  validity_end (False, str, None)
    Validity ends before


  key_size (False, int, None)
    SSL key size


  certificate (True, str, None)
    (Required for new resource) SSL Certifcate


  common_name (False, str, None)
    Common name


  validity_days (False, int, None)
    Validity days


  tags (False, list, None)
    Tags set for resource


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

