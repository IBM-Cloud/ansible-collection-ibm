
ibm_function_package_info -- Retrieve IBM Cloud 'ibm_function_package' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_function_package' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  annotations (False, str, None)
    All annotations set on package by user and those set by the IBM Cloud Function backend/API.


  parameters (False, str, None)
    All parameters set on package by user and those set by the IBM Cloud Function backend/API.


  bind_package_name (False, str, None)
    Name of binded package.


  name (True, str, None)
    Name of the package.


  publish (False, bool, None)
    Package Visibility.


  version (False, str, None)
    Semantic version of the package.


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

