
ibm_is_instance -- Configure IBM Cloud 'ibm_is_instance' resource
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_instance' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.2
- Terraform v0.12.20



Parameters
----------

  gpu (False, list, None)
    None


  status (False, str, None)
    instance status


  resource_crn (False, str, None)
    The crn of the resource


  zone (False, str, None)
    (Required for new resource) Zone name


  profile (False, str, None)
    (Required for new resource) Profile info


  volumes (False, list, None)
    List of volumes


  resource_group (False, str, None)
    Instance resource group


  primary_network_interface (False, list, None)
    (Required for new resource) Primary Network interface info


  network_interfaces (False, list, None)
    None


  boot_volume (False, list, None)
    None


  name (False, str, None)
    (Required for new resource) Instance name


  vpc (False, str, None)
    (Required for new resource) VPC id


  tags (False, list, None)
    list of tags for the instance


  volume_attachments (False, list, None)
    None


  vcpu (False, list, None)
    None


  resource_name (False, str, None)
    The name of the resource


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  keys (False, list, None)
    (Required for new resource) SSH key Ids for the instance


  user_data (False, str, None)
    User data given for the instance


  image (False, str, None)
    (Required for new resource) image name


  memory (False, int, None)
    Instance memory


  resource_status (False, str, None)
    The status of the resource


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, any, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

