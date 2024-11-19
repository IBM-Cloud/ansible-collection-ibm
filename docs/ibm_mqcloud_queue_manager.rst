
ibm_mqcloud_queue_manager -- Configure IBM Cloud 'ibm_mqcloud_queue_manager' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_mqcloud_queue_manager' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/mqcloud_queue_manager

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  name (True, str, None)
    (Required for new resource) A queue manager name conforming to MQ restrictions.


  size (True, str, None)
    (Required for new resource) The queue manager sizes of deployment available.


  version (False, str, None)
    The MQ version of the queue manager.


  service_instance_guid (True, str, None)
    (Required for new resource) The GUID that uniquely identifies the MQ on Cloud service instance.


  display_name (False, str, None)
    A displayable name for the queue manager - limited only in length.


  location (True, str, None)
    (Required for new resource) The locations in which the queue manager could be deployed.


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

