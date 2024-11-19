#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_vpc_cluster_info
for_more_info: refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/container_vpc_cluster

short_description: Retrieve IBM Cloud 'ibm_container_vpc_cluster' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_container_vpc_cluster' resource
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    wait_till:
        description:
            - wait_till can be configured for Master Ready, One worker Ready, Ingress Ready or Normal
        required: False
        type: str
    name:
        description:
            - Name or id of the cluster
        required: False
        type: str
    alb_type:
        description:
            - None
        required: False
        type: str
        default: all
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    wait_till_timeout:
        description:
            - timeout for wait_till in minutes
        required: False
        type: int
        default: 20
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
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'wait_till',
    'name',
    'alb_type',
    'resource_group_id',
    'wait_till_timeout',
]


TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    wait_till=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    alb_type=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    wait_till_timeout=dict(
        required=False,
        type='int'),
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

    result = ibmcloud_terraform(
        resource_type='ibm_container_vpc_cluster',
        tf_type='data',
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
