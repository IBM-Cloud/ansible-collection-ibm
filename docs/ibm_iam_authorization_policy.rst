
ibm_iam_authorization_policy -- Configure IBM Cloud 'ibm_iam_authorization_policy' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_iam_authorization_policy' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  source_resource_type (False, str, None)
    Resource type of source service


  source_service_account (False, str, None)
    Account GUID of source service


  source_resource_instance_id (False, str, None)
    The source resource instance Id


  target_service_name (False, str, None)
    (Required for new resource) The target service name


  roles (False, list, None)
    (Required for new resource) Role names of the policy definition


  target_resource_instance_id (False, str, None)
    The target resource instance Id


  target_resource_type (False, str, None)
    Resource type of target service


  version (False, str, None)
    None


  source_service_name (False, str, None)
    (Required for new resource) The source service name


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

