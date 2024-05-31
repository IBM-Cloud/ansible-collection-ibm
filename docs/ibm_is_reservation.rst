
ibm_is_reservation -- Configure IBM Cloud 'ibm_is_reservation' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_reservation' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_reservation

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.65.1
- Terraform v1.5.5



Parameters
----------

  resource_group (False, list, None)
    The committed use configuration to use for this reservation


  zone (True, str, None)
    (Required for new resource) The globally unique name for this zone.


  affinity_policy (False, str, None)
    The affinity policy to use for this reservation


  name (False, str, None)
    Reservation name


  committed_use (True, list, None)
    (Required for new resource) The committed use configuration to use for this reservation


  profile (True, list, None)
    (Required for new resource) The profile to use for this reservation.


  capacity (True, list, None)
    (Required for new resource) The capacity reservation configuration to use


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

