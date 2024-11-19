#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_lb_pool
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_lb_pool

short_description: Configure IBM Cloud 'ibm_is_lb_pool' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_lb_pool' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    health_monitor_port:
        description:
            - Health monitor Port the LB Pool
        required: False
        type: int
    session_persistence_type:
        description:
            - Load Balancer Pool session persisence type.
        required: False
        type: str
    health_delay:
        description:
            - (Required for new resource) Load Blancer health delay time period
        required: True
        type: int
    health_type:
        description:
            - (Required for new resource) Load Balancer health type
        required: True
        type: str
    session_persistence_app_cookie_name:
        description:
            - Load Balancer Pool session persisence app cookie name.
        required: False
        type: str
    proxy_protocol:
        description:
            - PROXY protocol setting for this pool
        required: False
        type: str
    algorithm:
        description:
            - (Required for new resource) Load Balancer Pool algorithm
        required: True
        type: str
    protocol:
        description:
            - (Required for new resource) Load Balancer Protocol
        required: True
        type: str
    health_timeout:
        description:
            - (Required for new resource) Load Balancer health timeout interval
        required: True
        type: int
    health_monitor_url:
        description:
            - Health monitor URL of LB Pool
        required: False
        type: str
    health_retries:
        description:
            - (Required for new resource) Load Balancer health retry count
        required: True
        type: int
    name:
        description:
            - (Required for new resource) Load Balancer Pool name
        required: True
        type: str
    lb:
        description:
            - (Required for new resource) Load Balancer ID
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
    ('health_delay', 'int'),
    ('health_type', 'str'),
    ('algorithm', 'str'),
    ('protocol', 'str'),
    ('health_timeout', 'int'),
    ('health_retries', 'int'),
    ('name', 'str'),
    ('lb', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'health_monitor_port',
    'session_persistence_type',
    'health_delay',
    'health_type',
    'session_persistence_app_cookie_name',
    'proxy_protocol',
    'algorithm',
    'protocol',
    'health_timeout',
    'health_monitor_url',
    'health_retries',
    'name',
    'lb',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('lb', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'name',
    'lb',
    'identifier',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    health_monitor_port=dict(
        required=False,
        type='int'),
    session_persistence_type=dict(
        required=False,
        type='str'),
    health_delay=dict(
        required=False,
        type='int'),
    health_type=dict(
        required=False,
        type='str'),
    session_persistence_app_cookie_name=dict(
        required=False,
        type='str'),
    proxy_protocol=dict(
        required=False,
        type='str'),
    algorithm=dict(
        required=False,
        type='str'),
    protocol=dict(
        required=False,
        type='str'),
    health_timeout=dict(
        required=False,
        type='int'),
    health_monitor_url=dict(
        required=False,
        type='str'),
    health_retries=dict(
        required=False,
        type='int'),
    name=dict(
        required=False,
        type='str'),
    lb=dict(
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

    result_ds = ibmcloud_terraform(
        resource_type='ibm_is_lb_pool',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_lb_pool',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.71.2',
            tl_required_params=TL_REQUIRED_PARAMETERS,
            tl_all_params=TL_ALL_PARAMETERS)
        if result['rc'] > 0:
            module.fail_json(
                msg=Terraform.parse_stderr(result['stderr']), **result)

        module.exit_json(**result)
    else:
        module.exit_json(**result_ds)


def main():
    run_module()


if __name__ == '__main__':
    main()
