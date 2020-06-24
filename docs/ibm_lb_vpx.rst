
ibm_lb_vpx -- Configure IBM Cloud 'ibm_lb_vpx' resource
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lb_vpx' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.8.0
- Terraform v0.12.20



Parameters
----------

  public_vlan_id (False, int, None)
    Piblic VLAN id


  vip_pool (False, list, None)
    List of VIP ids


  management_ip_address (False, str, None)
    management IP address


  tags (False, list, None)
    List of the tags


  version (False, str, None)
    (Required for new resource) version info


  plan (False, str, None)
    (Required for new resource) Plan info


  ip_count (False, int, None)
    (Required for new resource) IP address count


  name (False, str, None)
    Name


  type (False, str, None)
    Type of the VPX


  public_subnet (False, str, None)
    Public subnet


  private_vlan_id (False, int, None)
    Private VLAN id


  private_subnet (False, str, None)
    Private subnet


  datacenter (False, str, None)
    (Required for new resource) Datacenter name


  speed (False, int, None)
    (Required for new resource) Speed value


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

