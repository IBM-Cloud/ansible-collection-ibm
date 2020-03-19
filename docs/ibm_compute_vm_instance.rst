
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

- IBM-Cloud terraform-provider-ibm v1.2.5
- Terraform v0.12.20



Parameters
----------

  post_install_script_uri (False, str, None)
    None


  datacenter (False, str, None)
    None


  flavor_key_name (False, str, None)
    Flavor key name used to provision vm.


  public_bandwidth_unlimited (False, bool, False)
    None


  file_storage_ids (False, list, None)
    None


  image_id (False, int, None)
    None


  transient (False, bool, None)
    None


  public_security_group_ids (False, list, None)
    None


  private_subnet_id (False, int, None)
    None


  ipv6_static_enabled (False, bool, False)
    None


  block_storage_ids (False, list, None)
    None


  dedicated_acct_host_only (False, bool, None)
    None


  public_vlan_id (False, int, None)
    None


  disks (False, list, None)
    None


  ipv6_address (False, str, None)
    None


  ssh_key_ids (False, list, None)
    None


  wait_time_minutes (False, int, 90)
    None


  datacenter_choice (False, list, None)
    The user provided datacenter options


  private_vlan_id (False, int, None)
    None


  cores (False, int, None)
    None


  dedicated_host_id (False, int, None)
    None


  private_security_group_ids (False, list, None)
    None


  public_ipv6_subnet (False, str, None)
    None


  tags (False, list, None)
    None


  resource_status (False, str, None)
    The status of the resource


  bulk_vms (False, list, None)
    None


  os_reference_code (False, str, None)
    None


  private_interface_id (False, int, None)
    None


  ipv6_address_id (False, int, None)
    None


  notes (False, str, None)
    None


  public_interface_id (False, int, None)
    None


  ipv4_address_private (False, str, None)
    None


  network_speed (False, int, 100)
    None


  ip_address_id_private (False, int, None)
    None


  user_metadata (False, str, None)
    None


  private_network_only (False, bool, False)
    None


  public_subnet_id (False, int, None)
    None


  resource_name (False, str, None)
    The name of the resource


  dedicated_host_name (False, str, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  hourly_billing (False, bool, True)
    None


  ipv6_enabled (False, bool, False)
    None


  public_ipv6_subnet_id (False, str, None)
    None


  secondary_ip_count (False, int, None)
    None


  public_bandwidth_limited (False, int, None)
    None


  hostname (False, str, None)
    None


  domain (False, str, None)
    None


  local_disk (False, bool, True)
    None


  evault (False, int, None)
    None


  public_subnet (False, str, None)
    None


  ipv4_address (False, str, None)
    None


  placement_group_name (False, str, None)
    The placement group name


  placement_group_id (False, int, None)
    The placement group id


  ip_address_id (False, int, None)
    None


  secondary_ip_addresses (False, list, None)
    None


  memory (False, int, None)
    None


  private_subnet (False, str, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

