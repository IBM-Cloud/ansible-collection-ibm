
ibm_tg_connection_prefix_filter -- Configure IBM Cloud 'ibm_tg_connection_prefix_filter' resource
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_tg_connection_prefix_filter' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/tg_connection_prefix_filter

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.51.0
- Terraform v0.12.20



Parameters
----------

  prefix (True, str, None)
    (Required for new resource) IP Prefix


  before (False, str, None)
    Identifier of prefix filter that handles ordering


  ge (False, int, None)
    IP Prefix GE


  le (False, int, None)
    IP Prefix LE


  gateway (True, str, None)
    (Required for new resource) The Transit Gateway identifier


  connection_id (True, str, None)
    (Required for new resource) The Transit Gateway Connection identifier


  action (True, str, None)
    (Required for new resource) Whether to permit or deny the prefix filter


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

