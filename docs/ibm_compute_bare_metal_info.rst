
ibm_compute_bare_metal_info -- Retrieve IBM Cloud 'ibm_compute_bare_metal' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_compute_bare_metal' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.3
- Terraform v0.12.20



Parameters
----------

  global_identifier (False, str, None)
    The unique global identifier of the bare metal server


  domain (False, str, None)
    The domain of the bare metal server


  hourly_billing (False, bool, None)
    The billing type of the server.


  private_network_only (False, bool, None)
    Specifies whether the server only has access to the private network.


  datacenter (False, str, None)
    Datacenter in which the bare metal is deployed


  public_ipv4_address (False, str, None)
    The public IPv4 address of the bare metal server.


  public_subnet (False, int, None)
    The public subnet used for the public network interface of the server.


  notes (False, str, None)
    Notes associated with the server.


  public_bandwidth (False, int, None)
    The amount of public network traffic, allowed per month.


  os_reference_code (False, str, None)
    None


  file_storage_ids (False, list, None)
    File storage to which this computing server have access.


  ipv6_enabled (False, bool, None)
    Indicates whether the public IPv6 address enabled or not


  redundant_power_supply (False, bool, None)
    When the value is `true`, it indicates additional power supply is provided.


  redundant_network (False, bool, None)
    When the value is `true`, two physical network interfaces are provided with a bonding configuration.


  tags (False, list, None)
    Tags associated with this bare metal server.


  block_storage_ids (False, list, None)
    Block storage to which this computing server have access.


  ipv6_address_id (False, int, None)
    None


  secondary_ip_count (False, int, None)
    The number of secondary IPv4 addresses of the bare metal server.


  secondary_ip_addresses (False, list, None)
    The public secondary IPv4 addresses of the bare metal server.


  user_metadata (False, str, None)
    Arbitrary data available to the computing server.


  memory (False, int, None)
    The amount of memory in gigabytes, for the server.


  most_recent (False, bool, False)
    If true and multiple entries are found, the most recently created bare metal is used. If false, an error is returned


  hostname (False, str, None)
    The hostname of the bare metal server


  network_speed (False, int, None)
    The connection speed, expressed in Mbps,  for the server network components.


  private_ipv4_address_id (False, int, None)
    None


  public_vlan_id (False, int, None)
    The public VLAN used for the public network interface of the server.


  private_vlan_id (False, int, None)
    The private VLAN used for the private network interface of the server.


  private_subnet (False, int, None)
    The private subnet used for the private network interface of the server.


  unbonded_network (False, bool, None)
    When the value is `true`, two physical network interfaces are provided without a bonding configuration.


  ipv6_address (False, str, None)
    The public IPv6 address of the bare metal server


  public_ipv4_address_id (False, int, None)
    None


  private_ipv4_address (False, str, None)
    The private IPv4 address of the bare metal server.


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

