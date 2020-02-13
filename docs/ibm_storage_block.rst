
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

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  os_format_type (False, str, None)
    (Required for new resource)


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  capacity (False, int, None)
    (Required for new resource)


  volumename (False, str, None)
    None


  allowed_hardware_ids (False, list, None)
    None


  allowed_host_info (False, list, None)
    None


  resource_name (False, str, None)
    The name of the resource


  type (False, str, None)
    (Required for new resource)


  allowed_virtual_guest_ids (False, list, None)
    None


  notes (False, str, None)
    None


  allowed_hardware_info (False, list, None)
    None


  tags (False, list, None)
    None


  hourly_billing (False, bool, False)
    None


  target_address (False, list, None)
    None


  iops (False, float, None)
    (Required for new resource)


  hostname (False, str, None)
    None


  snapshot_capacity (False, int, None)
    None


  allowed_virtual_guest_info (False, list, None)
    None


  allowed_ip_addresses (False, list, None)
    None


  datacenter (False, str, None)
    (Required for new resource)


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

