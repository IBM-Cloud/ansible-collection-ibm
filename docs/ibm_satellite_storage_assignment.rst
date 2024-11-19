
ibm_satellite_storage_assignment -- Configure IBM Cloud 'ibm_satellite_storage_assignment' resource
===================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_satellite_storage_assignment' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/satellite_storage_assignment

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  cluster (False, str, None)
    ID of the Satellite cluster or Service Cluster that you want to apply the configuration to.


  update_config_revision (False, bool, False)
    Updating an assignment to the latest available storage configuration version.


  groups (False, list, None)
    One or more cluster groups on which you want to apply the configuration. Note that at least one cluster group is required.


  config (True, str, None)
    (Required for new resource) Storage Configuration Name or ID.


  controller (False, str, None)
    The Name or ID of the Satellite Location.


  assignment_name (True, str, None)
    (Required for new resource) Name of the Assignment.


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

