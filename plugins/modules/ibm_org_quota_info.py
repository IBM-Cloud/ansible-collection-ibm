#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_org_quota_info
short_description: Retrieve IBM Cloud 'ibm_org_quota' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_org_quota' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.4
    - Terraform v0.12.20

options:
    memory_limit:
        description:
            - Defines the total memory limit for organization.
        required: False
        type: int
    instance_memory_limit:
        description:
            - Defines the  total instance memory limit for organization.
        required: False
        type: int
    trial_db_allowed:
        description:
            - Defines trial db are allowed for organization.
        required: False
        type: bool
    total_service_keys:
        description:
            - Defines the total service keys for organization.
        required: False
        type: int
    name:
        description:
            - Org quota name, for example qIBM
        required: True
        type: str
    total_services:
        description:
            - Defines the total services for organization.
        required: False
        type: int
    app_instance_limit:
        description:
            - Defines the total app instance limit for organization.
        required: False
        type: int
    total_private_domains:
        description:
            - Defines the total private domain limit for organization.v
        required: False
        type: int
    app_tasks_limit:
        description:
            - Defines the total app task limit for organization.
        required: False
        type: int
    total_reserved_route_ports:
        description:
            - Defines the number of reserved route ports for organization.
        required: False
        type: int
    non_basic_services_allowed:
        description:
            - Define non basic services are allowed for organization.
        required: False
        type: bool
    total_routes:
        description:
            - Defines the total route for organization.
        required: False
        type: int
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
    'memory_limit',
    'instance_memory_limit',
    'trial_db_allowed',
    'total_service_keys',
    'name',
    'total_services',
    'app_instance_limit',
    'total_private_domains',
    'app_tasks_limit',
    'total_reserved_route_ports',
    'non_basic_services_allowed',
    'total_routes',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    memory_limit=dict(
        required=False,
        type='int'),
    instance_memory_limit=dict(
        required=False,
        type='int'),
    trial_db_allowed=dict(
        required=False,
        type='bool'),
    total_service_keys=dict(
        required=False,
        type='int'),
    name=dict(
        required=True,
        type='str'),
    total_services=dict(
        required=False,
        type='int'),
    app_instance_limit=dict(
        required=False,
        type='int'),
    total_private_domains=dict(
        required=False,
        type='int'),
    app_tasks_limit=dict(
        required=False,
        type='int'),
    total_reserved_route_ports=dict(
        required=False,
        type='int'),
    non_basic_services_allowed=dict(
        required=False,
        type='bool'),
    total_routes=dict(
        required=False,
        type='int'),
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
        resource_type='ibm_org_quota',
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
