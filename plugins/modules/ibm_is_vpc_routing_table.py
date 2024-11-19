#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_vpc_routing_table
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_vpc_routing_table

short_description: Configure IBM Cloud 'ibm_is_vpc_routing_table' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_vpc_routing_table' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    tags:
        description:
            - List of tags
        required: False
        type: list
        elements: str
    accept_routes_from_resource_type:
        description:
            - The filters specifying the resources that may create routes in this routing table, The resource type: vpn_gateway or vpn_server
        required: False
        type: list
        elements: str
    advertise_routes_to:
        description:
            - The ingress sources to advertise routes to. Routes in the table with `advertise` enabled will be advertised to these sources.
        required: False
        type: list
        elements: str
    route_direct_link_ingress:
        description:
            - If set to true, this routing table will be used to route traffic that originates from Direct Link to this VPC.
        required: False
        type: bool
        default: False
    route_internet_ingress:
        description:
            - If set to true, this routing table will be used to route traffic that originates from the internet. For this to succeed, the VPC must not already have a routing table with this property set to true.
        required: False
        type: bool
        default: False
    route_transit_gateway_ingress:
        description:
            - If set to true, this routing table will be used to route traffic that originates from Transit Gateway to this VPC.
        required: False
        type: bool
        default: False
    vpc:
        description:
            - (Required for new resource) The VPC identifier.
        required: True
        type: str
    name:
        description:
            - The user-defined name for this routing table.
        required: False
        type: str
    route_vpc_zone_ingress:
        description:
            - If set to true, this routing table will be used to route traffic that originates from subnets in other zones in this VPC.
        required: False
        type: bool
        default: False
    access_tags:
        description:
            - List of access management tags
        required: False
        type: list
        elements: str
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
    ('vpc', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'tags',
    'accept_routes_from_resource_type',
    'advertise_routes_to',
    'route_direct_link_ingress',
    'route_internet_ingress',
    'route_transit_gateway_ingress',
    'vpc',
    'name',
    'route_vpc_zone_ingress',
    'access_tags',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('vpc', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'routing_table',
    'vpc',
    'name',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    tags=dict(
        required=False,
        elements='',
        type='list'),
    accept_routes_from_resource_type=dict(
        required=False,
        elements='',
        type='list'),
    advertise_routes_to=dict(
        required=False,
        elements='',
        type='list'),
    route_direct_link_ingress=dict(
        required=False,
        type='bool'),
    route_internet_ingress=dict(
        required=False,
        type='bool'),
    route_transit_gateway_ingress=dict(
        required=False,
        type='bool'),
    vpc=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    route_vpc_zone_ingress=dict(
        required=False,
        type='bool'),
    access_tags=dict(
        required=False,
        elements='',
        type='list'),
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
        resource_type='ibm_is_vpc_routing_table',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_vpc_routing_table',
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
