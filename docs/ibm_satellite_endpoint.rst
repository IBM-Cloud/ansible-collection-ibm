
ibm_satellite_endpoint -- Configure IBM Cloud 'ibm_satellite_endpoint' resource
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_satellite_endpoint' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/satellite_endpoint

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  certs (False, list, None)
    The certs.


  location (True, str, None)
    (Required for new resource) The Location ID.


  connection_type (True, str, None)
    (Required for new resource) The type of the endpoint.


  server_host (True, str, None)
    (Required for new resource) The host name or IP address of the server endpoint. For 'http-tunnel' protocol, server_host can start with '*.' , which means a wildcard to it's sub domains. Such as '*.example.com' can accept request to 'api.example.com' and 'www.example.com'.


  server_port (True, int, None)
    (Required for new resource) The port number of the server endpoint. For 'http-tunnel' protocol, server_port can be 0, which means any port. Such as 0 is good for 80 (http) and 443 (https).


  timeout (False, int, None)
    The inactivity timeout in the Endpoint side.


  sni (False, str, None)
    The server name indicator (SNI) which used to connect to the server endpoint. Only useful if server side requires SNI.


  client_mutual_auth (False, bool, False)
    Whether enable mutual auth in the client application side, when client_protocol is 'tls' or 'https', this field is required.


  server_mutual_auth (False, bool, False)
    Whether enable mutual auth in the server application side, when client_protocol is 'tls', this field is required.


  display_name (True, str, None)
    (Required for new resource) The display name of the endpoint. Endpoint names must start with a letter and end with an alphanumeric character, can contain letters, numbers, and hyphen (-), and must be 63 characters or fewer.


  client_protocol (True, str, None)
    (Required for new resource) The protocol in the client application side.


  created_by (False, str, None)
    The service or person who created the endpoint. Must be 1000 characters or fewer.


  server_protocol (False, str, None)
    The protocol in the server application side. This parameter will change to default value if it is omitted even when using PATCH API. If client_protocol is 'udp', server_protocol must be 'udp'. If client_protocol is 'tcp'/'http', server_protocol could be 'tcp'/'tls' and default to 'tcp'. If client_protocol is 'tls'/'https', server_protocol could be 'tcp'/'tls' and default to 'tls'. If client_protocol is 'http-tunnel', server_protocol must be 'tcp'.


  reject_unauth (False, bool, False)
    Whether reject any connection to the server application which is not authorized with the list of supplied CAs in the fields certs.server_cert.


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

