#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_alb_create
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/container_alb_create

short_description: Configure IBM Cloud 'ibm_container_alb_create' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_alb_create' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    enable:
        description:
            - If set to true, the ALB is enabled by default.
        required: False
        type: bool
        default: True
    nlb_version:
        description:
            - The version of the network load balancer that you want to use for the ALB.
        required: False
        type: str
    cluster:
        description:
            - (Required for new resource) The ID of the cluster that the ALB belongs to.
        required: True
        type: str
    alb_type:
        description:
            - (Required for new resource) The type of ALB that you want to create.
        required: True
        type: str
    ingress_image:
        description:
            - The type of Ingress image that you want to use for your ALB deployment.
        required: False
        type: str
    vlan_id:
        description:
            - (Required for new resource) The VLAN ID that you want to use for your ALBs.
        required: True
        type: str
    ip:
        description:
            - The IP address that you want to assign to the ALB.
        required: False
        type: str
    zone:
        description:
            - (Required for new resource) The zone where you want to deploy the ALB.
        required: True
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
    ('alb_type', 'str'),
    ('vlan_id', 'str'),
    ('zone', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'enable',
    'nlb_version',
    'cluster',
    'alb_type',
    'ingress_image',
    'vlan_id',
    'ip',
    'zone',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    enable=dict(
        required=False,
        type='bool'),
    nlb_version=dict(
        required=False,
        type='str'),
    cluster=dict(
        required=False,
        type='str'),
    alb_type=dict(
        required=False,
        type='str'),
    ingress_image=dict(
        required=False,
        type='str'),
    vlan_id=dict(
        required=False,
        type='str'),
    ip=dict(
        required=False,
        type='str'),
    zone=dict(
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
        resource_type='ibm_container_alb_create',
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
