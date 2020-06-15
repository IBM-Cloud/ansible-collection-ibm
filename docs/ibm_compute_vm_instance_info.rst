
ibm_compute_vm_instance_info -- Retrieve IBM Cloud 'ibm_compute_vm_instance' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_compute_vm_instance' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.7.1
- Terraform v0.12.20



Parameters
----------

  ipv6_address_id (False, int, None)
    None


  secondary_ip_addresses (False, list, None)
    None


  secondary_ip_count (False, int, None)
    None


  domain (True, str, None)
    The domain of the virtual guest


  cores (False, int, None)
    Number of cpu cores


  last_known_power_state (False, str, None)
    The last known power state of a virtual guest in the event the guest is turned off outside of IMS or has gone offline.


  public_subnet_id (False, int, None)
    None


  private_subnet_id (False, int, None)
    None


  ipv4_address_private (False, str, None)
    None


  ip_address_id_private (False, int, None)
    None


  public_ipv6_subnet (False, str, None)
    None


  hostname (True, str, None)
    The hostname of the virtual guest


  datacenter (False, str, None)
    Datacenter in which the virtual guest is deployed


  private_interface_id (False, int, None)
    None


  most_recent (False, bool, False)
    If true and multiple entries are found, the most recently created virtual guest is used. If false, an error is returned


  public_interface_id (False, int, None)
    None


  power_state (False, str, None)
    The current power state of a virtual guest.


  public_ipv6_subnet_id (False, str, None)
    None


  status (False, str, None)
    The VSI status


  ipv4_address (False, str, None)
    None


  ip_address_id (False, int, None)
    None


  ipv6_address (False, str, None)
    None


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

