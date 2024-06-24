
ibm_dns_custom_resolver_secondary_zone -- Configure IBM Cloud 'ibm_dns_custom_resolver_secondary_zone' resource
===============================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dns_custom_resolver_secondary_zone' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/dns_custom_resolver_secondary_zone

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  enabled (True, bool, None)
    (Required for new resource) Enable/Disable the secondary zone


  zone (True, str, None)
    (Required for new resource) The name of the zone.


  resolver_id (True, str, None)
    (Required for new resource) The unique identifier of a custom resolver.


  transfer_from (True, list, None)
    (Required for new resource) The addresses of DNS servers where the secondary zone data should be transferred from


  description (False, str, None)
    Descriptive text of the secondary zone


  instance_id (True, str, None)
    (Required for new resource) The unique identifier of a service instance.


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

