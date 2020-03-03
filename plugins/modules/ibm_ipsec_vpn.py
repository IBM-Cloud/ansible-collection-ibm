#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_ipsec_vpn
short_description: Configure IBM Cloud 'ibm_ipsec_vpn' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_ipsec_vpn' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.3
    - Terraform v0.12.20

options:
    customer_peer_ip:
        description:
            - None
        required: False
        type: str
    datacenter:
        description:
            - (Required for new resource) 
        required: False
        type: str
    internal_peer_ip_address:
        description:
            - None
        required: False
        type: str
    name:
        description:
            - None
        required: False
        type: str
    phase_one:
        description:
            - None
        required: False
        type: list
        elements: dict
    phase_two:
        description:
            - None
        required: False
        type: list
        elements: dict
    address_translation:
        description:
            - None
        required: False
        type: list
        elements: dict
    preshared_key:
        description:
            - None
        required: False
        type: str
    internal_subnet_id:
        description:
            - None
        required: False
        type: int
    remote_subnet_id:
        description:
            - None
        required: False
        type: int
    remote_subnet:
        description:
            - None
        required: False
        type: list
        elements: dict
    service_subnet_id:
        description:
            - None
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
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be provided
              via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('datacenter', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'customer_peer_ip',
    'datacenter',
    'internal_peer_ip_address',
    'name',
    'phase_one',
    'phase_two',
    'address_translation',
    'preshared_key',
    'internal_subnet_id',
    'remote_subnet_id',
    'remote_subnet',
    'service_subnet_id',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    customer_peer_ip=dict(
        required=False,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    internal_peer_ip_address=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    phase_one=dict(
        required=False,
        elements='',
        type='list'),
    phase_two=dict(
        required=False,
        elements='',
        type='list'),
    address_translation=dict(
        required=False,
        elements='',
        type='list'),
    preshared_key=dict(
        required=False,
        type='str'),
    internal_subnet_id=dict(
        required=False,
        type='int'),
    remote_subnet_id=dict(
        required=False,
        type='int'),
    remote_subnet=dict(
        required=False,
        elements='',
        type='list'),
    service_subnet_id=dict(
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
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south')
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

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

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_ipsec_vpn',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.2.3',
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
