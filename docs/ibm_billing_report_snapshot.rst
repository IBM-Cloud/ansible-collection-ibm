
ibm_billing_report_snapshot -- Configure IBM Cloud 'ibm_billing_report_snapshot' resource
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_billing_report_snapshot' resource

This module does not support idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/billing_report_snapshot

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.71.2
- Terraform v1.5.5



Parameters
----------

  interval (True, str, None)
    (Required for new resource) Frequency of taking the snapshot of the billing reports.


  versioning (False, str, new)
    A new version of report is created or the existing report version is overwritten with every update.


  report_types (False, list, None)
    The type of billing reports to take snapshot of. Possible values are [account_summary, enterprise_summary, account_resource_instance_usage].


  cos_bucket (True, str, None)
    (Required for new resource) The name of the COS bucket to store the snapshot of the billing reports.


  cos_reports_folder (False, str, IBMCloud-Billing-Reports)
    The billing reports root folder to store the billing reports snapshots. Defaults to "IBMCloud-Billing-Reports".


  cos_location (True, str, None)
    (Required for new resource) Region of the COS instance.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


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

