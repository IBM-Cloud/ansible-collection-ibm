
ibm_dns_glb -- Configure IBM Cloud 'ibm_dns_glb' resource
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dns_glb' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/dns_glb

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  zone_id (True, str, None)
    (Required for new resource) Zone Id


  name (True, str, None)
    (Required for new resource) Name of the load balancer


  default_pools (True, list, None)
    (Required for new resource) A list of pool IDs ordered by their failover priority


  instance_id (True, str, None)
    (Required for new resource) The GUID of the private DNS.


  description (False, str, None)
    Descriptive text of the load balancer


  enabled (False, bool, None)
    Whether the load balancer is enabled


  ttl (False, int, 60)
    Time to live in second


  fallback_pool (True, str, None)
    (Required for new resource) The pool ID to use when all other pools are detected as unhealthy


  az_pools (False, list, None)
    Map availability zones to pool ID's.


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

