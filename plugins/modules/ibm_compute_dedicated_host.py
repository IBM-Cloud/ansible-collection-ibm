#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_dedicated_host
short_description: Configure IBM Cloud 'ibm_compute_dedicated_host' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_compute_dedicated_host' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.8.1
    - Terraform v0.12.20

options:
    memory_capacity:
        description:
            - The capacity that the dedicated host's memory allocation is restricted to.
        required: False
        type: int
    domain:
        description:
            - (Required for new resource) The domain of dedicatated host.
        required: True
        type: str
    datacenter:
        description:
            - (Required for new resource) The data center in which the dedicatated host is to be provisioned.
        required: True
        type: str
    router_hostname:
        description:
            - (Required for new resource) The hostname of the primary router that the dedicated host is associated with.
        required: True
        type: str
    disk_capacity:
        description:
            - The capacity that the dedicated host's disk allocation is restricted to.
        required: False
        type: int
    wait_time_minutes:
        description:
            - None
        required: False
        type: int
        default: 90
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    hostname:
        description:
            - (Required for new resource) The host name of dedicatated host.
        required: True
        type: str
    flavor:
        description:
            - The flavor of the dedicatated host.
        required: False
        type: str
        default: 56_CORES_X_242_RAM_X_1_4_TB
    hourly_billing:
        description:
            - The billing type for the dedicatated host.
        required: False
        type: bool
        default: True
    cpu_count:
        description:
            - The capacity that the dedicated host's CPU allocation is restricted to.
        required: False
        type: int
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
    ('domain', 'str'),
    ('datacenter', 'str'),
    ('router_hostname', 'str'),
    ('hostname', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'memory_capacity',
    'domain',
    'datacenter',
    'router_hostname',
    'disk_capacity',
    'wait_time_minutes',
    'tags',
    'hostname',
    'flavor',
    'hourly_billing',
    'cpu_count',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    memory_capacity=dict(
        required= False,
        type='int'),
    domain=dict(
        required= False,
        type='str'),
    datacenter=dict(
        required= False,
        type='str'),
    router_hostname=dict(
        required= False,
        type='str'),
    disk_capacity=dict(
        required= False,
        type='int'),
    wait_time_minutes=dict(
        default=90,
        type='int'),
    tags=dict(
        required= False,
        elements='',
        type='list'),
    hostname=dict(
        required= False,
        type='str'),
    flavor=dict(
        default='56_CORES_X_242_RAM_X_1_4_TB',
        type='str'),
    hourly_billing=dict(
        default=True,
        type='bool'),
    cpu_count=dict(
        required= False,
        type='int'),
    id=dict(
        required= False,
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

    result = ibmcloud_terraform(
        resource_type='ibm_compute_dedicated_host',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.8.1',
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
