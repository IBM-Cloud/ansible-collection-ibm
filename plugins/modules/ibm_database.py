#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_database
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/database

short_description: Configure IBM Cloud 'ibm_database' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_database' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.46.0
    - Terraform v0.12.20

options:
    plan_validation:
        description:
            - For elasticsearch and postgres perform database parameter validation during the plan phase. Otherwise, database parameter validation happens in apply phase.
        required: False
        type: bool
        default: True
    service:
        description:
            - (Required for new resource) The name of the Cloud Internet database service
        required: True
        type: str
    users:
        description:
            - None
        required: False
        type: list
        elements: dict
    auto_scaling:
        description:
            - ICD Auto Scaling
        required: False
        type: list
        elements: dict
    adminpassword:
        description:
            - The admin user password for the instance
        required: False
        type: str
    backup_encryption_key_crn:
        description:
            - The Backup Encryption Key CRN
        required: False
        type: str
    point_in_time_recovery_time:
        description:
            - The point in time recovery time stamp of the deployed instance
        required: False
        type: str
    name:
        description:
            - (Required for new resource) Resource instance name for example, my Database instance
        required: True
        type: str
    resource_group_id:
        description:
            - The id of the resource group in which the Database instance is present
        required: False
        type: str
    service_endpoints:
        description:
            - Types of the service endpoints. Possible values are 'public', 'private', 'public-and-private'.
        required: False
        type: str
        default: public
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    point_in_time_recovery_deployment_id:
        description:
            - The CRN of source instance
        required: False
        type: str
    version:
        description:
            - The database version to provision if specified
        required: False
        type: str
    whitelist:
        description:
            - None
        required: False
        type: list
        elements: dict
    group:
        description:
            - None
        required: False
        type: list
        elements: dict
    location:
        description:
            - (Required for new resource) The location or the region in which Database instance exists
        required: True
        type: str
    remote_leader_id:
        description:
            - The CRN of leader database
        required: False
        type: str
    key_protect_instance:
        description:
            - The CRN of Key protect instance
        required: False
        type: str
    key_protect_key:
        description:
            - The CRN of Key protect key
        required: False
        type: str
    plan:
        description:
            - (Required for new resource) The plan type of the Database instance
        required: True
        type: str
    configuration:
        description:
            - The configuration in JSON format
        required: False
        type: str
    backup_id:
        description:
            - The CRN of backup source database
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
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
    ('service', 'str'),
    ('name', 'str'),
    ('location', 'str'),
    ('plan', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'plan_validation',
    'service',
    'users',
    'auto_scaling',
    'adminpassword',
    'backup_encryption_key_crn',
    'point_in_time_recovery_time',
    'name',
    'resource_group_id',
    'service_endpoints',
    'tags',
    'point_in_time_recovery_deployment_id',
    'version',
    'whitelist',
    'group',
    'location',
    'remote_leader_id',
    'key_protect_instance',
    'key_protect_key',
    'plan',
    'configuration',
    'backup_id',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'service',
    'name',
    'location',
    'tags',
    'resource_group_id',
]

TL_CONFLICTS_MAP = {
    'group': ['members_memory_allocation_mb', 'members_disk_allocation_mb', 'members_cpu_allocation_count', 'node_memory_allocation_mb', 'node_disk_allocation_mb', 'node_cpu_allocation_count', 'node_count'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    plan_validation=dict(
        required=False,
        type='bool'),
    service=dict(
        required=False,
        type='str'),
    users=dict(
        required=False,
        elements='',
        type='list'),
    auto_scaling=dict(
        required=False,
        elements='',
        type='list'),
    adminpassword=dict(
        required=False,
        type='str'),
    backup_encryption_key_crn=dict(
        required=False,
        type='str'),
    point_in_time_recovery_time=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    service_endpoints=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    point_in_time_recovery_deployment_id=dict(
        required=False,
        type='str'),
    version=dict(
        required=False,
        type='str'),
    whitelist=dict(
        required=False,
        elements='',
        type='list'),
    group=dict(
        required=False,
        elements='',
        type='list'),
    location=dict(
        required=False,
        type='str'),
    remote_leader_id=dict(
        required=False,
        type='str'),
    key_protect_instance=dict(
        required=False,
        type='str'),
    key_protect_key=dict(
        required=False,
        type='str'),
    plan=dict(
        required=False,
        type='str'),
    configuration=dict(
        required=False,
        type='str'),
    backup_id=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
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

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    conflicts = {}
    if len(TL_CONFLICTS_MAP) != 0:
        for arg in TL_CONFLICTS_MAP:
            if module.params[arg]:
                for conflict in TL_CONFLICTS_MAP[arg]:
                    try:
                        if module.params[conflict]:
                            conflicts[arg] = conflict
                    except KeyError:
                        pass
    if len(conflicts):
        module.fail_json(msg=("conflicts exist: {}".format(conflicts)))

    result_ds = ibmcloud_terraform(
        resource_type='ibm_database',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.46.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_database',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.46.0',
            tl_required_params=TL_REQUIRED_PARAMETERS,
            tl_all_params=TL_ALL_PARAMETERS)
        if result['rc'] > 0:
            module.fail_json(
                msg=Terraform.parse_stderr(result['stderr']), **result)

        module.exit_json(**result)
    else:
        module.exit_json(**result_ds)


def main():
    run_module()


if __name__ == '__main__':
    main()
