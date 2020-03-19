
ibm_lbaas_server_instance_attachment -- Configure IBM Cloud 'ibm_lbaas_server_instance_attachment' resource
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lbaas_server_instance_attachment' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.5
- Terraform v0.12.20



Parameters
----------

  uuid (False, str, None)
    The UUID of a load balancer member


  private_ip_address (False, str, None)
    (Required for new resource) The Private IP address of a load balancer member.


  weight (False, int, None)
    The weight of a load balancer member.


  lbaas_id (False, str, None)
    (Required for new resource) The UUID of a load balancer


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

