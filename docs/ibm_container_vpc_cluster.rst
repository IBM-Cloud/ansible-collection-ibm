
ibm_container_vpc_cluster -- Configure IBM Cloud 'ibm_container_vpc_cluster' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_container_vpc_cluster' resource

This module supports idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.20.0
- Terraform v0.12.20



Parameters
----------

  tags (False, list, None)
    List of tags for the resources


  force_delete_storage (False, bool, False)
    Force the removal of a cluster and its persistent storage. Deleted data cannot be recovered


  disable_public_service_endpoint (False, bool, False)
    Boolean value true if Public service endpoint to be disabled


  worker_count (False, int, 1)
    Number of worker nodes in the cluster


  worker_labels (False, dict, None)
    Labels for default worker pool


  flavor (True, str, None)
    (Required for new resource) Cluster nodes flavour


  kms_config (False, list, None)
    Enables KMS on a given cluster


  wait_till (False, str, IngressReady)
    wait_till can be configured for Master Ready, One worker Ready or Ingress Ready


  vpc_id (True, str, None)
    (Required for new resource) The vpc id where the cluster is


  update_all_workers (False, bool, False)
    Updates all the woker nodes if sets to true


  zones (True, list, None)
    (Required for new resource) Zone info


  entitlement (False, str, None)
    Entitlement option reduces additional OCP Licence cost in Openshift Clusters


  patch_version (False, str, None)
    Kubernetes patch version


  service_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for services


  name (True, str, None)
    (Required for new resource) The cluster name


  kube_version (False, str, None)
    Kubernetes version


  resource_group_id (False, str, None)
    ID of the resource group.


  wait_for_worker_update (False, bool, True)
    Wait for worker node to update during kube version update.


  cos_instance_crn (False, str, None)
    A standard cloud object storage instance CRN to back up the internal registry in your OpenShift on VPC Gen 2 cluster


  pod_subnet (False, str, None)
    Custom subnet CIDR to provide private IP addresses for pods


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

