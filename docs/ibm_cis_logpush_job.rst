
ibm_cis_logpush_job -- Configure IBM Cloud 'ibm_cis_logpush_job' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_logpush_job' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cis_logpush_job

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.50.0
- Terraform v0.12.20



Parameters
----------

  frequency (False, str, None)
    The frequency at which CIS sends batches of logs to your destination


  cis_id (True, str, None)
    (Required for new resource) CIS instance crn


  logdna (True, str, None)
    (Required for new resource) Information to identify the LogDNA instance the data will be pushed.


  name (False, str, None)
    Logpush Job Name


  enabled (False, bool, None)
    Whether the logpush job enabled or not


  domain_id (True, str, None)
    (Required for new resource) Associated CIS domain


  logpull_options (False, str, None)
    Configuration string


  dataset (True, str, None)
    (Required for new resource) Dataset to be pulled


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

