
ibm_resource_instance_info -- Retrieve IBM Cloud 'ibm_resource_instance' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_resource_instance' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/resource_instance

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  resource_group_id (False, str, None)
    The id of the resource group in which the instance is present


  service (False, str, None)
    The service type of the instance


  identifier (False, str, None)
    Resource instance guid


  location (False, str, None)
    The location or the environment in which instance exists


  name (False, str, None)
    Resource instance name for example, myobjectstorage


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

