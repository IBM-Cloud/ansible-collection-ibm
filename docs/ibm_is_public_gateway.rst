
ibm_is_public_gateway -- Configure IBM Cloud 'ibm_is_public_gateway' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_public_gateway' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.0
- Terraform v0.12.20



Parameters
----------

  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  resource_status (False, str, None)
    The status of the resource


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  status (False, str, None)
    Public gateway instance status


  vpc (False, str, None)
    (Required for new resource) Public gateway VPC info


  zone (False, str, None)
    (Required for new resource) Public gateway zone info


  tags (False, list, None)
    Service tags for the public gateway instance


  resource_crn (False, str, None)
    The crn of the resource


  name (False, str, None)
    (Required for new resource) Name of the Public gateway instance


  floating_ip (False, dict, None)
    None


  resource_group (False, str, None)
    Public gateway resource group info


  resource_name (False, str, None)
    The name of the resource


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

