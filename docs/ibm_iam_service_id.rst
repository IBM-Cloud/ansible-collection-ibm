
ibm_iam_service_id -- Configure IBM Cloud 'ibm_iam_service_id' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_iam_service_id' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  version (False, str, None)
    version of the serviceID


  crn (False, str, None)
    crn of the serviceID


  tags (False, list, None)
    None


  name (False, str, None)
    (Required for new resource) Name of the serviceID


  description (False, str, None)
    Description of the serviceID


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

