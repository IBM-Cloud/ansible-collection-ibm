
ibm_database -- Configure IBM Cloud 'ibm_database' resource
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_database' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  resource_group_id (False, str, None)
    The id of the resource group in which the Database instance is present


  service (True, str, None)
    (Required for new resource) The name of the Cloud Internet database service


  allowlist (False, list, None)
    None


  plan (True, str, None)
    (Required for new resource) The plan type of the Database instance


  version (False, str, None)
    The database version to provision if specified


  remote_leader_id (False, str, None)
    The CRN of leader database


  point_in_time_recovery_time (False, str, None)
    The point in time recovery time stamp of the deployed instance


  point_in_time_recovery_deployment_id (False, str, None)
    The CRN of source instance


  offline_restore (False, bool, None)
    Set offline restore mode for MongoDB Enterprise Edition


  name (True, str, None)
    (Required for new resource) Resource instance name for example, my Database instance


  adminpassword (False, str, None)
    The admin user password for the instance


  configuration (False, str, None)
    The configuration in JSON format


  backup_id (False, str, None)
    The CRN of backup source database


  service_endpoints (True, str, None)
    (Required for new resource) Types of the service endpoints. Possible values are 'public', 'private', 'public-and-private'.


  key_protect_key (False, str, None)
    The CRN of Key protect key


  tags (False, list, None)
    None


  location (True, str, None)
    (Required for new resource) The location or the region in which Database instance exists


  backup_encryption_key_crn (False, str, None)
    The Backup Encryption Key CRN


  auto_scaling (False, list, None)
    ICD Auto Scaling


  key_protect_instance (False, str, None)
    The CRN of Key protect instance


  logical_replication_slot (False, list, None)
    None


  group (False, list, None)
    None


  users (False, list, None)
    None


  deletion_protection (False, bool, False)
    Whether Terraform will be prevented from destroying the instance


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

