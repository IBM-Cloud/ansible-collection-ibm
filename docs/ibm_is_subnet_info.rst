
ibm_is_subnet_info -- Retrieve IBM Cloud 'ibm_is_subnet' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_subnet' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  vpc (False, str, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  identifier (True, str, None)
    None


  ipv6_cidr_block (False, str, None)
    None


  name (False, str, None)
    None


  network_acl (False, str, None)
    None


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  available_ipv4_address_count (False, str, None)
    None


  status (False, str, None)
    None


  resource_crn (False, str, None)
    The crn of the resource


  resource_status (False, str, None)
    The status of the resource


  total_ipv4_address_count (False, int, None)
    None


  ip_version (False, int, None)
    None


  public_gateway (False, str, None)
    None


  resource_name (False, str, None)
    The name of the resource


  ipv4_cidr_block (False, str, None)
    None


  zone (False, str, None)
    None


  generation (False, any, 2)
    IBM Cloud infrastructure generation.


  ibmcloud_api_key (False, any, None)
    (Required when generation = 2) The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environmental variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environmental variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

