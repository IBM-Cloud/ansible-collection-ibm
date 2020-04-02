
ibm_lbaas -- Configure IBM Cloud 'ibm_lbaas' resource
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lbaas' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.3.0
- Terraform v0.12.20



Parameters
----------

  type (False, str, PUBLIC)
    Specifies if a load balancer is public or private


  wait_time_minutes (False, int, 90)
    None


  name (False, str, None)
    (Required for new resource) The load balancer's name.


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  status (False, str, None)
    The operation status 'ONLINE' or 'OFFLINE' of a load balancer.


  ssl_ciphers (False, list, None)
    None


  subnets (False, list, None)
    (Required for new resource) The subnet where this Load Balancer will be provisioned.


  datacenter (False, str, None)
    None


  vip (False, str, None)
    The virtual ip address of this load balancer


  use_system_public_ip_pool (False, bool, None)
    Applicable for public load balancer only. It specifies whether the public IP addresses are allocated from system public IP pool or public subnet from the account ordering the load balancer.


  protocols (False, list, None)
    Protocols to be assigned to this load balancer.


  health_monitors (False, list, None)
    None


  resource_name (False, str, None)
    The name of the resource


  resource_status (False, str, None)
    The status of the resource


  description (False, str, None)
    Description of a load balancer.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

