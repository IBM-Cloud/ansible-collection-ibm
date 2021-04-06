
ibm_storage_file -- Configure IBM Cloud 'ibm_storage_file' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_storage_file' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.23.0
- Terraform v0.12.20



Parameters
----------

  allowed_ip_addresses (False, list, None)
    Allowed range of IP addresses


  tags (False, list, None)
    Tags set for the storage volume


  iops (True, float, None)
    (Required for new resource) iops rate


  allowed_hardware_ids (False, list, None)
    Hardaware ID


  snapshot_schedule (False, list, None)
    None


  hourly_billing (False, bool, False)
    Hourly based billing type


  allowed_virtual_guest_ids (False, list, None)
    Virtual guest ID


  allowed_subnets (False, list, None)
    Allowed network subnets


  snapshot_capacity (False, int, None)
    Snapshot capacity


  datacenter (True, str, None)
    (Required for new resource) Datacenter name


  capacity (True, int, None)
    (Required for new resource) Storage capacity


  notes (False, str, None)
    Notes


  type (True, str, None)
    (Required for new resource) Storage type


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

