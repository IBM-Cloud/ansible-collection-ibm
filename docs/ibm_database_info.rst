
ibm_database_info -- Retrieve IBM Cloud 'ibm_database' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_database' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.3.0
- Terraform v0.12.20



Parameters
----------

  service (False, str, None)
    The name of the Cloud Internet database service


  version (False, str, None)
    The database version to provision if specified


  groups (False, list, None)
    None


  resource_group_id (False, str, None)
    The id of the resource group in which the Database instance is present


  guid (False, str, None)
    Unique identifier of resource instance


  whitelist (False, list, None)
    None


  resource_name (False, str, None)
    The name of the resource


  resource_status (False, str, None)
    The status of the resource


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  adminuser (False, str, None)
    The admin user id for the instance


  members_disk_allocation_mb (False, int, None)
    Disk allocation required for cluster


  status (False, str, None)
    The resource instance status


  users (False, list, None)
    None


  connectionstrings (False, list, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about the resource


  name (True, str, None)
    Resource instance name for example, my Database instance


  plan (False, str, None)
    The plan type of the Database instance


  members_memory_allocation_mb (False, int, None)
    Memory allocation required for cluster


  tags (False, list, None)
    None


  resource_crn (False, str, None)
    The crn of the resource


  location (False, str, None)
    The location or the region in which the Database instance exists


  adminpassword (False, str, None)
    The admin user id for the instance


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

