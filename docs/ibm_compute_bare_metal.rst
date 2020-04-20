
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

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  storage_groups (False, list, None)
    NA


  public_vlan_id (False, int, None)
    NA


  block_storage_ids (False, list, None)
    NA


  image_template_id (False, int, None)
    NA


  hourly_billing (False, bool, True)
    NA


  public_bandwidth (False, int, None)
    NA


  datacenter (False, str, None)
    NA


  gpu_key_name (False, str, None)
    NA


  disk_key_names (False, list, None)
    NA


  redundant_power_supply (False, bool, None)
    NA


  private_vlan_id (False, int, None)
    NA


  secondary_ip_addresses (False, list, None)
    NA


  domain (False, str, None)
    (Required for new resource) NA


  ssh_key_ids (False, list, None)
    NA


  network_speed (False, int, 100)
    NA


  public_subnet (False, str, None)
    NA


  private_subnet (False, str, None)
    NA


  global_identifier (False, str, None)
    The unique global identifier of the bare metal server


  tcp_monitoring (False, bool, False)
    NA


  software_guard_extensions (False, bool, False)
    NA


  extended_hardware_testing (False, bool, False)
    NA


  redundant_network (False, bool, False)
    NA


  restricted_network (False, bool, False)
    NA


  memory (False, int, None)
    NA


  quote_id (False, int, None)
    NA


  private_ipv4_address_id (False, int, None)
    NA


  file_storage_ids (False, list, None)
    NA


  tags (False, list, None)
    NA


  gpu_secondary_key_name (False, str, None)
    NA


  ipv6_enabled (False, bool, False)
    NA


  ipv6_address (False, str, None)
    NA


  ipv6_static_enabled (False, bool, False)
    NA


  os_key_name (False, str, None)
    NA


  private_ipv4_address (False, str, None)
    NA


  user_metadata (False, str, None)
    NA


  private_network_only (False, bool, False)
    NA


  package_key_name (False, str, None)
    NA


  fixed_config_preset (False, str, None)
    NA


  os_reference_code (False, str, None)
    NA


  process_key_name (False, str, None)
    NA


  secondary_ip_count (False, int, None)
    NA


  hostname (False, str, None)
    NA


  notes (False, str, None)
    NA


  post_install_script_uri (False, str, None)
    NA


  ipv6_address_id (False, int, None)
    NA


  unbonded_network (False, bool, False)
    NA


  public_ipv4_address (False, str, None)
    NA


  public_ipv4_address_id (False, int, None)
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

