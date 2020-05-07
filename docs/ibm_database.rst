
ibm_database -- Configure IBM Cloud 'ibm_database' resource
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_database' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.2
- Terraform v0.12.20



Parameters
----------

  plan (False, str, None)
    (Required for new resource) The plan type of the Database instance


  adminuser (False, str, None)
    The admin user id for the instance


  version (False, str, None)
    The database version to provision if specified


  members_memory_allocation_mb (False, int, None)
    Memory allocation required for cluster


  remote_leader_id (False, str, None)
    The CRN of leader database


  resource_name (False, str, None)
    The name of the resource


  resource_crn (False, str, None)
    The crn of the resource


  location (False, str, None)
    (Required for new resource) The location or the region in which Database instance exists


  point_in_time_recovery_time (False, str, None)
    The point in time recovery time stamp of the deployed instance


  connectionstrings (False, list, None)
    None


  whitelist (False, list, None)
    None


  service (False, str, None)
    (Required for new resource) The name of the Cloud Internet database service


  users (False, list, None)
    None


  key_protect_key (False, str, None)
    The CRN of Key protect key


  members_cpu_allocation_count (False, int, None)
    CPU allocation required for cluster


  resource_group_id (False, str, None)
    The id of the resource group in which the Database instance is present


  members_disk_allocation_mb (False, int, None)
    Disk allocation required for cluster


  point_in_time_recovery_deployment_id (False, str, None)
    The CRN of source instance


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about the resource


  name (False, str, None)
    (Required for new resource) Resource instance name for example, my Database instance


  guid (False, str, None)
    Unique identifier of resource instance


  service_endpoints (False, str, public)
    Types of the service endpoints. Possible values are 'public', 'private', 'public-and-private'.


  backup_id (False, str, None)
    The CRN of backup source database


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  status (False, str, None)
    The resource instance status


  key_protect_instance (False, str, None)
    The CRN of Key protect instance


  tags (False, list, None)
    None


  groups (False, list, None)
    None


  resource_status (False, str, None)
    The status of the resource


  adminpassword (False, str, None)
    The admin user password for the instance


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

