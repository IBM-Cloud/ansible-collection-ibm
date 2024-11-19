
ibm_cd_tekton_pipeline_property -- Configure IBM Cloud 'ibm_cd_tekton_pipeline_property' resource
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cd_tekton_pipeline_property' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cd_tekton_pipeline_property

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  path (False, str, None)
    A dot notation path for `integration` type properties only, that selects a value from the tool integration. If left blank the full tool integration data will be used.


  pipeline_id (True, str, None)
    (Required for new resource) The Tekton pipeline ID.


  name (True, str, None)
    (Required for new resource) Property name.


  value (False, str, None)
    Property value. Any string value is valid.


  enum (False, list, None)
    Options for `single_select` property type. Only needed when using `single_select` property type.


  type (True, str, None)
    (Required for new resource) Property type.


  locked (False, bool, False)
    When true, this property cannot be overridden by a trigger property or at runtime. Attempting to override it will result in run requests being rejected. The default is false.


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

