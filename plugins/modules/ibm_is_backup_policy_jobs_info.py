#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_backup_policy_jobs_info
for_more_info: refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_backup_policy_jobs

short_description: Retrieve IBM Cloud 'ibm_is_backup_policy_jobs' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_is_backup_policy_jobs' resource
requirements:
    - IBM-Cloud terraform-provider-ibm v1.51.0
    - Terraform v0.12.20

options:
    source_id:
        description:
            - Filters the collection to backup policy jobs with a source with the specified identifier
        required: False
        type: str
    target_snapshots_id:
        description:
            - Filters the collection to resources with the target snapshot with the specified identifier
        required: False
        type: list
        elements: str
    target_snapshots_crn:
        description:
            - Filters the collection to backup policy jobs with the target snapshot with the specified CRN
        required: False
        type: list
        elements: str
    backup_policy_plan_id:
        description:
            - Filters the collection to backup policy jobs with the backup plan with the specified identifier.
        required: False
        type: str
    status:
        description:
            - Filters the collection to backup policy jobs with the specified status
        required: False
        type: str
    backup_policy_id:
        description:
            - The backup policy identifier.
        required: True
        type: str
    generation:
        description:
            - The generation of Virtual Private Cloud infrastructure
              that you want to use. Supported values are 1 for VPC
              generation 1, and 2 for VPC generation 2 infrastructure.
              If this value is not specified, 2 is used by default. This
              can also be provided via the environment variable
              'IC_GENERATION'.
        default: 2
        required: False
        type: int
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
        type: str
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('backup_policy_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'source_id',
    'target_snapshots_id',
    'target_snapshots_crn',
    'backup_policy_plan_id',
    'status',
    'backup_policy_id',
]


TL_CONFLICTS_MAP = {
    'target_snapshots_id': ['target_snapshots_crn'],
    'target_snapshots_crn': ['target_snapshots_id'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    source_id=dict(
        required=False,
        type='str'),
    target_snapshots_id=dict(
        required=False,
        elements='',
        type='list'),
    target_snapshots_crn=dict(
        required=False,
        elements='',
        type='list'),
    backup_policy_plan_id=dict(
        required=False,
        type='str'),
    status=dict(
        required=False,
        type='str'),
    backup_policy_id=dict(
        required=True,
        type='str'),
    generation=dict(
        type='int',
        required=False,
        fallback=(env_fallback, ['IC_GENERATION']),
        default=2),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # VPC required arguments checks
    if module.params['generation'] == 1:
        missing_args = []
        if module.params['iaas_classic_username'] is None:
            missing_args.append('iaas_classic_username')
        if module.params['iaas_classic_api_key'] is None:
            missing_args.append('iaas_classic_api_key')
        if missing_args:
            module.fail_json(msg=(
                "VPC generation=1 missing required arguments: " +
                ", ".join(missing_args)))
    elif module.params['generation'] == 2:
        if module.params['ibmcloud_api_key'] is None:
            module.fail_json(
                msg=("VPC generation=2 missing required argument: "
                     "ibmcloud_api_key"))

    result = ibmcloud_terraform(
        resource_type='ibm_is_backup_policy_jobs',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.51.0',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
