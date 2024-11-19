
ibm_scc_profile_attachment -- Configure IBM Cloud 'ibm_scc_profile_attachment' resource
=======================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_scc_profile_attachment' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/scc_profile_attachment

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  schedule (True, str, None)
    (Required for new resource) The schedule of an attachment evaluation.


  name (True, str, None)
    (Required for new resource) The name of the attachment.


  description (False, str, None)
    The description for the attachment.


  profile_id (True, str, None)
    (Required for new resource) The ID of the profile that is specified in the attachment.


  attachment_parameters (False, list, None)
    The profile parameters for the attachment.


  status (True, str, None)
    (Required for new resource) The status of an attachment evaluation.


  notifications (False, list, None)
    The request payload of the attachment notifications.


  instance_id (True, str, None)
    (Required for new resource) The ID of the Security and Compliance Center instance.


  scope (True, list, None)
    (Required for new resource) The scope payload for the multi cloud feature.


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

