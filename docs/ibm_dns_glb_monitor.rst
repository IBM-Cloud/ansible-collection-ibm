
ibm_dns_glb_monitor -- Configure IBM Cloud 'ibm_dns_glb_monitor' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dns_glb_monitor' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/dns_glb_monitor

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  description (False, str, None)
    Descriptive text of the load balancer monitor


  port (False, int, None)
    Port number to connect to for the health check


  retries (False, int, 1)
    The number of retries to attempt in case of a timeout before marking the origin as unhealthy


  timeout (False, int, 5)
    The timeout (in seconds) before marking the health check as failed


  path (False, str, None)
    The endpoint path to health check against


  expected_codes (False, str, None)
    The expected HTTP response code or code range of the health check. This parameter is only valid for HTTP and HTTPS


  allow_insecure (False, bool, None)
    Do not validate the certificate when monitor use HTTPS. This parameter is currently only valid for HTTPS monitors.


  instance_id (True, str, None)
    (Required for new resource) Instance Id


  name (True, str, None)
    (Required for new resource) The unique identifier of a service instance.


  type (False, str, HTTP)
    The protocol to use for the health check


  interval (False, int, 60)
    The interval between each health check


  method (False, str, None)
    The method to use for the health check


  headers (False, list, None)
    The HTTP request headers to send in the health check


  expected_body (False, str, None)
    A case-insensitive sub-string to look for in the response body


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

