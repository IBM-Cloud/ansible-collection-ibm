
ibm_lb_service_group -- Configure IBM Cloud 'ibm_lb_service_group' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lb_service_group' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.3
- Terraform v0.12.20



Parameters
----------

  virtual_server_id (False, int, None)
    Virtual server ID


  service_group_id (False, int, None)
    Service group ID


  allocation (False, int, None)
    (Required for new resource) Allocation type


  routing_method (False, str, None)
    (Required for new resource) Routing method


  tags (False, list, None)
    List of tags


  load_balancer_id (False, int, None)
    (Required for new resource) Loadbalancer ID


  port (False, int, None)
    (Required for new resource) Port number


  routing_type (False, str, None)
    (Required for new resource) Routing type


  timeout (False, int, None)
    Timeout value


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

