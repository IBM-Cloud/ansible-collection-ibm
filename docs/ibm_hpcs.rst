
ibm_hpcs -- Configure IBM Cloud 'ibm_hpcs' resource
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_hpcs' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/hpcs

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.38.2
- Terraform v0.12.20



Parameters
----------

  failover_units (False, int, None)
    The number of failover crypto units for your service instance


  admins (True, list, None)
    (Required for new resource) Crypto Unit Administrators


  revocation_threshold (True, int, None)
    (Required for new resource) Revocation Threshold Value


  location (True, str, None)
    (Required for new resource) The location where the HPCS instance available


  units (True, int, None)
    (Required for new resource) The number of operational crypto units for your service instance


  resource_group_id (False, str, None)
    The resource group id


  name (True, str, None)
    (Required for new resource) A name for the HPCS instance


  tags (False, list, None)
    None


  signature_threshold (True, int, None)
    (Required for new resource) Signature Threshold Value


  plan (True, str, None)
    (Required for new resource) The plan type of the HPCS Instance


  signature_server_url (False, str, None)
    URL of signing service


  service (False, str, hs-crypto)
    The name of the service offering `hs-crypto`


  service_endpoints (False, str, None)
    Types of the service endpoints. Possible values are `public-and-private`, `private-only`.


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

