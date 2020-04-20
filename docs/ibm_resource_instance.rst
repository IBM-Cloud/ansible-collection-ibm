
ibm_resource_instance -- Configure IBM Cloud 'ibm_resource_instance' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_resource_instance' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  resource_group_id (False, str, None)
    The resource group id


  parameters (False, dict, None)
    Arbitrary parameters to pass. Must be a JSON object


  guid (False, str, None)
    Guid of resource instance


  resource_status (False, str, None)
    The status of the resource


  name (False, str, None)
    (Required for new resource) A name for the resource instance


  location (False, str, None)
    (Required for new resource) The location where the instance available


  tags (False, list, None)
    NA


  crn (False, str, None)
    CRN of resource instance


  service_endpoints (False, str, None)
    Types of the service endpoints. Possible values are 'public', 'private', 'public-and-private'.


  service (False, str, None)
    (Required for new resource) The name of the service offering like cloud-object-storage, kms etc


  status (False, str, None)
    Status of resource instance


  resource_crn (False, str, None)
    The crn of the resource


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  plan (False, str, None)
    (Required for new resource) The plan type of the service


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about the resource


  resource_name (False, str, None)
    The name of the resource


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

