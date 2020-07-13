
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

- IBM-Cloud terraform-provider-ibm v1.8.1
- Terraform v0.12.20



Parameters
----------

  boot_volume (False, list, None)
    None


  volumes (False, list, None)
    List of volumes


  memory (False, int, None)
    Instance memory


  status (False, str, None)
    instance status


  resource_name (False, str, None)
    The name of the resource


  resource_group_name (False, str, None)
    The resource group name in which resource is provisioned


  name (True, str, None)
    (Required for new resource) Instance name


  primary_network_interface (True, list, None)
    (Required for new resource) Primary Network interface info


  resource_crn (False, str, None)
    The crn of the resource


  vpc (True, str, None)
    (Required for new resource) VPC id


  network_interfaces (False, list, None)
    None


  user_data (False, str, None)
    User data given for the instance


  vcpu (False, list, None)
    None


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  resource_status (False, str, None)
    The status of the resource


  tags (False, list, None)
    list of tags for the instance


  profile (True, str, None)
    (Required for new resource) Profile info


  keys (True, list, None)
    (Required for new resource) SSH key Ids for the instance


  volume_attachments (False, list, None)
    None


  image (True, str, None)
    (Required for new resource) image name


  resource_group (False, str, None)
    Instance resource group


  zone (True, str, None)
    (Required for new resource) Zone name


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

