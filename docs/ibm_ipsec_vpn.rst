
ibm_ipsec_vpn -- Configure IBM Cloud 'ibm_ipsec_vpn' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_ipsec_vpn' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.23.0
- Terraform v0.12.20



Parameters
----------

  customer_peer_ip (False, str, None)
    Customer Peer IP Address


  datacenter (True, str, None)
    (Required for new resource) Datacenter name


  phase_two (False, list, None)
    None


  remote_subnet_id (False, int, None)
    Remote subnet ID value


  remote_subnet (False, list, None)
    None


  service_subnet_id (False, int, None)
    Service subnet ID value


  phase_one (False, list, None)
    None


  address_translation (False, list, None)
    None


  preshared_key (False, str, None)
    Preshared Key data


  internal_subnet_id (False, int, None)
    Internal subnet ID value


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

