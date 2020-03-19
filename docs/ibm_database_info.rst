
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

- IBM-Cloud terraform-provider-ibm v1.2.5
- Terraform v0.12.20



Parameters
----------

  location (False, str, None)
    The location or the region in which the Database instance exists


  whitelist (False, list, None)
    None


  name (True, str, None)
    Resource instance name for example, my Database instance


  adminpassword (False, str, None)
    The admin user id for the instance


  members_memory_allocation_mb (False, int, None)
    Memory allocation required for cluster


  resource_name (False, str, None)
    The name of the resource


  resource_status (False, str, None)
    The status of the resource


  resource_group_id (False, str, None)
    The id of the resource group in which the Database instance is present


  service (False, str, None)
    The name of the Cloud Internet database service


  status (False, str, None)
    The resource instance status


  version (False, str, None)
    The database version to provision if specified


  members_disk_allocation_mb (False, int, None)
    Disk allocation required for cluster


  tags (False, list, None)
    None


  connectionstrings (False, list, None)
    None


  groups (False, list, None)
    None


  guid (False, str, None)
    Unique identifier of resource instance


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  resource_crn (False, str, None)
    The crn of the resource


  adminuser (False, str, None)
    The admin user id for the instance


  users (False, list, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about the resource


  plan (False, str, None)
    The plan type of the Database instance


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

