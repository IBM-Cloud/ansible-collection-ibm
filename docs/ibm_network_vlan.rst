
ibm_network_vlan -- Configure IBM Cloud 'ibm_network_vlan' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_network_vlan' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  softlayer_managed (False, bool, None)
    None


  child_resource_count (False, int, None)
    None


  tags (False, list, None)
    None


  resource_name (False, str, None)
    The name of the resource


  datacenter (False, str, None)
    (Required for new resource)


  type (False, str, None)
    (Required for new resource)


  name (False, str, None)
    None


  subnets (False, list, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  router_hostname (False, str, None)
    None


  vlan_number (False, int, None)
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

