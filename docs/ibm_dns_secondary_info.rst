
ibm_dns_secondary_info -- Retrieve IBM Cloud 'ibm_dns_secondary' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_dns_secondary' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  zone_name (True, str, None)
    The name of the secondary


  master_ip_address (False, str, None)
    None


  transfer_frequency (False, int, None)
    None


  status_id (False, int, None)
    None


  status_text (False, str, None)
    None


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

