
ibm_is_volumes_info -- Retrieve IBM Cloud 'ibm_is_volumes' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_volumes' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_volumes

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  volume_name (False, str, None)
    Volume name identifier.


  zone_name (False, str, None)
    Zone name identifier.


  attachment_state (False, str, None)
    Attachment state of the Volume.


  encryption (False, str, None)
    Encryption type of Volume.


  operating_system_family (False, str, None)
    Operating system family of the Volume.


  operating_system_architecture (False, str, None)
    Operating system architecture of the Volume.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

