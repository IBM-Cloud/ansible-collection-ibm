
ibm_scc_profile -- Configure IBM Cloud 'ibm_scc_profile' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_scc_profile' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/scc_profile

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  controls (True, list, None)
    (Required for new resource) The array of controls that are used to create the profile.


  profile_name (True, str, None)
    (Required for new resource) The profile name.


  profile_type (True, str, None)
    (Required for new resource) The profile type, such as custom or predefined.


  instance_id (True, str, None)
    (Required for new resource) The ID of the Security and Compliance Center instance.


  profile_description (True, str, None)
    (Required for new resource) The profile description.


  profile_version (False, str, 0.0.0)
    The version status of the profile.


  default_parameters (False, list, None)
    The default parameters of the profile.


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

