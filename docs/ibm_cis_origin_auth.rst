
ibm_cis_origin_auth -- Configure IBM Cloud 'ibm_cis_origin_auth' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_origin_auth' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cis_origin_auth

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  cis_id (True, str, None)
    (Required for new resource) CIS instance crn


  level (True, str, None)
    (Required for new resource) Origin auth level zone or hostname


  hostname (False, str, None)
    Host name needed for host level authentication


  private_key (True, str, None)
    (Required for new resource) Private key content which needs to be uploaded


  domain_id (True, str, None)
    (Required for new resource) Associated CIS domain


  enabled (False, bool, True)
    Enabel-disable origin auth for a zone or host


  certificate (True, str, None)
    (Required for new resource) Certificate content which needs to be uploaded


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

