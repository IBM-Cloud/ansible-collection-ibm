
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

- IBM-Cloud terraform-provider-ibm v1.2.1
- Terraform v0.12.20



Parameters
----------

  name (False, str, None)
    None


  secondary_address (False, list, None)
    None


  status (False, str, None)
    None


  type (False, str, None)
    None


  floating_ips (False, list, None)
    None


  security_group (False, str, None)
    (Required for new resource)


  network_interface (False, str, None)
    (Required for new resource)


  instance_network_interface (False, str, None)
    None


  port_speed (False, int, None)
    None


  primary_ipv4_address (False, str, None)
    None


  subnet (False, str, None)
    None


  security_groups (False, list, None)
    None


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, any, 2)
    IBM Cloud infrastructure generation.


  ibmcloud_api_key (False, any, None)
    (Required when generation = 2) The API Key used for authentification. This can also be provided via the environment variable 'IC_API_KEY'.


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environmental variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environmental variable 'IAAS_CLASSIC_API_KEY'.


  ibmcloud_region (False, any, us-south)
    Denotes which IBM Cloud region to connect to













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

