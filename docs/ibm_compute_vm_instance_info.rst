
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

- IBM-Cloud terraform-provider-ibm v1.2.5
- Terraform v0.12.20



Parameters
----------

  public_interface_id (False, int, None)
    None


  private_interface_id (False, int, None)
    None


  public_subnet_id (False, int, None)
    None


  ipv4_address (False, str, None)
    None


  ipv4_address_private (False, str, None)
    None


  ipv6_address_id (False, int, None)
    None


  public_ipv6_subnet (False, str, None)
    None


  hostname (True, str, None)
    The hostname of the virtual guest


  datacenter (False, str, None)
    Datacenter in which the virtual guest is deployed


  private_subnet_id (False, int, None)
    None


  ip_address_id (False, int, None)
    None


  secondary_ip_addresses (False, list, None)
    None


  secondary_ip_count (False, int, None)
    None


  domain (True, str, None)
    The domain of the virtual guest


  last_known_power_state (False, str, None)
    The last known power state of a virtual guest in the event the guest is turned off outside of IMS or has gone offline.


  most_recent (False, bool, False)
    If true and multiple entries are found, the most recently created virtual guest is used. If false, an error is returned


  ip_address_id_private (False, int, None)
    None


  status (False, str, None)
    The VSI status


  power_state (False, str, None)
    The current power state of a virtual guest.


  ipv6_address (False, str, None)
    None


  public_ipv6_subnet_id (False, str, None)
    None


  cores (False, int, None)
    Number of cpu cores


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

