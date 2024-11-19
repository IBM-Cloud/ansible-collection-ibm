#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_vpc_worker
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_vpc_worker

short_description: Configure IBM Cloud 'ibm_container_vpc_worker' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_vpc_worker' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    replace_worker:
        description:
            - (Required for new resource) Worker name/id that needs to be replaced
        required: True
        type: str
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    kube_config_path:
        description:
            - Path of downloaded cluster config
        required: False
        type: str
    cluster_name:
        description:
            - (Required for new resource) Cluster name
        required: True
        type: str
    sds:
        description:
            - Name of Software Defined Storage
        required: False
        type: str
    sds_timeout:
        description:
            - Timeout for checking sds deployment/status
        required: False
        type: str
        default: 15m
    check_ptx_status:
        description:
            - Check portworx status after worker replace
        required: False
        type: bool
        default: False
    ptx_timeout:
        description:
            - Timeout for checking ptx pods/status
        required: False
        type: str
        default: 15m
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
    ('replace_worker', 'str'),
    ('cluster_name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'replace_worker',
    'resource_group_id',
    'kube_config_path',
    'cluster_name',
    'sds',
    'sds_timeout',
    'check_ptx_status',
    'ptx_timeout',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
    'sds': ['check_ptx_status'],
    'check_ptx_status': ['sds'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    replace_worker=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    kube_config_path=dict(
        required=False,
        type='str'),
    cluster_name=dict(
        required=False,
        type='str'),
    sds=dict(
        required=False,
        type='str'),
    sds_timeout=dict(
        required=False,
        type='str'),
    check_ptx_status=dict(
        required=False,
        type='bool'),
    ptx_timeout=dict(
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

    result = ibmcloud_terraform(
        resource_type='ibm_container_vpc_worker',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.71.2',
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
