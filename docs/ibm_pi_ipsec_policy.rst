
ibm_pi_ipsec_policy -- Configure IBM Cloud 'ibm_pi_ipsec_policy' resource
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_ipsec_policy' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/pi_ipsec_policy

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  pi_cloud_instance_id (True, str, None)
    (Required for new resource) PI cloud instance ID


  pi_policy_name (True, str, None)
    (Required for new resource) Name of the IPSec Policy


  pi_policy_dh_group (True, int, None)
    (Required for new resource) DH group of the IPSec Policy


  pi_policy_encryption (True, str, None)
    (Required for new resource) Encryption of the IPSec Policy


  pi_policy_key_lifetime (True, int, None)
    (Required for new resource) Policy key lifetime


  pi_policy_pfs (True, bool, None)
    (Required for new resource) Perfect Forward Secrecy


  pi_policy_authentication (False, str, none)
    Authentication for the IPSec Policy


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  zone (False, str, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environment variable 'IC_ZONE'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

