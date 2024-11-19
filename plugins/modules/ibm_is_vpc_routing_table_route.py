#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_vpc_routing_table_route
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_vpc_routing_table_route

short_description: Configure IBM Cloud 'ibm_is_vpc_routing_table_route' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_vpc_routing_table_route' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    priority:
        description:
            - The route's priority. Smaller values have higher priority.
        required: False
        type: int
    destination:
        description:
            - (Required for new resource) The destination of the route.
        required: True
        type: str
    name:
        description:
            - The user-defined name for this route.
        required: False
        type: str
    routing_table:
        description:
            - (Required for new resource) The routing table identifier.
        required: True
        type: str
    vpc:
        description:
            - (Required for new resource) The VPC identifier.
        required: True
        type: str
    next_hop:
        description:
            - (Required for new resource) If action is deliver, the next hop that packets will be delivered to. For other action values, its address will be 0.0.0.0.
        required: True
        type: str
    advertise:
        description:
            - Indicates whether this route will be advertised to the ingress sources specified by the `advertise_routes_to` routing table property.
        required: False
        type: bool
        default: False
    zone:
        description:
            - (Required for new resource) The zone to apply the route to. Traffic from subnets in this zone will be subject to this route.
        required: True
        type: str
    action:
        description:
            - The action to perform with a packet matching the route.
        required: False
        type: str
        default: deliver
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
    ('destination', 'str'),
    ('routing_table', 'str'),
    ('vpc', 'str'),
    ('next_hop', 'str'),
    ('zone', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'priority',
    'destination',
    'name',
    'routing_table',
    'vpc',
    'next_hop',
    'advertise',
    'zone',
    'action',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
    ('routing_table', 'str'),
    ('vpc', 'str'),
]

TL_ALL_PARAMETERS_DS = [
    'route_id',
    'name',
    'routing_table',
    'vpc',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    priority=dict(
        required=False,
        type='int'),
    destination=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    routing_table=dict(
        required=False,
        type='str'),
    vpc=dict(
        required=False,
        type='str'),
    next_hop=dict(
        required=False,
        type='str'),
    advertise=dict(
        required=False,
        type='bool'),
    zone=dict(
        required=False,
        type='str'),
    action=dict(
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
        resource_type='ibm_is_vpc_routing_table_route',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.71.2',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_vpc_routing_table_route',
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
