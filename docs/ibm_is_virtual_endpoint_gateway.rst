
ibm_is_virtual_endpoint_gateway -- Configure IBM Cloud 'ibm_is_virtual_endpoint_gateway' resource
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_virtual_endpoint_gateway' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_virtual_endpoint_gateway

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.65.1
- Terraform v1.5.5



Parameters
----------

  name (True, str, None)
    (Required for new resource) Endpoint gateway name


  vpc (True, str, None)
    (Required for new resource) The VPC id


  tags (False, list, None)
    List of tags for VPE


  allow_dns_resolution_binding (False, bool, None)
    Indicates whether to allow this endpoint gateway to participate in DNS resolution bindings with a VPC that has dns.enable_hub set to true.


  resource_group (False, str, None)
    The resource group id


  security_groups (False, list, None)
    Endpoint gateway securitygroups list


  ips (False, list, None)
    Endpoint gateway IPs


  target (True, list, None)
    (Required for new resource) Endpoint gateway target


  access_tags (False, list, None)
    List of access management tags


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

