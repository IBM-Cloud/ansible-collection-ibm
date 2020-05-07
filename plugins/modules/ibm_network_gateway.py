#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_network_gateway
short_description: Configure IBM Cloud 'ibm_network_gateway' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_network_gateway' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.5.2
    - Terraform v0.12.20

options:
    private_vlan_id:
        description:
            - None
        required: False
        type: int
    public_ipv6_address_id:
        description:
            - None
        required: False
        type: int
    public_vlan_id:
        description:
            - None
        required: False
        type: int
    members:
        description:
            - (Required for new resource) The hardware members of this network Gateway
        required: False
        type: list
        elements: dict
    associated_vlans:
        description:
            - The VLAN instances associated with this Network Gateway
        required: False
        type: list
        elements: dict
    post_install_script_uri:
        description:
            - None
        required: False
        type: str
    private_ip_address_id:
        description:
            - None
        required: False
        type: int
    public_ipv4_address:
        description:
            - None
        required: False
        type: str
    public_ip_address_id:
        description:
            - None
        required: False
        type: int
    status:
        description:
            - None
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The name of the gateway
        required: False
        type: str
    ssh_key_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    private_ipv4_address:
        description:
            - None
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
    ('members', 'list'),
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'private_vlan_id',
    'public_ipv6_address_id',
    'public_vlan_id',
    'members',
    'associated_vlans',
    'post_install_script_uri',
    'private_ip_address_id',
    'public_ipv4_address',
    'public_ip_address_id',
    'status',
    'name',
    'ssh_key_ids',
    'private_ipv4_address',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    private_vlan_id=dict(
        required=False,
        type='int'),
    public_ipv6_address_id=dict(
        required=False,
        type='int'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    members=dict(
        required=False,
        elements='',
        type='list'),
    associated_vlans=dict(
        required=False,
        elements='',
        type='list'),
    post_install_script_uri=dict(
        required=False,
        type='str'),
    private_ip_address_id=dict(
        required=False,
        type='int'),
    public_ipv4_address=dict(
        required=False,
        type='str'),
    public_ip_address_id=dict(
        required=False,
        type='int'),
    status=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    ssh_key_ids=dict(
        required=False,
        elements='',
        type='list'),
    private_ipv4_address=dict(
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
        resource_type='ibm_network_gateway',
        tf_type='resource',
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
