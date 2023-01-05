
ibm_scc_posture_collector -- Configure IBM Cloud 'ibm_scc_posture_collector' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_scc_posture_collector' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/scc_posture_collector

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.48.0
- Terraform v0.12.20



Parameters
----------

  name (True, str, None)
    (Required for new resource) A unique name for your collector.


  is_public (True, bool, None)
    (Required for new resource) Determines whether the collector endpoint is accessible on a public network. If set to `true`, the collector connects to resources in your account over a public network. If set to `false`, the collector connects to resources by using a private IP that is accessible only through the IBM Cloud private network.


  managed_by (True, str, None)
    (Required for new resource) Determines whether the collector is an IBM or customer-managed virtual machine. Use `ibm` to allow Security and Compliance Center to create, install, and manage the collector on your behalf. The collector is installed in an OpenShift cluster and approved automatically for use. Use `customer` if you would like to install the collector by using your own virtual machine. For more information, check out the [docs](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-collector).


  description (False, str, None)
    A detailed description of the collector.


  passphrase (False, str, None)
    To protect the credentials that you add to the service, a passphrase is used to generate a data encryption key. The key is used to securely store your credentials and prevent anyone from accessing them.


  is_ubi_image (False, bool, None)
    Determines whether the collector has a Ubi image.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

