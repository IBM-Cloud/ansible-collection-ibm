
ibm_api_gateway_endpoint -- Configure IBM Cloud 'ibm_api_gateway_endpoint' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_api_gateway_endpoint' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/api_gateway_endpoint

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  open_api_doc_name (True, str, None)
    (Required for new resource) Json File path


  name (True, str, None)
    (Required for new resource) Endpoint name


  routes (False, list, None)
    Invokable routes for an endpoint


  managed (False, bool, False)
    Managed indicates if endpoint is online or offline.


  provider_id (False, str, user-defined)
    Provider ID of an endpoint allowable values user-defined and whisk


  type (False, str, unshare)
    Action type of Endpoint ALoowable values are share, unshare, manage, unmanage


  service_instance_crn (True, str, None)
    (Required for new resource) Api Gateway Service Instance Crn


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

