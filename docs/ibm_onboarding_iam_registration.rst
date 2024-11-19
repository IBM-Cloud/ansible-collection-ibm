
ibm_onboarding_iam_registration -- Configure IBM Cloud 'ibm_onboarding_iam_registration' resource
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_onboarding_iam_registration' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/onboarding_iam_registration

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  supported_authorization_subjects (False, list, None)
    The list of supported authorization subjects.


  actions (False, list, None)
    The product access management action.


  env (False, str, None)
    The environment to fetch this object from.


  name (True, str, None)
    (Required for new resource) The IAM registration name, which must be the programmatic name of the product.


  supported_anonymous_accesses (False, list, None)
    The list of supported anonymous accesses.


  product_id (True, str, None)
    (Required for new resource) The unique ID of the product.


  additional_policy_scopes (False, list, None)
    List of additional policy scopes.


  display_name (False, list, None)
    The display name of the object.


  supported_network (False, list, None)
    The registration of set of endpoint types that are supported by your service in the `networkType` environment attribute. This constrains the context-based restriction rules specific to the service such that they describe access restrictions on only this set of endpoints.


  enabled (False, bool, None)
    Whether the service is enabled or disabled for IAM.


  parent_ids (False, list, None)
    The list of parent IDs for product access management.


  resource_hierarchy_attribute (False, list, None)
    The resource hierarchy key-value pair for composite services.


  supported_attributes (False, list, None)
    The list of supported attributes.


  supported_roles (False, list, None)
    The list of roles that you can use to assign access.


  service_type (False, str, None)
    The type of the service.


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

