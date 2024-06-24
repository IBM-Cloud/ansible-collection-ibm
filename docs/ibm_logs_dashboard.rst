
ibm_logs_dashboard -- Configure IBM Cloud 'ibm_logs_dashboard' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_logs_dashboard' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/logs_dashboard

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  two_minutes (False, bool, None)
    None


  five_minutes (False, bool, None)
    None


  endpoint_type (False, str, None)
    public or private.


  layout (True, list, None)
    (Required for new resource) Layout configuration for the dashboard's visual elements.


  variables (False, list, None)
    List of variables that can be used within the dashboard for dynamic content.


  filters (False, list, None)
    List of filters that can be applied to the dashboard's data.


  folder_path (False, list, None)
    Path of the folder containing the dashboard.


  False (False, bool, None)
    None


  absolute_time_frame (False, list, None)
    Absolute time frame specifying a fixed start and end time.


  relative_time_frame (False, str, None)
    Relative time frame specifying a duration from the current time.


  folder_id (False, list, None)
    Unique identifier of the folder containing the dashboard.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  href (False, str, None)
    Unique identifier for the dashboard.


  annotations (False, list, None)
    List of annotations that can be applied to the dashboard's visual elements.


  name (True, str, None)
    (Required for new resource) Display name of the dashboard.


  description (False, str, None)
    Brief description or summary of the dashboard's purpose or content.


  instance_id (True, str, None)
    (Required for new resource) The ID of the logs instance.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

