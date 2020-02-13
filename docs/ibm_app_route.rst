
ibm_app_route -- Configure IBM Cloud 'ibm_app_route' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_app_route' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  tags (False, list, None)
    None


  host (False, str, None)
    The host portion of the route. Required for shared-domains.


  space_guid (False, str, None)
    (Required for new resource) The guid of the associated space


  domain_guid (False, str, None)
    (Required for new resource) The guid of the associated domain


  port (False, int, None)
    The port of the route. Supported for domains of TCP router groups only.


  path (False, str, None)
    The path for a route as raw text.Paths must be between 2 and 128 characters.Paths must start with a forward slash '/'.Paths must not contain a '?'


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

