
ibm_pi_network -- Configure IBM Cloud 'ibm_pi_network' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_network' resource

This module supports idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.16.1
- Terraform v0.12.20



Parameters
----------

  pi_cloud_instance_id (True, str, None)
    (Required for new resource) PI cloud instance ID


  pi_network_type (True, str, None)
    (Required for new resource) PI network type


  pi_network_name (True, str, None)
    (Required for new resource) PI network name


  pi_dns (False, list, None)
    List of PI network DNS name


  pi_cidr (False, str, None)
    PI network CIDR


  pi_gateway (False, str, None)
    PI network gateway


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

