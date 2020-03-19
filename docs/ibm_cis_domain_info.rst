
ibm_cis_domain_info -- Retrieve IBM Cloud 'ibm_cis_domain' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_cis_domain' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.5
- Terraform v0.12.20



Parameters
----------

  status (False, str, None)
    None


  name_servers (False, list, None)
    None


  original_name_servers (False, list, None)
    None


  cis_id (True, str, None)
    CIS object id


  domain (True, str, None)
    CISzone - Domain


  paused (False, bool, None)
    None


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

