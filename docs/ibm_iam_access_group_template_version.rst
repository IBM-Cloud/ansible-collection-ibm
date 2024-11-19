
ibm_iam_access_group_template_version -- Configure IBM Cloud 'ibm_iam_access_group_template_version' resource
=============================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_iam_access_group_template_version' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/iam_access_group_template_version

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  template_id (True, str, None)
    (Required for new resource) ID of the template that you want to create a new version of.


  name (False, str, None)
    The name of the access group template.


  policy_template_references (False, list, None)
    References to policy templates assigned to the access group template.


  description (False, str, None)
    The description of the access group template.


  committed (False, bool, None)
    A boolean indicating whether the access group template is committed. You must commit a template before you can assign it to child accounts.


  transaction_id (False, str, None)
    An optional transaction id for the request.


  group (False, list, None)
    Access Group Component.


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

