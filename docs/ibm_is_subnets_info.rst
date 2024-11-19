
ibm_is_subnets_info -- Retrieve IBM Cloud 'ibm_is_subnets' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_subnets' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_subnets

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  zone (False, str, None)
    Name of the Zone


  resource_group (False, str, None)
    Resource Group ID


  routing_table_name (False, str, None)
    Name of the routing table


  routing_table (False, str, None)
    ID of the routing table


  vpc (False, str, None)
    ID of the VPC


  vpc_name (False, str, None)
    Name of the VPC


  vpc_crn (False, str, None)
    CRN of the VPC


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

