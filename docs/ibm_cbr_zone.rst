
ibm_cbr_zone -- Configure IBM Cloud 'ibm_cbr_zone' resource
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cbr_zone' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cbr_zone

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  description (False, str, None)
    The description of the zone.


  x_correlation_id (False, str, None)
    The supplied or generated value of this header is logged for a request and repeated in a response header for the corresponding response. The same value is used for downstream requests and retries of those requests. If a value of this headers is not supplied in a request, the service generates a random (version 4) UUID.


  transaction_id (False, str, None)
    The `Transaction-Id` header behaves as the `X-Correlation-Id` header. It is supported for backward compatibility with other IBM platform services that support the `Transaction-Id` header only. If both `X-Correlation-Id` and `Transaction-Id` are provided, `X-Correlation-Id` has the precedence over `Transaction-Id`.


  addresses (False, list, None)
    The list of addresses in the zone.


  name (True, str, None)
    (Required for new resource) The name of the zone.


  excluded (False, list, None)
    The list of excluded addresses in the zone. Only addresses of type `ipAddress`, `ipRange`, and `subnet` can be excluded.


  account_id (True, str, None)
    (Required for new resource) The id of the account owning this zone.


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

