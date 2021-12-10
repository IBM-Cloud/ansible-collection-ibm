
ibm_cloudant -- Configure IBM Cloud 'ibm_cloudant' resource
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cloudant' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cloudant

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.37.1
- Terraform v0.12.20



Parameters
----------

  service_endpoints (False, str, None)
    Types of the service endpoints. Possible values are 'public', 'private', 'public-and-private'.


  capacity (False, int, 1)
    A number of blocks of throughput units. A block consists of 100 reads/sec, 50 writes/sec, and 5 global queries/sec of provisioned throughput capacity.


  enable_cors (False, bool, True)
    Boolean value to turn CORS on and off.


  parameters (False, dict, None)
    Arbitrary parameters to pass. Must be a JSON object


  legacy_credentials (False, bool, False)
    Use both legacy credentials and IAM for authentication


  environment_crn (False, str, None)
    CRN of the IBM Cloudant Dedicated Hardware plan instance


  resource_group_id (False, str, None)
    The resource group id


  cors_config (False, list, None)
    Configuration for CORS.


  name (True, str, None)
    (Required for new resource) A name for the resource instance


  tags (False, list, None)
    None


  location (True, str, None)
    (Required for new resource) The location where the instance available


  include_data_events (False, bool, False)
    Include data event types in events sent to IBM Cloud Activity Tracker with LogDNA for the IBM Cloudant instance. By default only emitted events are of "management" type.


  plan (True, str, None)
    (Required for new resource) The plan type of the service


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

