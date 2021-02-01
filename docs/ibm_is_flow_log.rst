
ibm_is_flow_log -- Configure IBM Cloud 'ibm_is_flow_log' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_flow_log' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.20.0
- Terraform v0.12.20



Parameters
----------

  name (True, str, None)
    (Required for new resource) Flow Log Collector name


  storage_bucket (True, str, None)
    (Required for new resource) The Cloud Object Storage bucket name where the collected flows will be logged


  active (False, bool, True)
    Indicates whether this collector is active


  resource_group (False, str, None)
    The resource group of flow log


  target (True, str, None)
    (Required for new resource) The target id that the flow log collector is to collect flow logs


  tags (False, list, None)
    Tags for the VPC Flow logs


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

