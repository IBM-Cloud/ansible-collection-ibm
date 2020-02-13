
ibm_space -- Configure IBM Cloud 'ibm_space' resource
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_space' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  space_quota (False, str, None)
    The name of the Space Quota Definition


  tags (False, list, None)
    None


  name (False, str, None)
    (Required for new resource) The name for the space


  org (False, str, None)
    (Required for new resource) The org this space belongs to


  auditors (False, list, None)
    The IBMID of the users who will have auditor role in this space, ex - user@example.com


  managers (False, list, None)
    The IBMID of the users who will have manager role in this space, ex - user@example.com


  developers (False, list, None)
    The IBMID of the users who will have developer role in this space, ex - user@example.com


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

