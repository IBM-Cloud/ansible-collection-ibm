
ibm_compute_dedicated_host -- Configure IBM Cloud 'ibm_compute_dedicated_host' resource
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_compute_dedicated_host' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/compute_dedicated_host

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.39.1
- Terraform v0.12.20



Parameters
----------

  hostname (True, str, None)
    (Required for new resource) The host name of dedicatated host.


  datacenter (True, str, None)
    (Required for new resource) The data center in which the dedicatated host is to be provisioned.


  flavor (False, str, 56_CORES_X_242_RAM_X_1_4_TB)
    The flavor of the dedicatated host.


  hourly_billing (False, bool, True)
    The billing type for the dedicatated host.


  wait_time_minutes (False, int, 90)
    None


  domain (True, str, None)
    (Required for new resource) The domain of dedicatated host.


  router_hostname (True, str, None)
    (Required for new resource) The hostname of the primary router that the dedicated host is associated with.


  tags (False, list, None)
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

