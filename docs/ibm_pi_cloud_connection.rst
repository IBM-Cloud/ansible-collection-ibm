
ibm_pi_cloud_connection -- Configure IBM Cloud 'ibm_pi_cloud_connection' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_cloud_connection' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_cloud_connection

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  pi_cloud_connection_gre_destination_address (False, str, None)
    GRE destination IP address


  pi_cloud_connection_vpc_crns (False, list, None)
    Set of VPCs to attach to this cloud connection


  pi_cloud_connection_transit_enabled (False, bool, False)
    Enable transit gateway for this cloud connection


  pi_cloud_instance_id (True, str, None)
    (Required for new resource) PI cloud instance ID


  pi_cloud_connection_global_routing (False, bool, False)
    Enable global routing for this cloud connection


  pi_cloud_connection_networks (False, list, None)
    Set of Networks to attach to this cloud connection


  pi_cloud_connection_classic_enabled (False, bool, False)
    Enable classic endpoint destination


  pi_cloud_connection_vpc_enabled (False, bool, False)
    Enable VPC for this cloud connection


  pi_cloud_connection_name (True, str, None)
    (Required for new resource) Name of the cloud connection


  pi_cloud_connection_speed (True, int, None)
    (Required for new resource) Speed of the cloud connection (speed in megabits per second)


  pi_cloud_connection_gre_cidr (False, str, None)
    GRE network in CIDR notation


  pi_cloud_connection_metered (False, bool, False)
    Enable metered for this cloud connection


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

