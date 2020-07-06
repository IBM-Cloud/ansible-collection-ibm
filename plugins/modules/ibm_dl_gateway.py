#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_dl_gateway
short_description: Configure IBM Cloud 'ibm_dl_gateway' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_dl_gateway' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.8.1
    - Terraform v0.12.20

options:
    location_name:
        description:
            - Gateway location
        required: False
        type: str
    carrier_name:
        description:
            - Carrier name
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The unique user-defined name for this gateway
        required: True
        type: str
    customer_name:
        description:
            - Customer name
        required: False
        type: str
    bgp_base_cidr:
        description:
            - (Required for new resource) BGP base CIDR
        required: True
        type: str
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
    type:
        description:
            - (Required for new resource) Gateway type
        required: True
        type: str
    bgp_asn:
        description:
            - (Required for new resource) BGP ASN
        required: True
        type: int
    cross_connect_router:
        description:
            - Cross connect router
        required: False
        type: str
    global:
        description:
            - (Required for new resource) Gateways with global routing (true) can connect to networks outside their associated region
        required: True
        type: bool
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
    ('name', 'str'),
    ('bgp_base_cidr', 'str'),
    ('metered', 'bool'),
    ('speed_mbps', 'int'),
    ('type', 'str'),
    ('bgp_asn', 'int'),
    ('global', 'bool'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'location_name',
    'carrier_name',
    'name',
    'customer_name',
    'bgp_base_cidr',
    'metered',
    'speed_mbps',
    'type',
    'bgp_asn',
    'cross_connect_router',
    'global',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    location_name=dict(
        required= False,
        type='str'),
    carrier_name=dict(
        required= False,
        type='str'),
    name=dict(
        required= False,
        type='str'),
    customer_name=dict(
        required= False,
        type='str'),
    bgp_base_cidr=dict(
        required= False,
        type='str'),
    metered=dict(
        required= False,
        type='bool'),
    speed_mbps=dict(
        required= False,
        type='int'),
    type=dict(
        required= False,
        type='str'),
    bgp_asn=dict(
        required= False,
        type='int'),
    cross_connect_router=dict(
        required= False,
        type='str'),
    global=dict(
        required= False,
        type='bool'),
    id=dict(
        required= False,
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

    result = ibmcloud_terraform(
        resource_type='ibm_dl_gateway',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.8.1',
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
