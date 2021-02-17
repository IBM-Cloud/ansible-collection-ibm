
ibm_multi_vlan_firewall -- Configure IBM Cloud 'ibm_multi_vlan_firewall' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_multi_vlan_firewall' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.21.0
- Terraform v0.12.20



Parameters
----------

  firewall_type (True, str, None)
    (Required for new resource) Firewall type


  addon_configuration (False, list, None)
    High Availability - [Web Filtering Add-on, NGFW Add-on, AV Add-on] or [Web Filtering Add-on, NGFW Add-on, AV Add-on]


  datacenter (True, str, None)
    (Required for new resource) Datacenter name


  pod (True, str, None)
    (Required for new resource) POD name


  name (True, str, None)
    (Required for new resource) name


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

