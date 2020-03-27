
ibm_cis_info -- Retrieve IBM Cloud 'ibm_cis' resource
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_cis' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.6
- Terraform v0.12.20



Parameters
----------

  plan (False, str, None)
    The plan type of the cis instance


  status (False, dict, None)
    The resource instance status


  resource_name (False, str, None)
    The name of the resource


  resource_crn (False, str, None)
    The crn of the resource


  resource_status (False, str, None)
    The status of the resource


  name (True, str, None)
    Resource instance name for example, my cis instance


  location (False, str, None)
    The location or the environment in which cis instance exists


  service (False, str, None)
    The name of the Cloud Internet Services offering, 'internet-svcs'


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about the resource


  resource_group_id (False, str, None)
    The id of the resource group in which the cis instance is present


  guid (False, str, None)
    Unique identifier of resource instance


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to


  ibmcloud_zone (False, any, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environmental variable 'IC_ZONE'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

