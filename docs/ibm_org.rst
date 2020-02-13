
ibm_org -- Configure IBM Cloud 'ibm_org' resource
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_org' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  users (False, list, None)
    The IBMID of the users who will have user role in this org, ex - user@example.com


  tags (False, list, None)
    None


  name (False, str, None)
    (Required for new resource) Org name, for example myorg@domain


  org_quota_definition_guid (False, str, None)
    Org quota guid


  billing_managers (False, list, None)
    The IBMID of the users who will have billing manager role in this org, ex - user@example.com


  managers (False, list, None)
    The IBMID of the users who will have manager role in this org, ex - user@example.com


  auditors (False, list, None)
    The IBMID of the users who will have auditor role in this org, ex - user@example.com


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

