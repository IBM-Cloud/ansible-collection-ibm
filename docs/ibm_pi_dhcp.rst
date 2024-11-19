
ibm_pi_dhcp -- Configure IBM Cloud 'ibm_pi_dhcp' resource
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_dhcp' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_dhcp

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  pi_cloud_instance_id (True, str, None)
    (Required for new resource) PI cloud instance ID


  pi_dhcp_snat_enabled (False, bool, True)
    Indicates if SNAT will be enabled for the DHCP service


  pi_cidr (False, str, None)
    Optional cidr for DHCP private network


  pi_dhcp_name (False, str, None)
    Optional name of DHCP Service (will be prefixed by DHCP identifier)


  pi_dns_server (False, str, None)
    Optional DNS Server for DHCP service


  pi_cloud_connection_id (False, str, None)
    Optional cloud connection uuid to connect with DHCP private network


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  zone (False, str, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environment variable 'IC_ZONE'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

