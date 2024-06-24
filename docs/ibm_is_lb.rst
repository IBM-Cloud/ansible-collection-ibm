
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

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  type (False, str, public)
    Load Balancer type


  name (True, str, None)
    (Required for new resource) Load Balancer name


  security_groups (False, list, None)
    Load Balancer securitygroups list


  resource_group (False, str, None)
    None


  route_mode (False, bool, False)
    Indicates whether route mode is enabled for this load balancer


  logging (False, bool, False)
    Logging of Load Balancer


  subnets (True, list, None)
    (Required for new resource) Load Balancer subnets list


  tags (False, list, None)
    None


  dns (False, list, None)
    The DNS configuration for this load balancer.


  access_tags (False, list, None)
    List of access management tags


  profile (False, str, None)
    The profile to use for this load balancer.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

