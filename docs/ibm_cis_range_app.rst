
ibm_cis_range_app -- Configure IBM Cloud 'ibm_cis_range_app' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_cis_range_app' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cis_range_app

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.38.2
- Terraform v0.12.20



Parameters
----------

  traffic_type (False, str, direct)
    Configure how traffic is handled at the edge.


  cis_id (True, str, None)
    (Required for new resource) CIS Intance CRN


  domain_id (True, str, None)
    (Required for new resource) CIS Domain ID


  protocol (True, str, None)
    (Required for new resource) Defines the protocol and port for this application


  edge_ips_connectivity (False, str, all)
    Specifies the IP version.


  ip_firewall (False, bool, None)
    Enables the IP Firewall for this application. Only available for TCP applications.


  dns_type (True, str, None)
    (Required for new resource) Type of the DNS record for this application


  origin_direct (False, list, None)
    IP address and port of the origin for this Range application.


  origin_dns (False, str, None)
    DNS record pointing to the origin for this Range application.


  dns (True, str, None)
    (Required for new resource) Name of the DNS record for this application


  proxy_protocol (False, str, None)
    Allows for the true client IP to be passed to the service.


  edge_ips_type (False, str, dynamic)
    The type of edge IP configuration.


  origin_port (False, int, None)
    Port at the origin that listens to traffic


  tls (False, str, False)
    Configure if and how TLS connections are terminated at the edge.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

