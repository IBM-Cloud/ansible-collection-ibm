
ibm_lb_vpx_vip -- Configure IBM Cloud 'ibm_lb_vpx_vip' resource
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lb_vpx_vip' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.3
- Terraform v0.12.20



Parameters
----------

  type (False, str, None)
    (Required for new resource) Type


  security_certificate_id (False, int, None)
    security certificate ID


  persistence (False, str, None)
    Persistance value


  source_port (False, int, None)
    (Required for new resource) Source Port number


  name (False, str, None)
    (Required for new resource) Name


  virtual_ip_address (False, str, None)
    (Required for new resource) Virtual IP address


  tags (False, list, None)
    List of tags


  nad_controller_id (False, int, None)
    (Required for new resource) NAD controller ID


  load_balancing_method (False, str, None)
    (Required for new resource) Load balancing method


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

