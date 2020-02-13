
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

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  cpu_count (False, int, None)
    The capacity that the dedicated host's CPU allocation is restricted to.


  memory_capacity (False, int, None)
    The capacity that the dedicated host's memory allocation is restricted to.


  hourly_billing (False, bool, True)
    The billing type for the dedicatated host.


  router_hostname (False, str, None)
    (Required for new resource) The hostname of the primary router that the dedicated host is associated with.


  disk_capacity (False, int, None)
    The capacity that the dedicated host's disk allocation is restricted to.


  wait_time_minutes (False, int, 90)
    None


  hostname (False, str, None)
    (Required for new resource) The host name of dedicatated host.


  domain (False, str, None)
    (Required for new resource) The domain of dedicatated host.


  datacenter (False, str, None)
    (Required for new resource) The data center in which the dedicatated host is to be provisioned.


  flavor (False, str, 56_CORES_X_242_RAM_X_1_4_TB)
    The flavor of the dedicatated host.


  tags (False, list, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

