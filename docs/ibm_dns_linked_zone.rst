
ibm_dns_linked_zone -- Configure IBM Cloud 'ibm_dns_linked_zone' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dns_linked_zone' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/dns_linked_zone

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  linked_to (False, str, None)
    The zone that is linked to the DNS Linked zone


  name (True, str, None)
    (Required for new resource) The name of the DNS Linked zone.


  description (False, str, None)
    Descriptive text of the DNS Linked zone


  owner_zone_id (True, str, None)
    (Required for new resource) The unique identifier of the owner DNS zone


  label (False, str, None)
    The label of the DNS Linked zone


  approval_required_before (False, str, None)
    DNS Linked Approval required before


  instance_id (True, str, None)
    (Required for new resource) The unique identifier of a DNS Linked zone.


  owner_instance_id (True, str, None)
    (Required for new resource) The unique identifier of the owner DNS instance


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

