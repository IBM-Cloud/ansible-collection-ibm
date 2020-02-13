
ibm_subnet -- Configure IBM Cloud 'ibm_subnet' resource
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_subnet' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  type (False, str, None)
    (Required for new resource)


  ip_version (False, int, 4)
    None


  vlan_id (False, int, None)
    None


  private (False, bool, False)
    None


  capacity (False, int, None)
    (Required for new resource)


  endpoint_ip (False, str, None)
    None


  subnet_cidr (False, str, None)
    None


  notes (False, str, None)
    None


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

