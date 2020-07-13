
ibm_storage_file -- Configure IBM Cloud 'ibm_storage_file' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_storage_file' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  volumename (False, str, None)
    Storage volume name


  allowed_hardware_ids (False, list, None)
    Hardaware ID


  allowed_ip_addresses (False, list, None)
    Allowed range of IP addresses


  notes (False, str, None)
    Notes


  resource_name (False, str, None)
    The name of the resource


  resource_status (False, str, None)
    The status of the resource


  type (True, str, None)
    (Required for new resource) Storage type


  iops (True, float, None)
    (Required for new resource) iops rate


  snapshot_schedule (False, list, None)
    None


  mountpoint (False, str, None)
    Storage mount point


  hourly_billing (False, bool, False)
    Hourly based billing type


  tags (False, list, None)
    Tags set for the storage volume


  datacenter (True, str, None)
    (Required for new resource) Datacenter name


  capacity (True, int, None)
    (Required for new resource) Storage capacity


  hostname (False, str, None)
    Hostname


  snapshot_capacity (False, int, None)
    Snapshot capacity


  allowed_virtual_guest_ids (False, list, None)
    Virtual guest ID


  allowed_subnets (False, list, None)
    Allowed network subnets


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


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

