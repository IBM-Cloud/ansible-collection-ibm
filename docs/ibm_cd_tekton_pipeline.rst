
ibm_cd_tekton_pipeline -- Configure IBM Cloud 'ibm_cd_tekton_pipeline' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cd_tekton_pipeline' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cd_tekton_pipeline

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  enable_partial_cloning (False, bool, False)
    Flag to enable partial cloning for this pipeline. When partial clone is enabled, only the files contained within the paths specified in definition repositories are read and cloned, this means that symbolic links might not work. If omitted, this feature is disabled by default.


  next_build_number (False, int, None)
    The build number that will be used for the next pipeline run.


  pipeline_id (True, str, None)
    (Required for new resource) String.


  worker (False, list, None)
    Details of the worker used to run the pipeline.


  enable_notifications (False, bool, False)
    Flag to enable notifications for this pipeline. If enabled, the Tekton pipeline run events will be published to all the destinations specified by the Slack and Event Notifications integrations in the parent toolchain. If omitted, this feature is disabled by default.


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

