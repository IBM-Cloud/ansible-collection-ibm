
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

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  most_recent (False, bool, False)
    If true and multiple entries are found, the most recently created bare metal is used. If false, an error is returned


  datacenter (False, str, None)
    Datacenter in which the bare metal is deployed


  public_bandwidth (False, int, None)
    The amount of public network traffic, allowed per month.


  public_subnet (False, int, None)
    The public subnet used for the public network interface of the server.


  private_vlan_id (False, int, None)
    The private VLAN used for the private network interface of the server.


  hourly_billing (False, bool, None)
    The billing type of the server.


  user_metadata (False, str, None)
    Arbitrary data available to the computing server.


  secondary_ip_count (False, int, None)
    The number of secondary IPv4 addresses of the bare metal server.


  private_ipv4_address_id (False, int, None)
    None


  notes (False, str, None)
    Notes associated with the server.


  redundant_network (False, bool, None)
    When the value is `true`, two physical network interfaces are provided with a bonding configuration.


  file_storage_ids (False, list, None)
    File storage to which this computing server have access.


  ipv6_enabled (False, bool, None)
    Indicates whether the public IPv6 address enabled or not


  ipv6_address (False, str, None)
    The public IPv6 address of the bare metal server


  public_ipv4_address_id (False, int, None)
    None


  global_identifier (False, str, None)
    The unique global identifier of the bare metal server


  private_network_only (False, bool, None)
    Specifies whether the server only has access to the private network.


  secondary_ip_addresses (False, list, None)
    The public secondary IPv4 addresses of the bare metal server.


  public_ipv4_address (False, str, None)
    The public IPv4 address of the bare metal server.


  private_ipv4_address (False, str, None)
    The private IPv4 address of the bare metal server.


  memory (False, int, None)
    The amount of memory in gigabytes, for the server.


  unbonded_network (False, bool, None)
    When the value is `true`, two physical network interfaces are provided without a bonding configuration.


  ipv6_address_id (False, int, None)
    None


  public_vlan_id (False, int, None)
    The public VLAN used for the public network interface of the server.


  redundant_power_supply (False, bool, None)
    When the value is `true`, it indicates additional power supply is provided.


  tags (False, list, None)
    Tags associated with this bare metal server.


  hostname (False, str, None)
    The hostname of the bare metal server


  os_reference_code (False, str, None)
    None


  block_storage_ids (False, list, None)
    Block storage to which this computing server have access.


  domain (False, str, None)
    The domain of the bare metal server


  network_speed (False, int, None)
    The connection speed, expressed in Mbps,  for the server network components.


  private_subnet (False, int, None)
    The private subnet used for the private network interface of the server.


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

