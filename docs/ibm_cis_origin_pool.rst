
ibm_cis_origin_pool -- Configure IBM Cloud 'ibm_cis_origin_pool' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_origin_pool' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cis_origin_pool

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  cis_id (True, str, None)
    (Required for new resource) CIS instance crn


  name (True, str, None)
    (Required for new resource) name


  monitor (False, str, None)
    Monitor value


  minimum_origins (False, int, 1)
    Minimum number of Origins


  notification_email (False, str, None)
    Email address configured to recieve the notifications


  check_regions (True, list, None)
    (Required for new resource) List of regions


  description (False, str, None)
    Description of the CIS Origin Pool


  enabled (True, bool, None)
    (Required for new resource) Boolean value set to true if cis origin pool needs to be enabled


  origins (True, list, None)
    (Required for new resource) Origins info


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

