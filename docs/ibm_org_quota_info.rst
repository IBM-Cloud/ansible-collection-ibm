
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

- IBM-Cloud terraform-provider-ibm v1.5.3
- Terraform v0.12.20



Parameters
----------

  total_routes (False, int, None)
    Defines the total route for organization.


  instance_memory_limit (False, int, None)
    Defines the  total instance memory limit for organization.


  trial_db_allowed (False, bool, None)
    Defines trial db are allowed for organization.


  app_tasks_limit (False, int, None)
    Defines the total app task limit for organization.


  total_service_keys (False, int, None)
    Defines the total service keys for organization.


  total_reserved_route_ports (False, int, None)
    Defines the number of reserved route ports for organization.


  name (True, str, None)
    Org quota name, for example qIBM


  non_basic_services_allowed (False, bool, None)
    Define non basic services are allowed for organization.


  total_services (False, int, None)
    Defines the total services for organization.


  memory_limit (False, int, None)
    Defines the total memory limit for organization.


  app_instance_limit (False, int, None)
    Defines the total app instance limit for organization.


  total_private_domains (False, int, None)
    Defines the total private domain limit for organization.v


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

