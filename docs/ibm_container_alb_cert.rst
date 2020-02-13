
ibm_container_alb_cert -- Configure IBM Cloud 'ibm_container_alb_cert' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_alb_cert' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  expires_on (False, str, None)
    None


  cloud_cert_instance_id (False, str, None)
    None


  cluster_crn (False, str, None)
    None


  region (False, str, None)
    None


  cert_crn (False, str, None)
    (Required for new resource)


  cluster_id (False, str, None)
    (Required for new resource)


  secret_name (False, str, None)
    (Required for new resource)


  domain_name (False, str, None)
    None


  issuer_name (False, str, None)
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

