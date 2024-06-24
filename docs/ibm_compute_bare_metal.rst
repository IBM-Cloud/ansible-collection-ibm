
ibm_compute_bare_metal -- Configure IBM Cloud 'ibm_compute_bare_metal' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_compute_bare_metal' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/compute_bare_metal

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  image_template_id (False, int, None)
    OS image template ID


  software_guard_extensions (False, bool, False)
    None


  package_key_name (False, str, None)
    None


  ssh_key_ids (False, list, None)
    SSH KEY IDS list


  user_metadata (False, str, None)
    User metadata info


  storage_groups (False, list, None)
    None


  private_subnet (False, str, None)
    None


  private_network_only (False, bool, False)
    only private network configured if is true


  gpu_secondary_key_name (False, str, None)
    None


  redundant_network (False, bool, False)
    None


  unbonded_network (False, bool, False)
    None


  quote_id (False, int, None)
    Quote ID for Quote based provisioning


  domain (True, str, None)
    (Required for new resource) Domain name


  os_reference_code (False, str, None)
    OS refernece code value


  hourly_billing (False, bool, True)
    Enables hourly billing


  tcp_monitoring (False, bool, False)
    TCP monitoring enabled if set as true


  gpu_key_name (False, str, None)
    None


  extended_hardware_testing (False, bool, False)
    None


  secondary_ip_count (False, int, None)
    Secondary IP addresses count


  hostname (False, str, None)
    Host name


  notes (False, str, None)
    Optional notes info


  file_storage_ids (False, list, None)
    None


  block_storage_ids (False, list, None)
    None


  post_install_script_uri (False, str, None)
    None


  datacenter (False, str, None)
    None


  disk_key_names (False, list, None)
    None


  ipv6_enabled (False, bool, False)
    Boolean value true if IPV6 ia enabled or false


  tags (False, list, None)
    None


  fixed_config_preset (False, str, None)
    Fixed config preset value


  public_bandwidth (False, int, None)
    None


  private_vlan_id (False, int, None)
    None


  redundant_power_supply (False, bool, None)
    None


  process_key_name (False, str, None)
    None


  os_key_name (False, str, None)
    None


  public_vlan_id (False, int, None)
    None


  public_subnet (False, str, None)
    None


  ipv6_static_enabled (False, bool, False)
    boolean value true if ipv6 static is enabled else false


  network_speed (False, int, 100)
    Network speed in MBPS


  restricted_network (False, bool, False)
    None


  memory (False, int, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

