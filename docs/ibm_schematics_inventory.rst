
ibm_schematics_inventory -- Configure IBM Cloud 'ibm_schematics_inventory' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_schematics_inventory' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/schematics_inventory

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  inventories_ini (False, str, None)
    Input inventory of host and host group for the playbook, in the `.ini` file format.


  resource_group (False, str, None)
    Resource-group name for the Inventory definition.   By default, Inventory definition will be created in Default Resource Group.


  description (False, str, None)
    The description of your Inventory definition. The description can be up to 2048 characters long in size.


  location (False, str, None)
    List of locations supported by IBM Cloud Schematics service.  While creating your workspace or action, choose the right region, since it cannot be changed.  Note, this does not limit the location of the IBM Cloud resources, provisioned using Schematics.


  resource_queries (False, list, None)
    Input resource query definitions that is used to dynamically generate the inventory of host and host group for the playbook.


  name (False, str, None)
    The unique name of your Inventory definition. The name can be up to 128 characters long and can include alphanumeric characters, spaces, dashes, and underscores.


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

