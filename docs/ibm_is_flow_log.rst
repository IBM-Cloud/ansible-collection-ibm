
ibm_is_flow_log -- Configure IBM Cloud 'ibm_is_flow_log' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_flow_log' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_flow_log

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  storage_bucket (True, str, None)
    (Required for new resource) The Cloud Object Storage bucket name where the collected flows will be logged


  target (True, str, None)
    (Required for new resource) The target id that the flow log collector is to collect flow logs


  resource_group (False, str, None)
    The resource group of flow log


  access_tags (False, list, None)
    List of access management tags


  name (True, str, None)
    (Required for new resource) Flow Log Collector name


  active (False, bool, True)
    Indicates whether this collector is active


  tags (False, list, None)
    Tags for the VPC Flow logs


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

