
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

- IBM-Cloud terraform-provider-ibm v1.3.0
- Terraform v0.12.20



Parameters
----------

  public_ipv4_address (False, str, None)
    None


  public_vlan_id (False, int, None)
    None


  members (False, list, None)
    (Required for new resource) The hardware members of this network Gateway


  name (False, str, None)
    (Required for new resource) The name of the gateway


  ssh_key_ids (False, list, None)
    None


  post_install_script_uri (False, str, None)
    None


  private_ip_address_id (False, int, None)
    None


  private_ipv4_address (False, str, None)
    None


  private_vlan_id (False, int, None)
    None


  public_ip_address_id (False, int, None)
    None


  public_ipv6_address_id (False, int, None)
    None


  status (False, str, None)
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


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

