
ibm_compute_dedicated_host -- Configure IBM Cloud 'ibm_compute_dedicated_host' resource
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_compute_dedicated_host' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.0
- Terraform v0.12.20



Parameters
----------

  domain (False, str, None)
    (Required for new resource) The domain of dedicatated host.


  datacenter (False, str, None)
    (Required for new resource) The data center in which the dedicatated host is to be provisioned.


  flavor (False, str, 56_CORES_X_242_RAM_X_1_4_TB)
    The flavor of the dedicatated host.


  disk_capacity (False, int, None)
    The capacity that the dedicated host's disk allocation is restricted to.


  wait_time_minutes (False, int, 90)
    None


  hostname (False, str, None)
    (Required for new resource) The host name of dedicatated host.


  hourly_billing (False, bool, True)
    The billing type for the dedicatated host.


  router_hostname (False, str, None)
    (Required for new resource) The hostname of the primary router that the dedicated host is associated with.


  cpu_count (False, int, None)
    The capacity that the dedicated host's CPU allocation is restricted to.


  memory_capacity (False, int, None)
    The capacity that the dedicated host's memory allocation is restricted to.


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

