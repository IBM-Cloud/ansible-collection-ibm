#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_dl_gateway
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/dl_gateway

short_description: Configure IBM Cloud 'ibm_dl_gateway' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_dl_gateway' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.65.1
    - Terraform v1.5.5

options:
    metered:
        description:
            - (Required for new resource) Metered billing option
        required: True
        type: bool
    speed_mbps:
        description:
            - (Required for new resource) Gateway speed in megabits per second
        required: True
        type: int
    loa_reject_reason:
        description:
            - Loa reject reason
        required: False
        type: str
    tags:
        description:
            - Tags for the direct link gateway
        required: False
        type: list
        elements: str
    bgp_asn:
        description:
            - (Required for new resource) BGP ASN
        required: True
        type: int
    connection_mode:
        description:
            - Type of services this Gateway is attached to. Mode transit means this Gateway will be attached to Transit Gateway Service and direct means this Gateway will be attached to vpc or classic connection
        required: False
        type: str
    global_:
        description:
            - (Required for new resource) Gateways with global routing (true) can connect to networks outside their associated region
        required: True
        type: bool
    name:
        description:
            - (Required for new resource) The unique user-defined name for this gateway
        required: True
        type: str
    resource_group:
        description:
            - Gateway resource group
        required: False
        type: str
    as_prepends:
        description:
            - List of AS Prepend configuration information
        required: False
        type: list
        elements: dict
    bfd_interval:
        description:
            - BFD Interval
        required: False
        type: int
    port:
        description:
            - Gateway port
        required: False
        type: str
    vlan:
        description:
            - VLAN allocated for this gateway
        required: False
        type: int
    bgp_base_cidr:
        description:
            - BGP base CIDR
        required: False
        type: str
    remove_vlan:
        description:
            - Remove VLAN allocated for this dedicated gateway
        required: False
        type: bool
        default: False
    authentication_key:
        description:
            - BGP MD5 authentication key
        required: False
        type: str
    bfd_status:
        description:
            - Gateway BFD status
        required: False
        type: str
    macsec_config:
        description:
            - MACsec configuration information
        required: False
        type: list
        elements: dict
    export_route_filters:
        description:
            - List Export Route Filters for a Direct Link gateway
        required: False
        type: list
        elements: dict
    default_import_route_filter:
        description:
            - The default directional route filter action that applies to routes that do not match any directional route filters
        required: False
        type: str
    carrier_name:
        description:
            - Carrier name
        required: False
        type: str
    default_export_route_filter:
        description:
            - The default directional route filter action that applies to routes that do not match any directional route filters
        required: False
        type: str
    bfd_multiplier:
        description:
            - BFD Multiplier
        required: False
        type: int
    cross_connect_router:
        description:
            - Cross connect router
        required: False
        type: str
    location_name:
        description:
            - Gateway location
        required: False
        type: str
    type:
        description:
            - (Required for new resource) Gateway type
        required: True
        type: str
    bgp_ibm_cidr:
        description:
            - BGP IBM CIDR
        required: False
        type: str
    import_route_filters:
        description:
            - List Import Route Filters for a Direct Link gateway
        required: False
        type: list
        elements: dict
    bfd_status_updated_at:
        description:
            - Date and time BFD status was updated
        required: False
        type: str
    customer_name:
        description:
            - Customer name
        required: False
        type: str
    bgp_cer_cidr:
        description:
            - BGP customer edge router CIDR
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
    ('metered', 'bool'),
    ('speed_mbps', 'int'),
    ('bgp_asn', 'int'),
    ('global_', 'bool'),
    ('name', 'str'),
    ('type', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'metered',
    'speed_mbps',
    'loa_reject_reason',
    'tags',
    'bgp_asn',
    'connection_mode',
    'global_',
    'name',
    'resource_group',
    'as_prepends',
    'bfd_interval',
    'port',
    'vlan',
    'bgp_base_cidr',
    'remove_vlan',
    'authentication_key',
    'bfd_status',
    'macsec_config',
    'export_route_filters',
    'default_import_route_filter',
    'carrier_name',
    'default_export_route_filter',
    'bfd_multiplier',
    'cross_connect_router',
    'location_name',
    'type',
    'bgp_ibm_cidr',
    'import_route_filters',
    'bfd_status_updated_at',
    'customer_name',
    'bgp_cer_cidr',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('name', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'bgp_status_updated_at',
    'link_status_updated_at',
    'name',
]

TL_CONFLICTS_MAP = {
    'port': ['location_name', 'cross_connect_router', 'carrier_name', 'customer_name'],
    'vlan': ['remove_vlan'],
    'remove_vlan': ['vlan'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    metered=dict(
        required=False,
        type='bool'),
    speed_mbps=dict(
        required=False,
        type='int'),
    loa_reject_reason=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    bgp_asn=dict(
        required=False,
        type='int'),
    connection_mode=dict(
        required=False,
        type='str'),
    global_=dict(
        required=False,
        type='bool'),
    name=dict(
        required=False,
        type='str'),
    resource_group=dict(
        required=False,
        type='str'),
    as_prepends=dict(
        required=False,
        elements='',
        type='list'),
    bfd_interval=dict(
        required=False,
        type='int'),
    port=dict(
        required=False,
        type='str'),
    vlan=dict(
        required=False,
        type='int'),
    bgp_base_cidr=dict(
        required=False,
        type='str'),
    remove_vlan=dict(
        required=False,
        type='bool'),
    authentication_key=dict(
        required=False,
        type='str'),
    bfd_status=dict(
        required=False,
        type='str'),
    macsec_config=dict(
        required=False,
        elements='',
        type='list'),
    export_route_filters=dict(
        required=False,
        elements='',
        type='list'),
    default_import_route_filter=dict(
        required=False,
        type='str'),
    carrier_name=dict(
        required=False,
        type='str'),
    default_export_route_filter=dict(
        required=False,
        type='str'),
    bfd_multiplier=dict(
        required=False,
        type='int'),
    cross_connect_router=dict(
        required=False,
        type='str'),
    location_name=dict(
        required=False,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    bgp_ibm_cidr=dict(
        required=False,
        type='str'),
    import_route_filters=dict(
        required=False,
        elements='',
        type='list'),
    bfd_status_updated_at=dict(
        required=False,
        type='str'),
    customer_name=dict(
        required=False,
        type='str'),
    bgp_cer_cidr=dict(
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

    result_ds = ibmcloud_terraform(
        resource_type='ibm_dl_gateway',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.65.1',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_dl_gateway',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.65.1',
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
