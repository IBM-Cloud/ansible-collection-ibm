
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

- IBM-Cloud terraform-provider-ibm v1.4.0
- Terraform v0.12.20



Parameters
----------

  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  resource_crn (False, str, None)
    The crn of the resource


  resource_status (False, str, None)
    The status of the resource


  ip_version (False, int, None)
    NA


  name (False, str, None)
    NA


  network_acl (False, str, None)
    NA


  public_gateway (False, str, None)
    NA


  status (False, str, None)
    NA


  identifier (True, str, None)
    NA


  ipv4_cidr_block (False, str, None)
    NA


  available_ipv4_address_count (False, str, None)
    NA


  zone (False, str, None)
    NA


  resource_name (False, str, None)
    The name of the resource


  ipv6_cidr_block (False, str, None)
    NA


  total_ipv4_address_count (False, int, None)
    NA


  vpc (False, str, None)
    NA


  generation (False, any, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

