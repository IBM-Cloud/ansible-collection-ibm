
ibm_dns_domain_registration_info -- Retrieve IBM Cloud 'ibm_dns_domain_registration' resource
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_dns_domain_registration' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  name (True, str, None)
    The name of the domain registration


  name_servers (False, list, None)
    Custom name servers for the domain registration


  id (False, int, None)
    A domain registration record's internal identifier


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

