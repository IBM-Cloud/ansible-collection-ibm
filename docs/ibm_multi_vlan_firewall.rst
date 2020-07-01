
ibm_multi_vlan_firewall -- Configure IBM Cloud 'ibm_multi_vlan_firewall' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_multi_vlan_firewall' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  public_ip (False, str, None)
    Public IP Address


  username (False, str, None)
    User name


  addon_configuration (False, list, None)
    High Availability - [Web Filtering Add-on, NGFW Add-on, AV Add-on] or [Web Filtering Add-on, NGFW Add-on, AV Add-on]


  datacenter (True, str, None)
    (Required for new resource) Datacenter name


  pod (True, str, None)
    (Required for new resource) POD name


  name (True, str, None)
    (Required for new resource) name


  public_vlan_id (False, int, None)
    Public VLAN id


  private_vlan_id (False, int, None)
    Private VLAN id


  firewall_type (True, str, None)
    (Required for new resource) Firewall type


  public_ipv6 (False, str, None)
    Public IPV6 IP


  private_ip (False, str, None)
    Private IP Address


  password (False, str, None)
    Password


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

