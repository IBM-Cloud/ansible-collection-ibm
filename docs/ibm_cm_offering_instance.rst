
ibm_cm_offering_instance -- Configure IBM Cloud 'ibm_cm_offering_instance' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cm_offering_instance' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cm_offering_instance

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  cluster_region (True, str, None)
    (Required for new resource) Cluster region (e.g., us-south).


  cluster_namespaces (True, list, None)
    (Required for new resource) List of target namespaces to install into.


  offering_id (True, str, None)
    (Required for new resource) Offering ID this instance was created from.


  version (True, str, None)
    (Required for new resource) The version this instance was installed from (not version id).


  label (True, str, None)
    (Required for new resource) the label for this instance.


  kind_format (True, str, None)
    (Required for new resource) the format this instance has (helm, operator, ova...).


  cluster_all_namespaces (True, bool, None)
    (Required for new resource) designate to install into all namespaces.


  install_plan (False, str, None)
    install plan for the subscription of the operator- can be either automatic or manual. Required for operator bundles


  channel (False, str, None)
    channel to target for the operator subscription. Required for operator bundles


  wait_until_successful (False, bool, True)
    Whether to wait until the offering instance successfully provisions, or to return when accepted


  resource_group_id (False, str, None)
    id of the resource group


  parent_crn (False, str, None)
    CRN of parent instance


  cluster_id (True, str, None)
    (Required for new resource) Cluster ID.


  catalog_id (True, str, None)
    (Required for new resource) Catalog ID this instance was created from.


  plan_id (False, str, None)
    id of the plan


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


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

