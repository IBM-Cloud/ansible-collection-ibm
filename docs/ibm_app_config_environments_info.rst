
ibm_app_config_environments_info -- Retrieve IBM Cloud 'ibm_app_config_environments' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_app_config_environments' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/app_config_environments

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.38.2
- Terraform v0.12.20



Parameters
----------

  tags (False, str, None)
    filter the resources to be returned based on the associated tags. Returns resources associated with any of the specified tags.


  limit (False, int, None)
    The number of records to retrieve. By default, the list operation return the first 10 records. To retrieve different set of records, use `limit` with `offset` to page through the available records.


  guid (True, str, None)
    GUID of the App Configuration service. Get it from the service instance credentials section of the dashboard.


  expand (False, bool, None)
    If set to `true`, returns expanded view of the resource details.


  offset (False, int, None)
    The number of records to skip. By specifying `offset`, you retrieve a subset of items that starts with the `offset` value. Use `offset` with `limit` to page through the available records.


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

