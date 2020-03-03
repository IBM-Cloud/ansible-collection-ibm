#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_multi_vlan_firewall
short_description: Configure IBM Cloud 'ibm_multi_vlan_firewall' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_multi_vlan_firewall' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.3
    - Terraform v0.12.20

options:
    public_vlan_id:
        description:
            - None
        required: False
        type: int
    firewall_type:
        description:
            - (Required for new resource) 
        required: False
        type: str
    public_ip:
        description:
            - None
        required: False
        type: str
    password:
        description:
            - None
        required: False
        type: str
    addon_configuration:
        description:
            - "Allowed Values:- ["FortiGate Security Appliance - Web Filtering Add-on (High Availability)","FortiGate Security Appliance - NGFW Add-on (High Availability)","FortiGate Security Appliance - AV Add-on (High Availability)"] or ["FortiGate Security Appliance - Web Filtering Add-on","FortiGate Security Appliance - NGFW Add-on","FortiGate Security Appliance - AV Add-on"]"
        required: False
        type: list
        elements: str
    datacenter:
        description:
            - (Required for new resource) 
        required: False
        type: str
    name:
        description:
            - (Required for new resource) 
        required: False
        type: str
    private_vlan_id:
        description:
            - None
        required: False
        type: int
    public_ipv6:
        description:
            - None
        required: False
        type: str
    private_ip:
        description:
            - None
        required: False
        type: str
    username:
        description:
            - None
        required: False
        type: str
    pod:
        description:
            - (Required for new resource) 
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
    ('firewall_type', 'str'),
    ('datacenter', 'str'),
    ('name', 'str'),
    ('pod', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'public_vlan_id',
    'firewall_type',
    'public_ip',
    'password',
    'addon_configuration',
    'datacenter',
    'name',
    'private_vlan_id',
    'public_ipv6',
    'private_ip',
    'username',
    'pod',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    public_vlan_id=dict(
        required=False,
        type='int'),
    firewall_type=dict(
        required=False,
        type='str'),
    public_ip=dict(
        required=False,
        type='str'),
    password=dict(
        required=False,
        type='str'),
    addon_configuration=dict(
        required=False,
        elements='',
        type='list'),
    datacenter=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    public_ipv6=dict(
        required=False,
        type='str'),
    private_ip=dict(
        required=False,
        type='str'),
    username=dict(
        required=False,
        type='str'),
    pod=dict(
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
        resource_type='ibm_multi_vlan_firewall',
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
