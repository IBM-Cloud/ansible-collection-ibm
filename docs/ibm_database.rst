
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

- IBM-Cloud terraform-provider-ibm v1.39.1
- Terraform v0.12.20



Parameters
----------

  service_endpoints (False, str, public)
    Types of the service endpoints. Possible values are 'public', 'private', 'public-and-private'.


  whitelist (False, list, None)
    None


  key_protect_instance (False, str, None)
    The CRN of Key protect instance


  users (False, list, None)
    None


  resource_group_id (False, str, None)
    The id of the resource group in which the Database instance is present


  service (True, str, None)
    (Required for new resource) The name of the Cloud Internet database service


  plan (True, str, None)
    (Required for new resource) The plan type of the Database instance


  members_disk_allocation_mb (False, int, None)
    Disk allocation required for cluster


  node_count (False, int, None)
    Total number of nodes in the cluster


  remote_leader_id (False, str, None)
    The CRN of leader database


  tags (False, list, None)
    None


  adminpassword (False, str, None)
    The admin user password for the instance


  configuration (False, str, None)
    The configuration in JSON format


  backup_encryption_key_crn (False, str, None)
    The Backup Encryption Key CRN


  auto_scaling (False, list, None)
    ICD Auto Scaling


  name (True, str, None)
    (Required for new resource) Resource instance name for example, my Database instance


  key_protect_key (False, str, None)
    The CRN of Key protect key


  version (False, str, None)
    The database version to provision if specified


  members_cpu_allocation_count (False, int, None)
    CPU allocation required for cluster


  node_memory_allocation_mb (False, int, None)
    Memory allocation per node


  node_cpu_allocation_count (False, int, None)
    CPU allocation per node


  backup_id (False, str, None)
    The CRN of backup source database


  members_memory_allocation_mb (False, int, None)
    Memory allocation required for cluster


  plan_validation (False, bool, True)
    For elasticsearch and postgres perform database parameter validation during the plan phase. Otherwise, database parameter validation happens in apply phase.


  point_in_time_recovery_deployment_id (False, str, None)
    The CRN of source instance


  location (True, str, None)
    (Required for new resource) The location or the region in which Database instance exists


  node_disk_allocation_mb (False, int, None)
    Disk allocation per node


  point_in_time_recovery_time (False, str, None)
    The point in time recovery time stamp of the deployed instance


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

