#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cis_global_load_balancer
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cis_global_load_balancer

short_description: Configure IBM Cloud 'ibm_cis_global_load_balancer' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cis_global_load_balancer' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    domain_id:
        description:
            - (Required for new resource) Associated CIS domain
        required: True
        type: str
    default_pool_ids:
        description:
            - (Required for new resource) List of default Pool IDs
        required: True
        type: list
        elements: str
    cis_id:
        description:
            - (Required for new resource) CIS instance crn
        required: True
        type: str
    description:
        description:
            - Description for the load balancer instance
        required: False
        type: str
    pop_pools:
        description:
            - None
        required: False
        type: list
        elements: dict
    session_affinity:
        description:
            - Session affinity info
        required: False
        type: str
        default: none
    name:
        description:
            - (Required for new resource) name
        required: True
        type: str
    fallback_pool_id:
        description:
            - (Required for new resource) fallback pool ID
        required: True
        type: str
    proxied:
        description:
            - set to true if proxy needs to be enabled
        required: False
        type: bool
        default: False
    region_pools:
        description:
            - None
        required: False
        type: list
        elements: dict
    ttl:
        description:
            - TTL value
        required: False
        type: int
        default: 60
    steering_policy:
        description:
            - Steering policy info
        required: False
        type: str
    enabled:
        description:
            - set to true of LB needs to enabled
        required: False
        type: bool
        default: True
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
            - The IBM Cloud Classic Infrastructure (SoftLayer) user name. This
              can also be provided via the environment variable
              'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - The IBM Cloud Classic Infrastructure API key. This can also be
              provided via the environment variable 'IAAS_CLASSIC_API_KEY'.
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
    ('domain_id', 'str'),
    ('default_pool_ids', 'list'),
    ('cis_id', 'str'),
    ('name', 'str'),
    ('fallback_pool_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'domain_id',
    'default_pool_ids',
    'cis_id',
    'description',
    'pop_pools',
    'session_affinity',
    'name',
    'fallback_pool_id',
    'proxied',
    'region_pools',
    'ttl',
    'steering_policy',
    'enabled',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
    'proxied': ['ttl'],
    'ttl': ['proxied'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    domain_id=dict(
        required=False,
        type='str'),
    default_pool_ids=dict(
        required=False,
        elements='',
        type='list'),
    cis_id=dict(
        required=False,
        type='str'),
    description=dict(
        required=False,
        type='str'),
    pop_pools=dict(
        required=False,
        elements='',
        type='list'),
    session_affinity=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    fallback_pool_id=dict(
        required=False,
        type='str'),
    proxied=dict(
        required=False,
        type='bool'),
    region_pools=dict(
        required=False,
        elements='',
        type='list'),
    ttl=dict(
        required=False,
        type='int'),
    steering_policy=dict(
        required=False,
        type='str'),
    enabled=dict(
        required=False,
        type='bool'),
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

    result = ibmcloud_terraform(
        resource_type='ibm_cis_global_load_balancer',
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
