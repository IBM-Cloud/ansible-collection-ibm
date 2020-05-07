#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_app_info
short_description: Retrieve IBM Cloud 'ibm_app' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_app' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.5.2
    - Terraform v0.12.20

options:
    health_check_timeout:
        description:
            - Timeout in seconds for health checking of an staged app when starting up.
        required: False
        type: int
    name:
        description:
            - The name for the app
        required: True
        type: str
    instances:
        description:
            - The number of instances
        required: False
        type: int
    environment_json:
        description:
            - Key/value pairs of all the environment variables to run in your app. Does not include any system or service variables.
        required: False
        type: dict
    health_check_http_endpoint:
        description:
            - Endpoint called to determine if the app is healthy.
        required: False
        type: str
    memory:
        description:
            - The amount of memory each instance should have. In megabytes.
        required: False
        type: int
    buildpack:
        description:
            - Buildpack to build the app. 3 options: a) Blank means autodetection; b) A Git Url pointing to a buildpack; c) Name of an installed buildpack.
        required: False
        type: str
    route_guid:
        description:
            - Define the route guids which should be bound to the application.
        required: False
        type: list
        elements: str
    package_state:
        description:
            - The state of the application package whether staged, pending etc
        required: False
        type: str
    state:
        description:
            - The state of the application
        required: False
        type: str
    health_check_type:
        description:
            - Type of health check to perform.
        required: False
        type: str
    space_guid:
        description:
            - Define space guid to which app belongs
        required: True
        type: str
    disk_quota:
        description:
            - The maximum amount of disk available to an instance of an app. In megabytes.
        required: False
        type: int
    service_instance_guid:
        description:
            - Define the service instance guids that should be bound to this application.
        required: False
        type: list
        elements: str
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
    ('space_guid', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'health_check_timeout',
    'name',
    'instances',
    'environment_json',
    'health_check_http_endpoint',
    'memory',
    'buildpack',
    'route_guid',
    'package_state',
    'state',
    'health_check_type',
    'space_guid',
    'disk_quota',
    'service_instance_guid',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    health_check_timeout=dict(
        required=False,
        type='int'),
    name=dict(
        required=True,
        type='str'),
    instances=dict(
        required=False,
        type='int'),
    environment_json=dict(
        required=False,
        type='dict'),
    health_check_http_endpoint=dict(
        required=False,
        type='str'),
    memory=dict(
        required=False,
        type='int'),
    buildpack=dict(
        required=False,
        type='str'),
    route_guid=dict(
        required=False,
        elements='',
        type='list'),
    package_state=dict(
        required=False,
        type='str'),
    state=dict(
        required=False,
        type='str'),
    health_check_type=dict(
        required=False,
        type='str'),
    space_guid=dict(
        required=True,
        type='str'),
    disk_quota=dict(
        required=False,
        type='int'),
    service_instance_guid=dict(
        required=False,
        elements='',
        type='list'),
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
    import ansible.module_utils.ibmcloud as ibmcloud

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_app',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.5.2',
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
