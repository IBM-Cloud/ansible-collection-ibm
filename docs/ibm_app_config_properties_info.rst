
ibm_app_config_properties_info -- Retrieve IBM Cloud 'ibm_app_config_properties' resource
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_app_config_properties' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/app_config_properties

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  limit (False, int, None)
    The number of records to retrieve. By default, the list operation return the first 10 records. To retrieve different set of records, use `limit` with `offset` to page through the available records.


  offset (False, int, None)
    The number of records to skip. By specifying `offset`, you retrieve a subset of items that starts with the `offset` value. Use `offset` with `limit` to page through the available records.


  tags (False, str, None)
    Filter the resources to be returned based on the associated tags. Specify the parameter as a list of comma separated tags. Returns resources associated with any of the specified tags.


  collections (False, list, None)
    Filter features by a list of comma separated collections.


  segments (False, list, None)
    Filter features by a list of comma separated segments.


  expand (False, bool, None)
    If set to `true`, returns expanded view of the resource details.


  include (False, list, None)
    Include the associated collections or targeting rules details in the response.


  guid (True, str, None)
    GUID of the App Configuration service. Get it from the service instance credentials section of the dashboard.


  environment_id (True, str, None)
    Environment Id.


  sort (False, str, None)
    Sort the feature details based on the specified attribute.


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

