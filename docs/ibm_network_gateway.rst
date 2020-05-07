
ibm_network_gateway -- Configure IBM Cloud 'ibm_network_gateway' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_network_gateway' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.2
- Terraform v0.12.20



Parameters
----------

  private_vlan_id (False, int, None)
    None


  public_ipv6_address_id (False, int, None)
    None


  public_vlan_id (False, int, None)
    None


  members (False, list, None)
    (Required for new resource) The hardware members of this network Gateway


  associated_vlans (False, list, None)
    The VLAN instances associated with this Network Gateway


  post_install_script_uri (False, str, None)
    None


  private_ip_address_id (False, int, None)
    None


  public_ipv4_address (False, str, None)
    None


  public_ip_address_id (False, int, None)
    None


  status (False, str, None)
    None


  name (False, str, None)
    (Required for new resource) The name of the gateway


  ssh_key_ids (False, list, None)
    None


  private_ipv4_address (False, str, None)
    None


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

