
ibm_org_quota_info -- Retrieve IBM Cloud 'ibm_org_quota' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_org_quota' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  app_tasks_limit (False, int, None)
    Defines the total app task limit for organization.


  total_reserved_route_ports (False, int, None)
    Defines the number of reserved route ports for organization.


  name (True, str, None)
    Org quota name, for example qIBM


  total_services (False, int, None)
    Defines the total services for organization.


  memory_limit (False, int, None)
    Defines the total memory limit for organization.


  instance_memory_limit (False, int, None)
    Defines the  total instance memory limit for organization.


  app_instance_limit (False, int, None)
    Defines the total app instance limit for organization.


  non_basic_services_allowed (False, bool, None)
    Define non basic services are allowed for organization.


  total_routes (False, int, None)
    Defines the total route for organization.


  trial_db_allowed (False, bool, None)
    Defines trial db are allowed for organization.


  total_private_domains (False, int, None)
    Defines the total private domain limit for organization.v


  total_service_keys (False, int, None)
    Defines the total service keys for organization.


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

