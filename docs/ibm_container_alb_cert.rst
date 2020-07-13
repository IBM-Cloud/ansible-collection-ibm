
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

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  cert_crn (True, str, None)
    (Required for new resource) Certificate CRN id


  secret_name (True, str, None)
    (Required for new resource) Secret name


  cluster_id (True, str, None)
    (Required for new resource) Cluster ID


  domain_name (False, str, None)
    Domain name


  expires_on (False, str, None)
    Certificate expaire on date


  issuer_name (False, str, None)
    certificate issuer name


  cluster_crn (False, str, None)
    cluster CRN


  cloud_cert_instance_id (False, str, None)
    cloud cert instance ID


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

