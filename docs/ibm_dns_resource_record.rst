
ibm_dns_resource_record -- Configure IBM Cloud 'ibm_dns_resource_record' resource
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dns_resource_record' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  instance_id (True, str, None)
    (Required for new resource) Instance ID


  name (True, str, None)
    (Required for new resource) DNS record name


  ttl (False, int, 900)
    DNS record TTL


  preference (False, int, 0)
    DNS maximum preference


  port (False, int, None)
    DNS server Port


  modified_on (False, str, None)
    Modification date


  priority (False, int, 0)
    DNS server Priority


  weight (False, int, 0)
    DNS server weight


  protocol (False, str, None)
    Protocol


  zone_id (True, str, None)
    (Required for new resource) Zone ID


  rdata (True, str, None)
    (Required for new resource) DNS record Data


  created_on (False, str, None)
    Creation Data


  resource_record_id (False, str, None)
    Resource record ID


  type (True, str, None)
    (Required for new resource) DNS record Type


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

