
ibm_compute_ssh_key_info -- Retrieve IBM Cloud 'ibm_compute_ssh_key' resource
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_compute_ssh_key' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  fingerprint (False, str, None)
    A sequence of bytes to authenticate or lookup a longer ssh key


  notes (False, str, None)
    A small note about a ssh key to use at your discretion


  most_recent (False, bool, False)
    If true and multiple entries are found, the most recently created key is used. If false, an error is returned


  label (True, str, None)
    The label associated with the ssh key


  public_key (False, str, None)
    The public ssh key


  ibmcloud_api_key (True, any, None)
    The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

