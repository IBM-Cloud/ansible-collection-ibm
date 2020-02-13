
ibm_compute_autoscale_policy -- Configure IBM Cloud 'ibm_compute_autoscale_policy' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_compute_autoscale_policy' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  tags (False, list, None)
    None


  name (False, str, None)
    (Required for new resource)


  scale_type (False, str, None)
    (Required for new resource)


  scale_amount (False, int, None)
    (Required for new resource)


  cooldown (False, int, None)
    None


  scale_group_id (False, int, None)
    (Required for new resource)


  triggers (False, list, None)
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

