
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

- IBM-Cloud terraform-provider-ibm v1.8.0
- Terraform v0.12.20



Parameters
----------

  domain_name (False, str, None)
    Domain name


  issuer_name (False, str, None)
    certificate issuer name


  cluster_crn (False, str, None)
    cluster CRN


  cloud_cert_instance_id (False, str, None)
    cloud cert instance ID


  region (False, str, None)
    region name


  cert_crn (False, str, None)
    (Required for new resource) Certificate CRN id


  cluster_id (False, str, None)
    (Required for new resource) Cluster ID


  secret_name (False, str, None)
    (Required for new resource) Secret name


  expires_on (False, str, None)
    Certificate expaire on date


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

