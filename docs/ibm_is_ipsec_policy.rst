
ibm_is_ipsec_policy -- Configure IBM Cloud 'ibm_is_ipsec_policy' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_ipsec_policy' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.0
- Terraform v0.12.20



Parameters
----------

  name (False, str, None)
    (Required for new resource) IPSEC name


  resource_group (False, str, None)
    Resource group info


  transform_protocol (False, str, None)
    IPSEC transform protocol


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  resource_name (False, str, None)
    The name of the resource


  authentication_algorithm (False, str, None)
    (Required for new resource) Authentication alorothm


  encryption_algorithm (False, str, None)
    (Required for new resource) Encryption algorithm


  pfs (False, str, None)
    (Required for new resource) PFS info


  key_lifetime (False, int, 3600)
    IPSEC key lifetime


  encapsulation_mode (False, str, None)
    IPSEC encapsulation mode


  vpn_connections (False, list, None)
    None


  resource_crn (False, str, None)
    The crn of the resource


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, any, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

