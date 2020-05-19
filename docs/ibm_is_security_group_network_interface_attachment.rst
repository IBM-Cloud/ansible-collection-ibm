
ibm_is_security_group_network_interface_attachment -- Configure IBM Cloud 'ibm_is_security_group_network_interface_attachment' resource
=======================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_security_group_network_interface_attachment' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.3
- Terraform v0.12.20



Parameters
----------

  secondary_address (False, list, None)
    security group network interface attachment secondary address


  subnet (False, str, None)
    security group network interface attachment subnet


  security_groups (False, list, None)
    None


  name (False, str, None)
    security group network interface attachment name


  instance_network_interface (False, str, None)
    security group network interface attachment network interface ID


  port_speed (False, int, None)
    security group network interface attachment port speed


  primary_ipv4_address (False, str, None)
    security group network interface attachment Primary IPV4 address


  floating_ips (False, list, None)
    None


  security_group (False, str, None)
    (Required for new resource) security group network interface attachment group ID


  network_interface (False, str, None)
    (Required for new resource) security group network interface attachment NIC ID


  status (False, str, None)
    security group network interface attachment status


  type (False, str, None)
    security group network interface attachment type


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

