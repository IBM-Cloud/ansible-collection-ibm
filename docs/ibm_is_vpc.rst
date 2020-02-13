
ibm_is_vpc -- Configure IBM Cloud 'ibm_is_vpc' resource
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_vpc' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  default_network_acl (False, str, None)
    None


  classic_access (False, bool, False)
    None


  name (False, str, None)
    (Required for new resource)


  default_security_group (False, str, None)
    None


  resource_name (False, str, None)
    The name of the resource


  address_prefix_management (False, str, auto)
    None


  resource_group (False, str, None)
    None


  resource_crn (False, str, None)
    The crn of the resource


  status (False, str, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  tags (False, list, None)
    None


  resource_status (False, str, None)
    The status of the resource


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


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

