
ibm_storage_block -- Configure IBM Cloud 'ibm_storage_block' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_storage_block' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  os_format_type (False, str, None)
    (Required for new resource) NA


  notes (False, str, None)
    NA


  allowed_hardware_info (False, list, None)
    NA


  tags (False, list, None)
    NA


  target_address (False, list, None)
    NA


  resource_name (False, str, None)
    The name of the resource


  hostname (False, str, None)
    NA


  volumename (False, str, None)
    NA


  allowed_ip_addresses (False, list, None)
    NA


  iops (False, float, None)
    (Required for new resource) NA


  allowed_virtual_guest_ids (False, list, None)
    NA


  allowed_virtual_guest_info (False, list, None)
    NA


  allowed_host_info (False, list, None)
    NA


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  capacity (False, int, None)
    (Required for new resource) NA


  datacenter (False, str, None)
    (Required for new resource) NA


  snapshot_capacity (False, int, None)
    NA


  allowed_hardware_ids (False, list, None)
    NA


  hourly_billing (False, bool, False)
    NA


  type (False, str, None)
    (Required for new resource) NA


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

