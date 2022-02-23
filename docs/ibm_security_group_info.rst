
ibm_security_group_info -- Retrieve IBM Cloud 'ibm_security_group' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_security_group' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/security_group

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.38.2
- Terraform v0.12.20



Parameters
----------

  most_recent (False, bool, False)
    If true and multiple entries are found, the most recently created group is used. If false, an error is returned


  name (True, str, None)
    The name of the security group


  description (False, str, None)
    The description of the security group


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

