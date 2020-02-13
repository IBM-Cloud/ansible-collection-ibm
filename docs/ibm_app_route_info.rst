
ibm_app_route_info -- Retrieve IBM Cloud 'ibm_app_route' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_app_route' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  path (False, str, None)
    The path of the route


  port (False, str, None)
    The port of the route


  space_guid (True, str, None)
    The guid of the space


  domain_guid (True, str, None)
    The guid of the domain


  host (False, str, None)
    The host of the route


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

