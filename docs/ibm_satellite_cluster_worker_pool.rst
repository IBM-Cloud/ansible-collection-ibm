
ibm_satellite_cluster_worker_pool -- Configure IBM Cloud 'ibm_satellite_cluster_worker_pool' resource
=====================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_satellite_cluster_worker_pool' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/satellite_cluster_worker_pool

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  operating_system (False, str, None)
    Operating system of the worker pool. Options are REDHAT_7_64, REDHAT_8_64, or RHCOS.


  zones (False, list, None)
    Zone info for worker pool


  worker_pool_labels (False, dict, None)
    Labels on all the workers in the worker pool


  resource_group_id (False, str, None)
    ID of the resource group.


  flavor (False, str, None)
    The flavor defines the amount of virtual CPU, memory, and disk space that is set up in each worker node


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  disk_encryption (False, bool, None)
    Disk encryption for worker node


  isolation (False, str, None)
    None


  worker_count (False, int, None)
    Specify the desired number of workers per zone in this worker pool


  host_labels (False, list, None)
    Labels that describe a Satellite host


  name (True, str, None)
    (Required for new resource) The name for the worker pool


  cluster (True, str, None)
    (Required for new resource) The unique name for the new IBM Cloud Satellite cluster


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

