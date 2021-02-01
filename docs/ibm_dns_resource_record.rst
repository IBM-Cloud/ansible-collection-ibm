
ibm_dns_resource_record -- Configure IBM Cloud 'ibm_dns_resource_record' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dns_resource_record' resource

This module does not support idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.17.0
- Terraform v0.12.20



Parameters
----------

  zone_id (True, str, None)
    (Required for new resource) Zone ID


  priority (False, int, 0)
    DNS server Priority


  weight (False, int, 0)
    DNS server weight


  protocol (False, str, None)
    Protocol


  ttl (False, int, 900)
    DNS record TTL


  port (False, int, None)
    DNS server Port


  instance_id (True, str, None)
    (Required for new resource) Instance ID


  type (True, str, None)
    (Required for new resource) DNS record Type


  name (True, str, None)
    (Required for new resource) DNS record name


  rdata (True, str, None)
    (Required for new resource) DNS record Data


  preference (False, int, 0)
    DNS maximum preference


  service (False, str, None)
    Service info


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

