
ibm_compute_autoscale_group -- Configure IBM Cloud 'ibm_compute_autoscale_group' resource
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_compute_autoscale_group' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.2
- Terraform v0.12.20



Parameters
----------

  regional_group (False, str, None)
    (Required for new resource)


  maximum_member_count (False, int, None)
    (Required for new resource)


  health_check (False, dict, None)
    None


  network_vlan_ids (False, list, None)
    None


  virtual_guest_member_template (False, list, None)
    (Required for new resource)


  tags (False, list, None)
    None


  name (False, str, None)
    (Required for new resource)


  minimum_member_count (False, int, None)
    (Required for new resource)


  cooldown (False, int, None)
    (Required for new resource)


  termination_policy (False, str, None)
    (Required for new resource)


  virtual_server_id (False, int, None)
    None


  port (False, int, None)
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

