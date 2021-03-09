
ibm_cis_global_load_balancer -- Configure IBM Cloud 'ibm_cis_global_load_balancer' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_global_load_balancer' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.21.1
- Terraform v0.12.20



Parameters
----------

  description (False, str, None)
    Description for the load balancer instance


  ttl (False, int, 60)
    TTL value


  region_pools (False, list, None)
    None


  cis_id (True, str, None)
    (Required for new resource) CIS instance crn


  enabled (False, bool, True)
    set to true of LB needs to enabled


  domain_id (True, str, None)
    (Required for new resource) Associated CIS domain


  default_pool_ids (True, list, None)
    (Required for new resource) List of default Pool IDs


  fallback_pool_id (True, str, None)
    (Required for new resource) fallback pool ID


  proxied (False, bool, False)
    set to true if proxy needs to be enabled


  session_affinity (False, str, none)
    Session affinity info


  pop_pools (False, list, None)
    None


  name (True, str, None)
    (Required for new resource) name


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

