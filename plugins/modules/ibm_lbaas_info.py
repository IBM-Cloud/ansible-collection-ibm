#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_lbaas_info
short_description: Retrieve IBM Cloud 'ibm_lbaas' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_lbaas' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.4
    - Terraform v0.12.20

options:
    health_monitors:
        description:
            - None
        required: False
        type: list
        elements: dict
    server_instances:
        description:
            - None
        required: False
        type: list
        elements: dict
    name:
        description:
            - None
        required: True
        type: str
    type:
        description:
            - None
        required: False
        type: str
    datacenter:
        description:
            - None
        required: False
        type: str
    active_connections:
        description:
            - None
        required: False
        type: int
    use_system_public_ip_pool:
        description:
            - None
        required: False
        type: bool
    status:
        description:
            - None
        required: False
        type: str
    ssl_ciphers:
        description:
            - None
        required: False
        type: list
        elements: str
    protocols:
        description:
            - None
        required: False
        type: list
        elements: dict
    server_instances_up:
        description:
            - None
        required: False
        type: int
    server_instances_down:
        description:
            - None
        required: False
        type: int
    description:
        description:
            - None
        required: False
        type: str
    vip:
        description:
            - None
        required: False
        type: str
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be 
              provided via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone 
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'health_monitors',
    'server_instances',
    'name',
    'type',
    'datacenter',
    'active_connections',
    'use_system_public_ip_pool',
    'status',
    'ssl_ciphers',
    'protocols',
    'server_instances_up',
    'server_instances_down',
    'description',
    'vip',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    health_monitors=dict(
        required=False,
        elements='',
        type='list'),
    server_instances=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=True,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    active_connections=dict(
        required=False,
        type='int'),
    use_system_public_ip_pool=dict(
        required=False,
        type='bool'),
    status=dict(
        required=False,
        type='str'),
    ssl_ciphers=dict(
        required=False,
        elements='',
        type='list'),
    protocols=dict(
        required=False,
        elements='',
        type='list'),
    server_instances_up=dict(
        required=False,
        type='int'),
    server_instances_down=dict(
        required=False,
        type='int'),
    description=dict(
        required=False,
        type='str'),
    vip=dict(
        required=False,
        type='str'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_lbaas',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.2.4',
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
