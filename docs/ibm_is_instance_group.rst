
ibm_is_instance_group -- Configure IBM Cloud 'ibm_is_instance_group' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_instance_group' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance_group

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.24.0
- Terraform v0.12.20



Parameters
----------

  instance_template (True, str, None)
    (Required for new resource) instance template ID


  instance_count (False, int, 0)
    The number of instances in the instance group


  resource_group (False, str, None)
    Resource group ID


  subnets (True, list, None)
    (Required for new resource) list of subnet IDs


  application_port (False, int, None)
    Used by the instance group when scaling up instances to supply the port for the load balancer pool member.


  name (True, str, None)
    (Required for new resource) The user-defined name for this instance group


  load_balancer (False, str, None)
    load balancer ID


  load_balancer_pool (False, str, None)
    load balancer pool ID


  tags (False, list, None)
    List of tags for instance group


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

