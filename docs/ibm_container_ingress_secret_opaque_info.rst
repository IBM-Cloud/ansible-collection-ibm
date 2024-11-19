
ibm_container_ingress_secret_opaque_info -- Retrieve IBM Cloud 'ibm_container_ingress_secret_opaque' resource
=============================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_container_ingress_secret_opaque' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/container_ingress_secret_opaque

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  cluster (True, str, None)
    Cluster ID or name


  secret_name (True, str, None)
    Secret name


  secret_namespace (True, str, None)
    Secret namespace


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

