
ibm_is_instance_info -- Retrieve IBM Cloud 'ibm_is_instance' resource
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_instance' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  resource_name (False, str, None)
    The name of the resource


  resource_crn (False, str, None)
    The crn of the resource


  tags (False, list, None)
    list of tags for the instance


  boot_volume (False, list, None)
    Instance Boot Volume


  image (False, str, None)
    Instance Image


  status (False, str, None)
    instance status


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  resource_status (False, str, None)
    The status of the resource


  passphrase (False, str, None)
    Passphrase for Instance Private Key file


  zone (False, str, None)
    Zone name


  network_interfaces (False, list, None)
    Instance Network interface info


  resource_group (False, str, None)
    Instance resource group


  memory (False, int, None)
    Instance memory


  name (True, str, None)
    Instance name


  password (False, str, None)
    password for Windows Instance


  keys (False, list, None)
    Instance keys


  vpc (False, str, None)
    VPC id


  profile (False, str, None)
    Profile info


  primary_network_interface (False, list, None)
    Primary Network interface info


  private_key (False, str, None)
    Instance Private Key file


  volume_attachments (False, list, None)
    Instance Volume Attachments


  volumes (False, list, None)
    List of volumes


  vcpu (False, list, None)
    Instance vCPU


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

