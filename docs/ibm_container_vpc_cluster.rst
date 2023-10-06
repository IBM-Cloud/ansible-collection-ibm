
ibm_container_vpc_cluster -- Configure IBM Cloud 'ibm_container_vpc_cluster' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_vpc_cluster' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_vpc_cluster

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.51.0
- Terraform v0.12.20



Parameters
----------

  kms_instance_id (False, str, None)
    Instance ID for boot volume encryption


  flavor (True, str, None)
    (Required for new resource) Cluster nodes flavour


  wait_for_worker_update (False, bool, True)
    Wait for worker node to update during kube version update.


  wait_till (False, str, IngressReady)
    wait_till can be configured for Master Ready, One worker Ready or Ingress Ready or Normal


  operating_system (False, str, None)
    The operating system of the workers in the default worker pool.


  crk (False, str, None)
    Root Key ID for boot volume encryption


  kms_config (False, list, None)
    Enables KMS on a given cluster


  worker_labels (False, dict, None)
    Labels for default worker pool


  taints (False, list, None)
    WorkerPool Taints


  retry_patch_version (False, int, None)
    Argument which helps to retry the patch version updates on worker nodes. Increment the value to retry the patch updates if the previous apply fails


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  host_pool_id (False, str, None)
    The ID of the cluster's associated host pool


  update_all_workers (False, bool, False)
    Updates all the woker nodes if sets to true


  pod_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for pods


  cos_instance_crn (False, str, None)
    A standard cloud object storage instance CRN to back up the internal registry in your OpenShift on VPC Gen 2 cluster


  resource_group_id (False, str, None)
    ID of the resource group.


  name (True, str, None)
    (Required for new resource) The cluster name


  service_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for services


  worker_count (False, int, 1)
    Number of worker nodes in the cluster


  kube_version (False, str, None)
    Kubernetes version


  secondary_storage (False, str, None)
    The secondary storage option for the default worker pool.


  disable_public_service_endpoint (False, bool, False)
    Boolean value true if Public service endpoint to be disabled


  tags (False, list, None)
    List of tags for the resources


  force_delete_storage (False, bool, False)
    Force the removal of a cluster and its persistent storage. Deleted data cannot be recovered


  kms_account_id (False, str, None)
    Account ID of kms instance holder - if not provided, defaults to the account in use


  vpc_id (True, str, None)
    (Required for new resource) The vpc id where the cluster is


  zones (True, list, None)
    (Required for new resource) Zone info


  patch_version (False, str, None)
    Kubernetes patch version


  image_security_enforcement (False, bool, False)
    Set true to enable image security enforcement policies


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

