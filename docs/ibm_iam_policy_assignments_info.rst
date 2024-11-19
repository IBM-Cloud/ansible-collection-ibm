
ibm_iam_policy_assignments_info -- Retrieve IBM Cloud 'ibm_iam_policy_assignments' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_iam_policy_assignments' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/iam_policy_assignments

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  version (False, str, 1.0)
    specify version of response body format.


  accept_language (False, str, default)
    Language code for translations* `default` - English* `de` -  German (Standard)* `en` - English* `es` - Spanish (Spain)* `fr` - French (Standard)* `it` - Italian (Standard)* `ja` - Japanese* `ko` - Korean* `pt-br` - Portuguese (Brazil)* `zh-cn` - Chinese (Simplified, PRC)* `zh-tw` - (Chinese, Taiwan).


  template_id (False, str, None)
    Optional template id.


  template_version (False, str, None)
    Optional policy template version.


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

