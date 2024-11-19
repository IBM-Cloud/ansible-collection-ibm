#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_instances_info
for_more_info: refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_instances

short_description: Retrieve IBM Cloud 'ibm_is_instances' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_is_instances' resource
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    resource_group:
        description:
            - Instance resource group
        required: False
        type: str
    dedicated_host_name:
        description:
            - Name of the dedicated host to filter the instances attached to it
        required: False
        type: str
    dedicated_host:
        description:
            - ID of the dedicated host to filter the instances attached to it
        required: False
        type: str
    placement_group:
        description:
            - ID of the placement group to filter the instances attached to it
        required: False
        type: str
    instance_group:
        description:
            - Instance group ID to filter the instances attached to it
        required: False
        type: str
    instance_group_name:
        description:
            - Instance group name to filter the instances attached to it
        required: False
        type: str
    vpc_name:
        description:
            - Name of the vpc to filter the instances attached to it
        required: False
        type: str
    vpc:
        description:
            - VPC ID to filter the instances attached to it
        required: False
        type: str
    vpc_crn:
        description:
            - VPC CRN to filter the instances attached to it
        required: False
        type: str
    placement_group_name:
        description:
            - Name of the placement group to filter the instances attached to it
        required: False
        type: str
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
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'resource_group',
    'dedicated_host_name',
    'dedicated_host',
    'placement_group',
    'instance_group',
    'instance_group_name',
    'vpc_name',
    'vpc',
    'vpc_crn',
    'placement_group_name',
]


TL_CONFLICTS_MAP = {
    'dedicated_host_name': ['dedicated_host'],
    'dedicated_host': ['dedicated_host_name'],
    'placement_group': ['placement_group_name'],
    'instance_group': ['vpc', 'vpc_crn', 'vpc_name', 'instance_group_name'],
    'instance_group_name': ['vpc', 'vpc_crn', 'vpc_name', 'instance_group'],
    'vpc_name': ['vpc', 'vpc_crn', 'instance_group'],
    'vpc': ['vpc_name', 'vpc_crn', 'instance_group'],
    'vpc_crn': ['vpc_name', 'vpc', 'instance_group'],
    'placement_group_name': ['placement_group'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    resource_group=dict(
        required=False,
        type='str'),
    dedicated_host_name=dict(
        required=False,
        type='str'),
    dedicated_host=dict(
        required=False,
        type='str'),
    placement_group=dict(
        required=False,
        type='str'),
    instance_group=dict(
        required=False,
        type='str'),
    instance_group_name=dict(
        required=False,
        type='str'),
    vpc_name=dict(
        required=False,
        type='str'),
    vpc=dict(
        required=False,
        type='str'),
    vpc_crn=dict(
        required=False,
        type='str'),
    placement_group_name=dict(
        required=False,
        type='str'),
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

    if 'generation' in module.params:
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
        resource_type='ibm_is_instances',
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
