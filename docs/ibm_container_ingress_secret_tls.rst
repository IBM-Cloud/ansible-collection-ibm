
ibm_container_ingress_secret_tls -- Configure IBM Cloud 'ibm_container_ingress_secret_tls' resource
===================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_ingress_secret_tls' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_ingress_secret_tls

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  update_secret (False, int, None)
    Updates secret from secrets manager if value is changed (increment each usage)


  secret_namespace (True, str, None)
    (Required for new resource) Secret namespace


  cert_crn (True, str, None)
    (Required for new resource) Certificate CRN


  persistence (False, bool, None)
    Persistence of secret


  cluster (True, str, None)
    (Required for new resource) Cluster ID or name


  secret_name (True, str, None)
    (Required for new resource) Secret name


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

