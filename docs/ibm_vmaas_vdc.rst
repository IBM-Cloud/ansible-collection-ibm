
ibm_vmaas_vdc -- Configure IBM Cloud 'ibm_vmaas_vdc' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_vmaas_vdc' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/vmaas_vdc

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  name (True, str, None)
    (Required for new resource) A human readable ID for the virtual data center (VDC).


  ram (False, int, None)
    The RAM usage limit on the virtual data center (VDC) in GB (1024^3 bytes). Supported for VDCs deployed on a multitenant Cloud Director site. This property is applicable when the resource pool type is reserved.


  accept_language (False, str, None)
    Language.


  windows_byol (False, bool, False)
    Indicates if the Microsoft Windows VMs will be using the license from IBM or the customer will use their own license (BYOL).


  director_site (True, list, None)
    (Required for new resource) The Cloud Director site in which to deploy the virtual data center (VDC).


  cpu (False, int, None)
    The vCPU usage limit on the virtual data center (VDC). Supported for VDCs deployed on a multitenant Cloud Director site. This property is applicable when the resource pool type is reserved.


  fast_provisioning_enabled (False, bool, None)
    Determines whether this virtual data center has fast provisioning enabled or not.


  rhel_byol (False, bool, False)
    Indicates if the RHEL VMs will be using the license from IBM or the customer will use their own license (BYOL).


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

