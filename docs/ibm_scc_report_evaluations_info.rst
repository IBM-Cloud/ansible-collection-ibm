
ibm_scc_report_evaluations_info -- Retrieve IBM Cloud 'ibm_scc_report_evaluations' resource
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_scc_report_evaluations' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/scc_report_evaluations

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  target_name (False, str, None)
    The name of the evaluation target.


  instance_id (True, str, None)
    The ID of the Security and Compliance Center instance.


  report_id (True, str, None)
    The ID of the scan that is associated with a report.


  component_id (False, str, None)
    The ID of component.


  target_id (False, str, None)
    The ID of the evaluation target.


  assessment_id (False, str, None)
    The ID of the assessment.


  status (False, str, None)
    The evaluation status value.


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

