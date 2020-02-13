
ibm_iam_access_group_policy -- Configure IBM Cloud 'ibm_iam_access_group_policy' resource
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_iam_access_group_policy' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  version (False, str, None)
    None


  access_group_id (False, str, None)
    (Required for new resource) ID of access group


  roles (False, list, None)
    (Required for new resource) Role names of the policy definition


  resources (False, list, None)
    None


  account_management (False, bool, False)
    Give access to all account management services


  tags (False, list, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

