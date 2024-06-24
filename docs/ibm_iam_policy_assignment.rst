
ibm_iam_policy_assignment -- Configure IBM Cloud 'ibm_iam_policy_assignment' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_iam_policy_assignment' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/iam_policy_assignment

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  version (True, str, None)
    (Required for new resource) specify version of response body format.


  templates (True, list, None)
    (Required for new resource) policy template details.


  target (True, dict, None)
    (Required for new resource) assignment target details


  accept_language (False, str, default)
    Language code for translations* `default` - English* `de` -  German (Standard)* `en` - English* `es` - Spanish (Spain)* `fr` - French (Standard)* `it` - Italian (Standard)* `ja` - Japanese* `ko` - Korean* `pt-br` - Portuguese (Brazil)* `zh-cn` - Chinese (Simplified, PRC)* `zh-tw` - (Chinese, Taiwan).


  options (True, list, None)
    (Required for new resource) The set of properties required for a policy assignment.


  template_version (False, str, None)
    The policy template version.


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

