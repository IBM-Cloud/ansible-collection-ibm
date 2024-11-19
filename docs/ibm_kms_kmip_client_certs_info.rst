
ibm_kms_kmip_client_certs_info -- Retrieve IBM Cloud 'ibm_kms_kmip_client_certs' resource
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_kms_kmip_client_certs' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/kms_kmip_client_certs

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  instance_id (True, str, None)
    Key protect Instance GUID


  adapter_id (False, str, None)
    The id of the KMIP adapter that contains the cert


  adapter_name (False, str, None)
    The name of the KMIP adapter that contains the cert


  show_total_count (False, bool, None)
    Flag to return the count of how many adapters there are in total


  endpoint_type (False, str, None)
    public or private


  limit (False, int, None)
    Limit of how many adapters to be fetched


  offset (False, int, None)
    Offset of adapters to be fetched


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

