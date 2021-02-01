
ibm_compute_autoscale_policy -- Configure IBM Cloud 'ibm_compute_autoscale_policy' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_compute_autoscale_policy' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.16.1
- Terraform v0.12.20



Parameters
----------

  triggers (False, list, None)
    None


  tags (False, list, None)
    List of tags


  name (True, str, None)
    (Required for new resource) Name


  scale_type (True, str, None)
    (Required for new resource) scale type


  scale_amount (True, int, None)
    (Required for new resource) Scale amount


  cooldown (False, int, None)
    cooldown value


  scale_group_id (True, int, None)
    (Required for new resource) scale group ID


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

