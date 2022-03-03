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
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.39.1
    - Terraform v0.12.20

options:
    https_redirect_listener:
        description:
            - ID of the listener that will be set as http redirect target
        required: False
        type: str
    connection_limit:
        description:
            - Connection limit for Loadbalancer
        required: False
        type: int
    default_pool:
        description:
            - Loadbalancer default pool info
        required: False
        type: str
    protocol:
        description:
            - (Required for new resource) Loadbalancer protocol
        required: True
        type: str
    certificate_instance:
        description:
            - certificate instance for the Loadbalancer
        required: False
        type: str
    https_redirect_status_code:
        description:
            - The HTTP status code to be returned in the redirect response
        required: False
        type: int
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
    accept_proxy_protocol:
        description:
            - Listener will forward proxy protocol
        required: False
        type: bool
    https_redirect_uri:
        description:
            - Target URI where traffic will be redirected
        required: False
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
        type: int
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
    'https_redirect_listener',
    'connection_limit',
    'default_pool',
    'protocol',
    'certificate_instance',
    'https_redirect_status_code',
    'lb',
    'port',
    'accept_proxy_protocol',
    'https_redirect_uri',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    https_redirect_listener=dict(
        required=False,
        type='str'),
    connection_limit=dict(
        required=False,
        type='int'),
    default_pool=dict(
        required=False,
        type='str'),
    protocol=dict(
        required=False,
        type='str'),
    certificate_instance=dict(
        required=False,
        type='str'),
    https_redirect_status_code=dict(
        required=False,
        type='int'),
    lb=dict(
        required=False,
        type='str'),
    port=dict(
        required=False,
        type='int'),
    accept_proxy_protocol=dict(
        required=False,
        type='bool'),
    https_redirect_uri=dict(
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
        resource_type='ibm_is_lb_listener',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.39.1',
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
