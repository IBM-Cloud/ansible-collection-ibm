
ibm_dns_domain_registration_nameservers -- Configure IBM Cloud 'ibm_dns_domain_registration_nameservers' resource
=================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dns_domain_registration_nameservers' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  dns_registration_id (False, str, None)
    (Required for new resource)


  name_servers (False, list, None)
    (Required for new resource) Custom name servers for the domain registration


  original_name_servers (False, list, None)
    Save of name servers prior to update


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

