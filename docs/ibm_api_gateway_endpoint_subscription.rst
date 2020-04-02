
ibm_api_gateway_endpoint_subscription -- Configure IBM Cloud 'ibm_api_gateway_endpoint_subscription' resource
=============================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_api_gateway_endpoint_subscription' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.3.0
- Terraform v0.12.20



Parameters
----------

  artifact_id (False, str, None)
    (Required for new resource) Endpoint ID


  client_id (False, str, None)
    (Required for new resource) Subscription Id


  name (False, str, None)
    (Required for new resource) Subscription name


  type (False, str, None)
    (Required for new resource) Subscription type. Allowable values are external, bluemix


  client_secret (False, str, None)
    Client Sercret of a Subscription


  secret_provided (False, bool, None)
    Indicates if client secret is provided to subscription or not


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

