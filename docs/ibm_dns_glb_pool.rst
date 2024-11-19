
ibm_dns_glb_pool -- Configure IBM Cloud 'ibm_dns_glb_pool' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dns_glb_pool' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/dns_glb_pool

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  name (True, str, None)
    (Required for new resource) The unique identifier of a service instance.


  monitor (False, str, None)
    The ID of the load balancer monitor to be associated to this pool


  origins (True, list, None)
    (Required for new resource) Origins info


  healthcheck_subnets (False, list, None)
    Health check subnet crn of VSIs


  instance_id (True, str, None)
    (Required for new resource) Instance Id


  healthy_origins_threshold (False, int, None)
    The minimum number of origins that must be healthy for this pool to serve traffic


  notification_channel (False, str, None)
    The notification channel,It is a webhook url


  healthcheck_region (False, str, None)
    Health check region of VSIs


  description (False, str, None)
    Descriptive text of the load balancer pool


  enabled (False, bool, None)
    Whether the load balancer pool is enabled


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

