#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_subnet_info
short_description: Retrieve IBM Cloud 'ibm_is_subnet' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_is_subnet' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.4.0
    - Terraform v0.12.20

options:
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance
        required: False
        type: str
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    ip_version:
        description:
            - NA
        required: False
        type: int
    name:
        description:
            - NA
        required: False
        type: str
    network_acl:
        description:
            - NA
        required: False
        type: str
    public_gateway:
        description:
            - NA
        required: False
        type: str
    status:
        description:
            - NA
        required: False
        type: str
    identifier:
        description:
            - NA
        required: True
        type: str
    ipv4_cidr_block:
        description:
            - NA
        required: False
        type: str
    available_ipv4_address_count:
        description:
            - NA
        required: False
        type: str
    zone:
        description:
            - NA
        required: False
        type: str
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    ipv6_cidr_block:
        description:
            - NA
        required: False
        type: str
    total_ipv4_address_count:
        description:
            - NA
        required: False
        type: int
    vpc:
        description:
            - NA
        required: False
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
    ('identifier', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'resource_group_name',
    'resource_controller_url',
    'resource_crn',
    'resource_status',
    'ip_version',
    'name',
    'network_acl',
    'public_gateway',
    'status',
    'identifier',
    'ipv4_cidr_block',
    'available_ipv4_address_count',
    'zone',
    'resource_name',
    'ipv6_cidr_block',
    'total_ipv4_address_count',
    'vpc',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    resource_group_name=dict(
        required=False,
        type='str'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    resource_crn=dict(
        required=False,
        type='str'),
    resource_status=dict(
        required=False,
        type='str'),
    ip_version=dict(
        required=False,
        type='int'),
    name=dict(
        required=False,
        type='str'),
    network_acl=dict(
        required=False,
        type='str'),
    public_gateway=dict(
        required=False,
        type='str'),
    status=dict(
        required=False,
        type='str'),
    identifier=dict(
        required=True,
        type='str'),
    ipv4_cidr_block=dict(
        required=False,
        type='str'),
    available_ipv4_address_count=dict(
        required=False,
        type='str'),
    zone=dict(
        required=False,
        type='str'),
    resource_name=dict(
        required=False,
        type='str'),
    ipv6_cidr_block=dict(
        required=False,
        type='str'),
    total_ipv4_address_count=dict(
        required=False,
        type='int'),
    vpc=dict(
        required=False,
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
    import ansible.module_utils.ibmcloud as ibmcloud

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

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_is_subnet',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.4.0',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
