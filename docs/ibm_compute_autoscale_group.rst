
ibm_compute_autoscale_group -- Configure IBM Cloud 'ibm_compute_autoscale_group' resource
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_compute_autoscale_group' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/compute_autoscale_group

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  termination_policy (True, str, None)
    (Required for new resource) Termination policy


  health_check (False, dict, None)
    None


  virtual_guest_member_template (True, list, None)
    (Required for new resource) Virtual guest member template


  tags (False, list, None)
    List of tags


  name (True, str, None)
    (Required for new resource) Name


  regional_group (True, str, None)
    (Required for new resource) regional group


  minimum_member_count (True, int, None)
    (Required for new resource) Minimum member count


  cooldown (True, int, None)
    (Required for new resource) Cooldown value


  maximum_member_count (True, int, None)
    (Required for new resource) Maximum member count


  virtual_server_id (False, int, None)
    virtual server ID


  port (False, int, None)
    Port number


  network_vlan_ids (False, list, None)
    List of network VLAN ids


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

