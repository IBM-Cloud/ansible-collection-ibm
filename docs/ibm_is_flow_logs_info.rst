
ibm_is_flow_logs_info -- Retrieve IBM Cloud 'ibm_is_flow_logs' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_flow_logs' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_flow_logs

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  vpc_name (False, str, None)
    The vpc name this flow log is in


  vpc_crn (False, str, None)
    The vpc CRN this flow log is in


  name (False, str, None)
    The name of the flow log


  target (False, str, None)
    The target id of the flow log


  target_resource_type (False, str, None)
    The target resource type of the flow log


  resource_group (False, str, None)
    The unique identifier of the resource group this flow log belongs to


  vpc (False, str, None)
    The vpc ID this flow log is in


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

