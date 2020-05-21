#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_cluster_feature
short_description: Configure IBM Cloud 'ibm_container_cluster_feature' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_cluster_feature' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.6.0
    - Terraform v0.12.20

options:
    private_service_endpoint:
        description:
            - None
        required: False
        type: bool
    reload_workers:
        description:
            - Boolean value set true if worker nodes to be reloaded
        required: False
        type: bool
        default: True
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    cluster:
        description:
            - (Required for new resource) Cluster name of ID
        required: False
        type: str
    public_service_endpoint:
        description:
            - None
        required: False
        type: bool
    public_service_endpoint_url:
        description:
            - None
        required: False
        type: str
    refresh_api_servers:
        description:
            - Boolean value true of API server to be refreshed in K8S cluster
        required: False
        type: bool
        default: True
    private_service_endpoint_url:
        description:
            - None
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
    ('cluster', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'private_service_endpoint',
    'reload_workers',
    'resource_group_id',
    'cluster',
    'public_service_endpoint',
    'public_service_endpoint_url',
    'refresh_api_servers',
    'private_service_endpoint_url',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    private_service_endpoint=dict(
        required=False,
        type='bool'),
    reload_workers=dict(
        default=True,
        type='bool'),
    resource_group_id=dict(
        required=False,
        type='str'),
    cluster=dict(
        required=False,
        type='str'),
    public_service_endpoint=dict(
        required=False,
        type='bool'),
    public_service_endpoint_url=dict(
        required=False,
        type='str'),
    refresh_api_servers=dict(
        default=True,
        type='bool'),
    private_service_endpoint_url=dict(
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

    result = ibmcloud_terraform(
        resource_type='ibm_container_cluster_feature',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.6.0',
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
