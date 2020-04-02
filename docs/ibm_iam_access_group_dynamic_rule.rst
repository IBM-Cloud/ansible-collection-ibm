
ibm_iam_access_group_dynamic_rule -- Configure IBM Cloud 'ibm_iam_access_group_dynamic_rule' resource
=====================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_iam_access_group_dynamic_rule' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.3.0
- Terraform v0.12.20



Parameters
----------

  access_group_id (False, str, None)
    (Required for new resource) Unique identifier of the access group


  name (False, str, None)
    (Required for new resource) The name of the Rule


  expiration (False, int, None)
    (Required for new resource) The expiration in hours


  identity_provider (False, str, None)
    (Required for new resource) The realm name or identity proivider url


  conditions (False, list, None)
    (Required for new resource)


  rule_id (False, str, None)
    id of the rule


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

