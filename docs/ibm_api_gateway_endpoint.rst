
ibm_api_gateway_endpoint -- Configure IBM Cloud 'ibm_api_gateway_endpoint' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_api_gateway_endpoint' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.3.0
- Terraform v0.12.20



Parameters
----------

  service_instance_crn (False, str, None)
    (Required for new resource) Api Gateway Service Instance Crn


  open_api_doc_name (False, str, None)
    (Required for new resource) Json File path


  routes (False, list, None)
    Invokable routes for an endpoint


  managed (False, bool, False)
    Managed indicates if endpoint is online or offline.


  provider_id (False, str, user-defined)
    Provider ID of an endpoint allowable values user-defined and whisk


  name (False, str, None)
    (Required for new resource) Endpoint name


  shared (False, bool, None)
    The Shared status of an endpoint


  base_path (False, str, None)
    Base path of an endpoint


  endpoint_id (False, str, None)
    Endpoint ID


  type (False, str, unshare)
    Action type of Endpoint ALoowable values are share, unshare, manage, unmanage


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

