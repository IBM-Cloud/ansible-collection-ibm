
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

- IBM-Cloud terraform-provider-ibm v1.2.3
- Terraform v0.12.20



Parameters
----------

  resource_crn (False, str, None)
    The crn of the resource


  plan (False, str, None)
    (Required for new resource) The plan type of the Database instance


  adminpassword (False, str, None)
    The admin user password for the instance


  remote_leader_id (False, str, None)
    The CRN of leader database


  status (False, str, None)
    The resource instance status


  users (False, list, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about the resource


  resource_status (False, str, None)
    The status of the resource


  tags (False, list, None)
    None


  members_memory_allocation_mb (False, int, None)
    Memory allocation required for cluster


  members_cpu_allocation_count (False, int, None)
    CPU allocation required for cluster


  backup_id (False, str, None)
    The CRN of backup source database


  name (False, str, None)
    (Required for new resource) Resource instance name for example, my Database instance


  members_disk_allocation_mb (False, int, None)
    Disk allocation required for cluster


  key_protect_instance (False, str, None)
    The CRN of Key protect instance


  resource_name (False, str, None)
    The name of the resource


  connectionstrings (False, list, None)
    None


  whitelist (False, list, None)
    None


  groups (False, list, None)
    None


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  resource_group_id (False, str, None)
    The id of the resource group in which the Database instance is present


  location (False, str, None)
    (Required for new resource) The location or the region in which Database instance exists


  service (False, str, None)
    (Required for new resource) The name of the Cloud Internet database service


  service_endpoints (False, str, public)
    Types of the service endpoints. Possible values are 'public', 'private', 'public-and-private'.


  adminuser (False, str, None)
    The admin user id for the instance


  version (False, str, None)
    The database version to provision if specified


  key_protect_key (False, str, None)
    The CRN of Key protect key


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

