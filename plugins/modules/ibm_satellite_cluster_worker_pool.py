#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_satellite_cluster_worker_pool
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/satellite_cluster_worker_pool

short_description: Configure IBM Cloud 'ibm_satellite_cluster_worker_pool' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_satellite_cluster_worker_pool' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.42.0
    - Terraform v0.12.20

options:
    disk_encryption:
        description:
            - Disk encryption for worker node
        required: False
        type: bool
    isolation:
        description:
            - None
        required: False
        type: str
    worker_count:
        description:
            - Specify the desired number of workers per zone in this worker pool
        required: False
        type: int
    zones:
        description:
            - Zone info for worker pool
        required: False
        type: list
        elements: dict
    host_labels:
        description:
            - Labels that describe a Satellite host
        required: False
        type: list
        elements: str
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The name for the worker pool
        required: True
        type: str
    cluster:
        description:
            - (Required for new resource) The unique name for the new IBM Cloud Satellite cluster
        required: True
        type: str
    flavor:
        description:
            - The flavor defines the amount of virtual CPU, memory, and disk space that is set up in each worker node
        required: False
        type: str
    entitlement:
        description:
            - None
        required: False
        type: str
    worker_pool_labels:
        description:
            - Labels on all the workers in the worker pool
        required: False
        type: dict
        elements: str
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
    ('name', 'str'),
    ('cluster', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'disk_encryption',
    'isolation',
    'worker_count',
    'zones',
    'host_labels',
    'resource_group_id',
    'name',
    'cluster',
    'flavor',
    'entitlement',
    'worker_pool_labels',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('name', 'str'),
    ('cluster', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'resource_group_id',
    'name',
    'cluster',
    'region',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    disk_encryption=dict(
        required=False,
        type='bool'),
    isolation=dict(
        required=False,
        type='str'),
    worker_count=dict(
        required=False,
        type='int'),
    zones=dict(
        required=False,
        elements='',
        type='list'),
    host_labels=dict(
        required=False,
        elements='',
        type='list'),
    resource_group_id=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    cluster=dict(
        required=False,
        type='str'),
    flavor=dict(
        required=False,
        type='str'),
    entitlement=dict(
        required=False,
        type='str'),
    worker_pool_labels=dict(
        required=False,
        elements='',
        type='dict'),
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
        resource_type='ibm_satellite_cluster_worker_pool',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.42.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_satellite_cluster_worker_pool',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.42.0',
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
