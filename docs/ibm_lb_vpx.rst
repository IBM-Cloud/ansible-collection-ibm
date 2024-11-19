
ibm_lb_vpx -- Configure IBM Cloud 'ibm_lb_vpx' resource
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lb_vpx' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/lb_vpx

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  speed (True, int, None)
    (Required for new resource) Speed value


  plan (True, str, None)
    (Required for new resource) Plan info


  tags (False, list, None)
    List of the tags


  version (True, str, None)
    (Required for new resource) version info


  public_vlan_id (False, int, None)
    Piblic VLAN id


  public_subnet (False, str, None)
    Public subnet


  private_vlan_id (False, int, None)
    Private VLAN id


  private_subnet (False, str, None)
    Private subnet


  datacenter (True, str, None)
    (Required for new resource) Datacenter name


  ip_count (True, int, None)
    (Required for new resource) IP address count


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

