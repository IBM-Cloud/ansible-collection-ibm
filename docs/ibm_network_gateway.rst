
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

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  post_install_script_uri (False, str, None)
    None


  private_ip_address_id (False, int, None)
    None


  private_ipv4_address (False, str, None)
    None


  public_ipv4_address (False, str, None)
    None


  status (False, str, None)
    None


  members (False, list, None)
    (Required for new resource) The hardware members of this network Gateway


  name (False, str, None)
    (Required for new resource) The name of the gateway


  ssh_key_ids (False, list, None)
    None


  private_vlan_id (False, int, None)
    None


  public_ip_address_id (False, int, None)
    None


  public_ipv6_address_id (False, int, None)
    None


  public_vlan_id (False, int, None)
    None


  associated_vlans (False, list, None)
    The VLAN instances associated with this Network Gateway


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

