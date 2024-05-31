
ibm_is_vpc_routing_table_route -- Configure IBM Cloud 'ibm_is_vpc_routing_table_route' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_vpc_routing_table_route' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_vpc_routing_table_route

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.65.1
- Terraform v1.5.5



Parameters
----------

  routing_table (True, str, None)
    (Required for new resource) The routing table identifier.


  next_hop (True, str, None)
    (Required for new resource) If action is deliver, the next hop that packets will be delivered to. For other action values, its address will be 0.0.0.0.


  action (False, str, deliver)
    The action to perform with a packet matching the route.


  name (False, str, None)
    The user-defined name for this route.


  zone (True, str, None)
    (Required for new resource) The zone to apply the route to. Traffic from subnets in this zone will be subject to this route.


  vpc (True, str, None)
    (Required for new resource) The VPC identifier.


  destination (True, str, None)
    (Required for new resource) The destination of the route.


  advertise (False, bool, False)
    Indicates whether this route will be advertised to the ingress sources specified by the `advertise_routes_to` routing table property.


  priority (False, int, None)
    The route's priority. Smaller values have higher priority.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

