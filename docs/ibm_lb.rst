
ibm_lb -- Configure IBM Cloud 'ibm_lb' resource
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_lb' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.5.2
- Terraform v0.12.20



Parameters
----------

  ha_enabled (False, bool, False)
    true if High availability is enabled


  security_certificate_id (False, int, None)
    Security certificate ID


  dedicated (False, bool, False)
    Boolena value true if Load balncer is dedicated type


  ssl_enabled (False, bool, None)
    None


  datacenter (False, str, None)
    (Required for new resource) Datacenter name info


  ip_address (False, str, None)
    None


  subnet_id (False, int, None)
    None


  ssl_offload (False, bool, False)
    boolean value true if SSL offload is enabled


  tags (False, list, None)
    Tags associated with resource


  hostname (False, str, None)
    None


  connections (False, int, None)
    (Required for new resource) Connections value


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

