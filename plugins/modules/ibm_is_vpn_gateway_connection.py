#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_vpn_gateway_connection
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_vpn_gateway_connection

short_description: Configure IBM Cloud 'ibm_is_vpn_gateway_connection' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_vpn_gateway_connection' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    timeout:
        description:
            - Timeout for dead peer detection
        required: False
        type: int
        default: 10
    local:
        description:
            - None
        required: False
        type: list
        elements: dict
    peer:
        description:
            - None
        required: False
        type: list
        elements: dict
    ipsec_policy:
        description:
            - IP security policy for vpn gateway connection
        required: False
        type: str
    ike_policy:
        description:
            - VPN gateway connection IKE Policy
        required: False
        type: str
    name:
        description:
            - (Required for new resource) VPN Gateway connection name
        required: True
        type: str
    admin_state_up:
        description:
            - VPN gateway connection admin state
        required: False
        type: bool
    action:
        description:
            - Action detection for dead peer detection action
        required: False
        type: str
        default: restart
    interval:
        description:
            - Interval for dead peer detection interval
        required: False
        type: int
        default: 2
    vpn_gateway:
        description:
            - (Required for new resource) VPN Gateway info
        required: True
        type: str
    establish_mode:
        description:
            - The establish mode of the VPN gateway connection:- `bidirectional`: Either side of the VPN gateway can initiate IKE protocol   negotiations or rekeying processes.- `peer_only`: Only the peer can initiate IKE protocol negotiations for this VPN gateway   connection. Additionally, the peer is responsible for initiating the rekeying process   after the connection is established. If rekeying does not occur, the VPN gateway   connection will be brought down after its lifetime expires.
        required: False
        type: str
        default: bidirectional
    preshared_key:
        description:
            - (Required for new resource) vpn gateway
        required: True
        type: str
    distribute_traffic:
        description:
            - Indicates whether the traffic is distributed between the `up` tunnels of the VPN gateway connection when the VPC route's next hop is a VPN connection. If `false`, the traffic is only routed through the `up` tunnel with the lower `public_ip` address.
        required: False
        type: bool
        default: False
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
    ('name', 'str'),
    ('vpn_gateway', 'str'),
    ('preshared_key', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'timeout',
    'local',
    'peer',
    'ipsec_policy',
    'ike_policy',
    'name',
    'admin_state_up',
    'action',
    'interval',
    'vpn_gateway',
    'establish_mode',
    'preshared_key',
    'distribute_traffic',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
    'vpn_gateway',
    'vpn_gateway_name',
    'vpn_gateway_connection',
    'vpn_gateway_connection_name',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    timeout=dict(
        required=False,
        type='int'),
    local=dict(
        required=False,
        elements='',
        type='list'),
    peer=dict(
        required=False,
        elements='',
        type='list'),
    ipsec_policy=dict(
        required=False,
        type='str'),
    ike_policy=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    admin_state_up=dict(
        required=False,
        type='bool'),
    action=dict(
        required=False,
        type='str'),
    interval=dict(
        required=False,
        type='int'),
    vpn_gateway=dict(
        required=False,
        type='str'),
    establish_mode=dict(
        required=False,
        type='str'),
    preshared_key=dict(
        required=False,
        type='str'),
    distribute_traffic=dict(
        required=False,
        type='bool'),
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
        resource_type='ibm_is_vpn_gateway_connection',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_vpn_gateway_connection',
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
