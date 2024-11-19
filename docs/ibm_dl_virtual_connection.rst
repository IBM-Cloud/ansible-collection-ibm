
ibm_dl_virtual_connection -- Configure IBM Cloud 'ibm_dl_virtual_connection' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_dl_virtual_connection' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/dl_virtual_connection

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  type (True, str, None)
    (Required for new resource) The type of virtual connection.Allowable values (classic,vpc)


  network_id (False, str, None)
    Unique identifier of the target network. For type=vpc virtual connections this is the CRN of the target VPC. This field does not apply to type=classic connections.


  gateway (True, str, None)
    (Required for new resource) The Direct Link gateway identifier


  name (True, str, None)
    (Required for new resource) The user-defined name for this virtual connection. Virtualconnection names are unique within a gateway. This is the name of thevirtual connection itself, the network being connected may have its ownname attribute


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

