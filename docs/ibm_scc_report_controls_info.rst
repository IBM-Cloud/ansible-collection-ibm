
ibm_scc_report_controls_info -- Retrieve IBM Cloud 'ibm_scc_report_controls' resource
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_scc_report_controls' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/scc_report_controls

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  sort (False, str, None)
    This field sorts controls by using a valid sort field. To learn more, see [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).


  control_id (False, str, None)
    The ID of the control.


  instance_id (True, str, None)
    The ID of the Security and Compliance Center instance.


  report_id (True, str, None)
    The ID of the scan that is associated with a report.


  control_category (False, str, None)
    A control category value.


  status (False, str, None)
    The compliance status value.


  control_description (False, str, None)
    The description of the control.


  control_name (False, str, None)
    The name of the control.


  iaas_classic_username (False, any, None)
    The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

