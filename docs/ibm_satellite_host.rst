
ibm_satellite_host -- Configure IBM Cloud 'ibm_satellite_host' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_satellite_host' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/satellite_host

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  host_id (True, str, None)
    (Required for new resource) The specific host ID to assign to a Satellite location or cluster


  zone (False, str, None)
    The zone within the cluster to assign the host to


  host_provider (False, str, None)
    Host Provider


  location (True, str, None)
    (Required for new resource) The name or ID of the Satellite location


  cluster (False, str, None)
    The name or ID of a Satellite location or cluster to assign the host to


  labels (False, list, None)
    List of labels for the host


  worker_pool (False, str, None)
    The name or ID of the worker pool within the cluster to assign the host to


  wait_till (False, str, None)
    Wait until location is normal


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

