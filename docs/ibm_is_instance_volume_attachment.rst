
ibm_is_instance_volume_attachment -- Configure IBM Cloud 'ibm_is_instance_volume_attachment' resource
=====================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_instance_volume_attachment' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance_volume_attachment

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.51.0
- Terraform v0.12.20



Parameters
----------

  iops (False, int, None)
    The maximum I/O operations per second (IOPS) for the volume.


  snapshot (False, str, None)
    The snapshot of the volume to be attached


  instance (True, str, None)
    (Required for new resource) Instance id


  volume_name (False, str, None)
    The unique user-defined name for this volume


  capacity (False, int, None)
    The capacity of the volume in gigabytes. The specified minimum and maximum capacity values for creating or updating volumes may expand in the future.


  encryption_key (False, str, None)
    The CRN of the [Key Protect Root Key](https://cloud.ibm.com/docs/key-protect?topic=key-protect-getting-started-tutorial) or [Hyper Protect Crypto Service Root Key](https://cloud.ibm.com/docs/hs-crypto?topic=hs-crypto-get-started) for this resource.


  delete_volume_on_instance_delete (False, bool, None)
    If set to true, when deleting the instance the volume will also be deleted.


  delete_volume_on_attachment_delete (False, bool, True)
    If set to true, when deleting the attachment, the volume will also be deleted. Default value for this true.


  profile (False, str, None)
    The  globally unique name for the volume profile to use for this volume.


  name (False, str, None)
    The user-defined name for this volume attachment.


  volume (False, str, None)
    Instance id


  tags (False, list, None)
    UserTags for the volume instance


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

