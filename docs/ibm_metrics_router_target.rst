
ibm_metrics_router_target -- Configure IBM Cloud 'ibm_metrics_router_target' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_metrics_router_target' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/metrics_router_target

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  name (True, str, None)
    (Required for new resource) The name of the target. The name must be 1000 characters or less, and cannot include any special characters other than `(space) - . _ :`. Do not include any personal identifying information (PII) in any resource names.


  destination_crn (True, str, None)
    (Required for new resource) The CRN of a destination service instance or resource. Ensure you have a service authorization between IBM Cloud Metrics Routing and your Cloud resource. Read [S2S authorization](https://cloud.ibm.com/docs/metrics-router?topic=metrics-router-target-monitoring&interface=ui#target-monitoring-ui) for details.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

