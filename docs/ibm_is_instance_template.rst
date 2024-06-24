
ibm_is_instance_template -- Configure IBM Cloud 'ibm_is_instance_template' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_instance_template' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_instance_template

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.66.0
- Terraform v1.5.5



Parameters
----------

  default_trusted_profile_target (False, str, None)
    The unique identifier or CRN of the default IAM trusted profile to use for this virtual server instance.


  network_attachments (False, list, None)
    The network attachments for this virtual server instance, including the primary network attachment.


  boot_volume (False, list, None)
    None


  profile (True, str, None)
    (Required for new resource) Profile info


  volume_attachments (False, list, None)
    None


  primary_network_interface (False, list, None)
    Primary Network interface info


  default_trusted_profile_auto_link (False, bool, None)
    If set to `true`, the system will create a link to the specified `target` trusted profile during instance creation. Regardless of whether a link is created by the system or manually using the IAM Identity service, it will be automatically deleted when the instance is deleted.


  total_volume_bandwidth (False, int, None)
    The amount of bandwidth (in megabits per second) allocated exclusively to instance storage volumes


  user_data (False, str, None)
    User data given for the instance


  name (False, str, None)
    Instance Template name


  metadata_service (False, list, None)
    The metadata service configuration


  keys (True, list, None)
    (Required for new resource) SSH key Ids for the instance template


  placement_group (False, str, None)
    Unique Identifier of the Placement Group for restricting the placement of the instance


  network_interfaces (False, list, None)
    None


  availability_policy_host_failure (False, str, None)
    The availability policy to use for this virtual server instance


  dedicated_host_group (False, str, None)
    Unique Identifier of the Dedicated Host Group where the instance will be placed


  catalog_offering (False, list, None)
    The catalog offering or offering version to use when provisioning this virtual server instance template. If an offering is specified, the latest version of that offering will be used. The specified offering or offering version may be in a different account in the same enterprise, subject to IAM policies.


  image (False, str, None)
    image name


  reservation_affinity (False, list, None)
    None


  vpc (True, str, None)
    (Required for new resource) VPC id


  zone (True, str, None)
    (Required for new resource) Zone name


  resource_group (False, str, None)
    Instance template resource group


  dedicated_host (False, str, None)
    Unique Identifier of the Dedicated Host where the instance will be placed


  primary_network_attachment (False, list, None)
    The primary network attachment for this virtual server instance.


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

