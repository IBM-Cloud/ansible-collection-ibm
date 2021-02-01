
ibm_container_alb_cert_info -- Retrieve IBM Cloud 'ibm_container_alb_cert' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_alb_cert' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.20.0
- Terraform v0.12.20



Parameters
----------

  cluster_id (True, str, None)
    Cluster ID


  namespace (False, str, ibm-cert-store)
    Namespace of the secret


  secret_name (True, str, None)
    Secret name


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

