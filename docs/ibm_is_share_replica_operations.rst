
ibm_is_share_replica_operations -- Configure IBM Cloud 'ibm_is_share_replica_operations' resource
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_share_replica_operations' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_share_replica_operations

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  split_share (False, bool, False)
    If set to true the replication relationship between source share and replica will be removed.


  share_replica (True, str, None)
    (Required for new resource) The file share identifier.


  fallback_policy (False, str, fail)
    The action to take if the failover request is accepted but cannot be performed or times out


  timeout (False, int, None)
    The failover timeout in seconds


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

