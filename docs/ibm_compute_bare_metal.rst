
ibm_compute_bare_metal -- Configure IBM Cloud 'ibm_compute_bare_metal' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_compute_bare_metal' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  user_metadata (False, str, None)
    None


  image_template_id (False, int, None)
    None


  network_speed (False, int, 100)
    None


  unbonded_network (False, bool, False)
    None


  restricted_network (False, bool, False)
    None


  fixed_config_preset (False, str, None)
    None


  private_ipv4_address (False, str, None)
    None


  public_subnet (False, str, None)
    None


  private_ipv4_address_id (False, int, None)
    None


  secondary_ip_count (False, int, None)
    None


  file_storage_ids (False, list, None)
    None


  post_install_script_uri (False, str, None)
    None


  software_guard_extensions (False, bool, False)
    None


  disk_key_names (False, list, None)
    None


  redundant_network (False, bool, False)
    None


  global_identifier (False, str, None)
    The unique global identifier of the bare metal server


  public_bandwidth (False, int, None)
    None


  public_ipv4_address_id (False, int, None)
    None


  ipv6_address (False, str, None)
    None


  domain (False, str, None)
    (Required for new resource)


  block_storage_ids (False, list, None)
    None


  datacenter (False, str, None)
    None


  hourly_billing (False, bool, True)
    None


  package_key_name (False, str, None)
    None


  storage_groups (False, list, None)
    None


  private_subnet (False, str, None)
    None


  secondary_ip_addresses (False, list, None)
    None


  notes (False, str, None)
    None


  os_reference_code (False, str, None)
    None


  private_network_only (False, bool, False)
    None


  tcp_monitoring (False, bool, False)
    None


  extended_hardware_testing (False, bool, False)
    None


  ipv6_static_enabled (False, bool, False)
    None


  ipv6_enabled (False, bool, False)
    None


  ipv6_address_id (False, int, None)
    None


  tags (False, list, None)
    None


  process_key_name (False, str, None)
    None


  gpu_key_name (False, str, None)
    None


  memory (False, int, None)
    None


  public_ipv4_address (False, str, None)
    None


  ssh_key_ids (False, list, None)
    None


  gpu_secondary_key_name (False, str, None)
    None


  public_vlan_id (False, int, None)
    None


  private_vlan_id (False, int, None)
    None


  hostname (False, str, None)
    None


  redundant_power_supply (False, bool, None)
    None


  os_key_name (False, str, None)
    None


  quote_id (False, int, None)
    None


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

