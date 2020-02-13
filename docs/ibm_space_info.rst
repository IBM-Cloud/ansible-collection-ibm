
ibm_space_info -- Retrieve IBM Cloud 'ibm_space' resource
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_space' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  space (True, str, None)
    Space name, for example dev


  org (True, str, None)
    The org this space belongs to


  auditors (False, list, None)
    The IBMID of the users who  have auditor role in this space, ex - user@example.com


  managers (False, list, None)
    The IBMID of the users who  have manager role in this space, ex - user@example.com


  developers (False, list, None)
    The IBMID of the users who  have developer role in this space, ex - user@example.com


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

