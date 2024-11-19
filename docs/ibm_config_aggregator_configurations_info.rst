
ibm_config_aggregator_configurations_info -- Retrieve IBM Cloud 'ibm_config_aggregator_configurations' resource
===============================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_config_aggregator_configurations' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/config_aggregator_configurations

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  sub_account (False, str, None)
    Filter the resource configurations from the specified sub-account in an enterprise hierarchy.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  config_type (False, str, None)
    The type of resource configuration that are to be retrieved.


  service_name (False, str, None)
    The name of the IBM Cloud service for which resources are to be retrieved.


  resource_group_id (False, str, None)
    The resource group id of the resources.


  location (False, str, None)
    The location or region in which the resources are created.


  instance_id (True, str, None)
    The ID of the configuration aggregator instance.


  resource_crn (False, str, None)
    The crn of the resource.


  access_tags (False, str, None)
    Filter the resource configurations attached with the specified access tags.


  user_tags (False, str, None)
    Filter the resource configurations attached with the specified user tags.


  service_tags (False, str, None)
    Filter the resource configurations attached with the specified service tags.


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

