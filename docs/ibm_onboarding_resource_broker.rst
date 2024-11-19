
ibm_onboarding_resource_broker -- Configure IBM Cloud 'ibm_onboarding_resource_broker' resource
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_onboarding_resource_broker' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/onboarding_resource_broker

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  auth_password (False, str, None)
    The authentication password to reach the broker.


  auth_scheme (True, str, None)
    (Required for new resource) The supported authentication scheme for the broker.


  resource_group_crn (False, str, None)
    The cloud resource name of the resource group.


  allow_context_updates (False, bool, None)
    Whether the resource controller will call the broker for any context changes to the instance. Currently, the only context related change is an instance name update.


  catalog_type (False, str, None)
    To enable the provisioning of your broker, set this parameter value to `service`.


  broker_url (True, str, None)
    (Required for new resource) The URL associated with the broker application.


  auth_username (False, str, None)
    The authentication username to reach the broker.


  state_ (False, str, None)
    The state of the broker.


  env (False, str, None)
    The environment to fetch this object from.


  type (True, str, None)
    (Required for new resource) The type of the provisioning model.


  name (True, str, None)
    (Required for new resource) The name of the broker.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


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

