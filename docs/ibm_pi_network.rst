
ibm_pi_network -- Configure IBM Cloud 'ibm_pi_network' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_network' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  pi_cidr (False, str, None)
    None


  pi_gateway (False, str, None)
    None


  pi_cloud_instance_id (False, str, None)
    (Required for new resource)


  network_id (False, str, None)
    None


  vlan_id (False, float, None)
    None


  pi_network_type (False, str, None)
    (Required for new resource)


  pi_network_name (False, str, None)
    (Required for new resource)


  pi_dns (False, list, None)
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

