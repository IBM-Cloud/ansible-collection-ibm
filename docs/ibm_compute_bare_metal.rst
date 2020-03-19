
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

- IBM-Cloud terraform-provider-ibm v1.2.5
- Terraform v0.12.20



Parameters
----------

  domain (False, str, None)
    (Required for new resource)


  block_storage_ids (False, list, None)
    None


  tags (False, list, None)
    None


  image_template_id (False, int, None)
    None


  software_guard_extensions (False, bool, False)
    None


  ipv6_address (False, str, None)
    None


  os_reference_code (False, str, None)
    None


  hourly_billing (False, bool, True)
    None


  process_key_name (False, str, None)
    None


  disk_key_names (False, list, None)
    None


  quote_id (False, int, None)
    None


  ipv6_address_id (False, int, None)
    None


  package_key_name (False, str, None)
    None


  public_vlan_id (False, int, None)
    None


  private_subnet (False, str, None)
    None


  private_ipv4_address (False, str, None)
    None


  datacenter (False, str, None)
    None


  os_key_name (False, str, None)
    None


  public_bandwidth (False, int, None)
    None


  storage_groups (False, list, None)
    None


  public_subnet (False, str, None)
    None


  private_vlan_id (False, int, None)
    None


  ipv6_static_enabled (False, bool, False)
    None


  hostname (False, str, None)
    None


  fixed_config_preset (False, str, None)
    None


  redundant_network (False, bool, False)
    None


  extended_hardware_testing (False, bool, False)
    None


  ipv6_enabled (False, bool, False)
    None


  global_identifier (False, str, None)
    The unique global identifier of the bare metal server


  private_network_only (False, bool, False)
    None


  gpu_secondary_key_name (False, str, None)
    None


  memory (False, int, None)
    None


  secondary_ip_addresses (False, list, None)
    None


  user_metadata (False, str, None)
    None


  notes (False, str, None)
    None


  file_storage_ids (False, list, None)
    None


  network_speed (False, int, 100)
    None


  tcp_monitoring (False, bool, False)
    None


  gpu_key_name (False, str, None)
    None


  unbonded_network (False, bool, False)
    None


  secondary_ip_count (False, int, None)
    None


  ssh_key_ids (False, list, None)
    None


  post_install_script_uri (False, str, None)
    None


  redundant_power_supply (False, bool, None)
    None


  restricted_network (False, bool, False)
    None


  public_ipv4_address (False, str, None)
    None


  public_ipv4_address_id (False, int, None)
    None


  private_ipv4_address_id (False, int, None)
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

