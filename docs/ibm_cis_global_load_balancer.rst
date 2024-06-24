
ibm_cis_global_load_balancer -- Configure IBM Cloud 'ibm_cis_global_load_balancer' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_global_load_balancer' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cis_global_load_balancer

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  proxied (False, bool, False)
    set to true if proxy needs to be enabled


  session_affinity (False, str, none)
    Session affinity info


  enabled (False, bool, True)
    set to true of LB needs to enabled


  pop_pools (False, list, None)
    None


  fallback_pool_id (True, str, None)
    (Required for new resource) fallback pool ID


  ttl (False, int, 60)
    TTL value


  domain_id (True, str, None)
    (Required for new resource) Associated CIS domain


  name (True, str, None)
    (Required for new resource) name


  default_pool_ids (True, list, None)
    (Required for new resource) List of default Pool IDs


  description (False, str, None)
    Description for the load balancer instance


  steering_policy (False, str, None)
    Steering policy info


  region_pools (False, list, None)
    None


  cis_id (True, str, None)
    (Required for new resource) CIS instance crn


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

