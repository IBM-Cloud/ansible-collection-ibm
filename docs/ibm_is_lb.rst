
ibm_is_lb -- Configure IBM Cloud 'ibm_is_lb' resource
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_lb' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_lb

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.26.2
- Terraform v0.12.20



Parameters
----------

  tags (False, list, None)
    None


  resource_group (False, str, None)
    None


  type (False, str, public)
    Load Balancer type


  profile (False, str, None)
    The profile to use for this load balancer.


  name (True, str, None)
    (Required for new resource) Load Balancer name


  security_groups (False, list, None)
    Load Balancer securitygroups list


  logging (False, bool, False)
    Logging of Load Balancer


  subnets (True, list, None)
    (Required for new resource) Load Balancer subnets list


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

