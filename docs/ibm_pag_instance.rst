
ibm_pag_instance -- Configure IBM Cloud 'ibm_pag_instance' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pag_instance' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pag_instance

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  service (True, str, None)
    (Required for new resource) The name of the service offering like cloud-object-storage, kms etc


  parameters (False, dict, None)
    Arbitrary parameters to pass. Must be a JSON object


  tags (False, list, None)
    None


  plan (True, str, None)
    (Required for new resource) The plan type of the service


  service_endpoints (False, str, None)
    Types of the service endpoints. Possible values are 'public', 'private', 'public-and-private'.


  location (True, str, None)
    (Required for new resource) The location where the instance available


  parameters_json (False, str, None)
    Arbitrary parameters to pass in Json string format


  name (True, str, None)
    (Required for new resource) A name for the resource instance


  resource_group_id (False, str, None)
    The resource group id


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

