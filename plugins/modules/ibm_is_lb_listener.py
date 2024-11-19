#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_lb_listener
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_lb_listener

short_description: Configure IBM Cloud 'ibm_is_lb_listener' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_lb_listener' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    connection_limit:
        description:
            - Connection limit for Loadbalancer
        required: False
        type: int
    port_min:
        description:
            - The inclusive lower bound of the range of ports used by this listener. Only load balancers in the `network` family support more than one port per listener.
        required: False
        type: int
    port_max:
        description:
            - The inclusive upper bound of the range of ports used by this listener. Only load balancers in the `network` family support more than one port per listener
        required: False
        type: int
    protocol:
        description:
            - (Required for new resource) Loadbalancer protocol
        required: True
        type: str
    accept_proxy_protocol:
        description:
            - Listener will forward proxy protocol
        required: False
        type: bool
    default_pool:
        description:
            - Loadbalancer default pool info
        required: False
        type: str
    lb:
        description:
            - (Required for new resource) Loadbalancer listener ID
        required: True
        type: str
    port:
        description:
            - Loadbalancer listener port
        required: False
        type: int
    certificate_instance:
        description:
            - certificate instance for the Loadbalancer
        required: False
        type: str
    https_redirect:
        description:
            - If present, the target listener that requests are redirected to.
        required: False
        type: list
        elements: dict
    idle_connection_timeout:
        description:
            - idle connection timeout of listener
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
    ('protocol', 'str'),
    ('lb', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'connection_limit',
    'port_min',
    'port_max',
    'protocol',
    'accept_proxy_protocol',
    'default_pool',
    'lb',
    'port',
    'certificate_instance',
    'https_redirect',
    'idle_connection_timeout',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('lb', 'str'),
    ('listener_id', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'lb',
    'listener_id',
]

TL_CONFLICTS_MAP = {
    'https_redirect': ['https_redirect_status_code', 'https_redirect_uri', 'https_redirect_listener'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    connection_limit=dict(
        required=False,
        type='int'),
    port_min=dict(
        required=False,
        type='int'),
    port_max=dict(
        required=False,
        type='int'),
    protocol=dict(
        required=False,
        type='str'),
    accept_proxy_protocol=dict(
        required=False,
        type='bool'),
    default_pool=dict(
        required=False,
        type='str'),
    lb=dict(
        required=False,
        type='str'),
    port=dict(
        required=False,
        type='int'),
    certificate_instance=dict(
        required=False,
        type='str'),
    https_redirect=dict(
        required=False,
        elements='',
        type='list'),
    idle_connection_timeout=dict(
        required=False,
        type='int'),
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
        resource_type='ibm_is_lb_listener',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_lb_listener',
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
