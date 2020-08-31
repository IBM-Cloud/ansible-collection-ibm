
ibm_lbaas -- Configure IBM Cloud 'ibm_lbaas' resource
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lbaas' resource

This module supports idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.11.1
- Terraform v0.12.20



Parameters
----------

  description (False, str, None)
    Description of a load balancer.


  protocols (False, list, None)
    Protocols to be assigned to this load balancer.


  subnets (True, list, None)
    (Required for new resource) The subnet where this Load Balancer will be provisioned.


  use_system_public_ip_pool (False, bool, None)
    in public loadbalancer - Public IP address allocation done by system public IP pool or public subnet.


  name (True, str, None)
    (Required for new resource) The load balancer's name.


  type (False, str, PUBLIC)
    Specifies if a load balancer is public or private


  ssl_ciphers (False, list, None)
    None


  wait_time_minutes (False, int, 90)
    None


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

