
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

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  public_subnet_id (False, int, None)
    NA


  ipv4_address (False, str, None)
    NA


  ipv4_address_private (False, str, None)
    NA


  ip_address_id (False, int, None)
    NA


  ipv6_address (False, str, None)
    NA


  secondary_ip_count (False, int, None)
    NA


  cores (False, int, None)
    Number of cpu cores


  public_interface_id (False, int, None)
    NA


  datacenter (False, str, None)
    Datacenter in which the virtual guest is deployed


  last_known_power_state (False, str, None)
    The last known power state of a virtual guest in the event the guest is turned off outside of IMS or has gone offline.


  private_interface_id (False, int, None)
    NA


  ipv6_address_id (False, int, None)
    NA


  secondary_ip_addresses (False, list, None)
    NA


  hostname (True, str, None)
    The hostname of the virtual guest


  domain (True, str, None)
    The domain of the virtual guest


  ip_address_id_private (False, int, None)
    NA


  public_ipv6_subnet (False, str, None)
    NA


  status (False, str, None)
    The VSI status


  most_recent (False, bool, False)
    If true and multiple entries are found, the most recently created virtual guest is used. If false, an error is returned


  public_ipv6_subnet_id (False, str, None)
    NA


  power_state (False, str, None)
    The current power state of a virtual guest.


  private_subnet_id (False, int, None)
    NA


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

