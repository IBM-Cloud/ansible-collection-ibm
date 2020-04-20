
ibm_compute_vm_instance -- Configure IBM Cloud 'ibm_compute_vm_instance' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_compute_vm_instance' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  public_ipv6_subnet_id (False, str, None)
    NA


  secondary_ip_addresses (False, list, None)
    NA


  notes (False, str, None)
    NA


  image_id (False, int, None)
    NA


  os_reference_code (False, str, None)
    NA


  flavor_key_name (False, str, None)
    Flavor key name used to provision vm.


  transient (False, bool, None)
    NA


  ipv4_address_private (False, str, None)
    NA


  public_bandwidth_limited (False, int, None)
    NA


  dedicated_acct_host_only (False, bool, None)
    NA


  public_security_group_ids (False, list, None)
    NA


  ipv6_address (False, str, None)
    NA


  resource_status (False, str, None)
    The status of the resource


  private_network_only (False, bool, False)
    NA


  secondary_ip_count (False, int, None)
    NA


  public_bandwidth_unlimited (False, bool, False)
    NA


  evault (False, int, None)
    NA


  domain (False, str, None)
    NA


  memory (False, int, None)
    NA


  public_interface_id (False, int, None)
    NA


  ssh_key_ids (False, list, None)
    NA


  private_subnet (False, str, None)
    NA


  private_security_group_ids (False, list, None)
    NA


  local_disk (False, bool, True)
    NA


  ipv6_static_enabled (False, bool, False)
    NA


  block_storage_ids (False, list, None)
    NA


  cores (False, int, None)
    NA


  dedicated_host_name (False, str, None)
    NA


  public_vlan_id (False, int, None)
    NA


  public_subnet (False, str, None)
    NA


  private_interface_id (False, int, None)
    NA


  network_speed (False, int, 100)
    NA


  user_metadata (False, str, None)
    NA


  hostname (False, str, None)
    NA


  private_vlan_id (False, int, None)
    NA


  public_ipv6_subnet (False, str, None)
    NA


  private_subnet_id (False, int, None)
    NA


  ip_address_id (False, int, None)
    NA


  placement_group_id (False, int, None)
    The placement group id


  ipv6_address_id (False, int, None)
    NA


  post_install_script_uri (False, str, None)
    NA


  disks (False, list, None)
    NA


  tags (False, list, None)
    NA


  bulk_vms (False, list, None)
    NA


  datacenter (False, str, None)
    NA


  placement_group_name (False, str, None)
    The placement group name


  dedicated_host_id (False, int, None)
    NA


  hourly_billing (False, bool, True)
    NA


  ip_address_id_private (False, int, None)
    NA


  wait_time_minutes (False, int, 90)
    NA


  resource_name (False, str, None)
    The name of the resource


  datacenter_choice (False, list, None)
    The user provided datacenter options


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  public_subnet_id (False, int, None)
    NA


  ipv4_address (False, str, None)
    NA


  ipv6_enabled (False, bool, False)
    NA


  file_storage_ids (False, list, None)
    NA


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

