
ibm_is_volume -- Configure IBM Cloud 'ibm_is_volume' resource
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_volume' resource

This module supports idempotency



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.17.0
- Terraform v0.12.20



Parameters
----------

  iops (False, int, None)
    IOPS value for the Volume


  tags (False, list, None)
    Tags for the volume instance


  zone (True, str, None)
    (Required for new resource) Zone name


  capacity (False, int, 100)
    Vloume capacity value


  name (True, str, None)
    (Required for new resource) Volume name


  profile (True, str, None)
    (Required for new resource) Vloume profile name


  encryption_key (False, str, None)
    Volume encryption key info


  resource_group (False, str, None)
    Resource group name


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

