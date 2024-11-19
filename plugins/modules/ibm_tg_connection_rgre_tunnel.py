#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_tg_connection_rgre_tunnel
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/tg_connection_rgre_tunnel

short_description: Configure IBM Cloud 'ibm_tg_connection_rgre_tunnel' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_tg_connection_rgre_tunnel' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    name:
        description:
            - (Required for new resource) The user-defined name for this tunnel connection.
        required: True
        type: str
    remote_bgp_asn:
        description:
            - The remote network BGP ASN.
        required: False
        type: int
    network_id:
        description:
            - The ID of the network being connected via this connection. This field is required for some types, such as 'vpc' or 'directlink' or 'power_virtual_server'. The value of this is the CRN of the VPC or direct link or power_virtual_server gateway to be connected. This field is required to be unspecified for network type 'classic', 'gre_tunnel', and 'unbound_gre_tunnel'.
        required: False
        type: str
    connection_id:
        description:
            - (Required for new resource) The Transit Gateway Connection identifier
        required: True
        type: str
    local_gateway_ip:
        description:
            - (Required for new resource) The local gateway IP address.
        required: True
        type: str
    zone:
        description:
            - (Required for new resource) Location of GRE tunnel.
        required: True
        type: str
    base_network_type:
        description:
            - The type of the base network for the RGRE. It should be i.e classic or VPC
        required: False
        type: str
    local_bgp_asn:
        description:
            - The local network BGP ASN.
        required: False
        type: int
    gateway:
        description:
            - (Required for new resource) The Transit Gateway identifier
        required: True
        type: str
    local_tunnel_ip:
        description:
            - (Required for new resource) The local tunnel IP address.
        required: True
        type: str
    remote_gateway_ip:
        description:
            - (Required for new resource) The remote gateway IP address.
        required: True
        type: str
    remote_tunnel_ip:
        description:
            - (Required for new resource) The remote tunnel IP address.
        required: True
        type: str
    network_account_id:
        description:
            - The ID of the account which owns the network that is being connected. Generally only used if the network is in a different account than the gateway. This field is required for type 'unbound_gre_tunnel' when the associated_network_type is 'classic' and the GRE tunnel is in a different account than the gateway.
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
            - The IBM Cloud Classic Infrastructure (SoftLayer) user name. This
              can also be provided via the environment variable
              'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - The IBM Cloud Classic Infrastructure API key. This can also be
              provided via the environment variable 'IAAS_CLASSIC_API_KEY'.
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
    ('connection_id', 'str'),
    ('local_gateway_ip', 'str'),
    ('zone', 'str'),
    ('gateway', 'str'),
    ('local_tunnel_ip', 'str'),
    ('remote_gateway_ip', 'str'),
    ('remote_tunnel_ip', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'name',
    'remote_bgp_asn',
    'network_id',
    'connection_id',
    'local_gateway_ip',
    'zone',
    'base_network_type',
    'local_bgp_asn',
    'gateway',
    'local_tunnel_ip',
    'remote_gateway_ip',
    'remote_tunnel_ip',
    'network_account_id',
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
    name=dict(
        required=False,
        type='str'),
    remote_bgp_asn=dict(
        required=False,
        type='int'),
    network_id=dict(
        required=False,
        type='str'),
    connection_id=dict(
        required=False,
        type='str'),
    local_gateway_ip=dict(
        required=False,
        type='str'),
    zone=dict(
        required=False,
        type='str'),
    base_network_type=dict(
        required=False,
        type='str'),
    local_bgp_asn=dict(
        required=False,
        type='int'),
    gateway=dict(
        required=False,
        type='str'),
    local_tunnel_ip=dict(
        required=False,
        type='str'),
    remote_gateway_ip=dict(
        required=False,
        type='str'),
    remote_tunnel_ip=dict(
        required=False,
        type='str'),
    network_account_id=dict(
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

    result = ibmcloud_terraform(
        resource_type='ibm_tg_connection_rgre_tunnel',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.71.2',
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
