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
    bgp_asn:
        description:
            - (Required for new resource) BGP ASN
        required: True
        type: int
    location_name:
        description:
            - Gateway location
        required: False
        type: str
    speed_mbps:
        description:
            - (Required for new resource) Gateway speed in megabits per second
        required: True
        type: int
    bgp_status:
        description:
            - Gateway BGP status
        required: False
        type: str
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    metered:
        description:
            - (Required for new resource) Metered billing option
        required: True
        type: bool
    port:
        description:
            - Gateway port
        required: False
        type: str
    provider_api_managed:
        description:
            - Indicates whether gateway was created through a provider portal
        required: False
        type: bool
    bgp_ibm_asn:
        description:
            - IBM BGP ASN
        required: False
        type: int
    completion_notice_reject_reason:
        description:
            - Reason for completion notice rejection
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The unique user-defined name for this gateway
        required: True
        type: str
    carrier_name:
        description:
            - Carrier name
        required: False
        type: str
    type:
        description:
            - (Required for new resource) Gateway type
        required: True
        type: str
    resource_group:
        description:
            - Gateway resource group
        required: False
        type: str
    link_status:
        description:
            - Gateway link status
        required: False
        type: str
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance
        required: False
        type: str
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    global:
        description:
            - (Required for new resource) Gateways with global routing (true) can connect to networks outside their associated region
        required: True
        type: bool
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
    operational_status:
        description:
            - Gateway operational status
        required: False
        type: str
    created_at:
        description:
            - The date and time resource was created
        required: False
        type: str
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    bgp_base_cidr:
        description:
            - (Required for new resource) BGP base CIDR
        required: True
        type: str
    cross_connect_router:
        description:
            - Cross connect router
        required: False
        type: str
    loa_reject_reason:
        description:
            - Loa reject reason
        required: False
        type: str
    bgp_ibm_cidr:
        description:
            - BGP IBM CIDR
        required: False
        type: str
    vlan:
        description:
            - VLAN allocated for this gateway
        required: False
        type: int
    crn:
        description:
            - The CRN (Cloud Resource Name) of this gateway
        required: False
        type: str
    location_display_name:
        description:
            - Gateway location long name
        required: False
        type: str
    tags:
        description:
            - Tags for the direct link gateway
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
    ('bgp_asn', 'int'),
    ('speed_mbps', 'int'),
    ('metered', 'bool'),
    ('name', 'str'),
    ('type', 'str'),
    ('global', 'bool'),
    ('bgp_base_cidr', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'bgp_asn',
    'location_name',
    'speed_mbps',
    'bgp_status',
    'resource_group_name',
    'metered',
    'port',
    'provider_api_managed',
    'bgp_ibm_asn',
    'completion_notice_reject_reason',
    'name',
    'carrier_name',
    'type',
    'resource_group',
    'link_status',
    'resource_controller_url',
    'resource_crn',
    'global',
    'customer_name',
    'bgp_cer_cidr',
    'operational_status',
    'created_at',
    'resource_status',
    'resource_name',
    'bgp_base_cidr',
    'cross_connect_router',
    'loa_reject_reason',
    'bgp_ibm_cidr',
    'vlan',
    'crn',
    'location_display_name',
    'tags',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    bgp_asn=dict(
        required= False,
        type='int'),
    location_name=dict(
        required= False,
        type='str'),
    speed_mbps=dict(
        required= False,
        type='int'),
    bgp_status=dict(
        required= False,
        type='str'),
    resource_group_name=dict(
        required= False,
        type='str'),
    metered=dict(
        required= False,
        type='bool'),
    port=dict(
        required= False,
        type='str'),
    provider_api_managed=dict(
        required= False,
        type='bool'),
    bgp_ibm_asn=dict(
        required= False,
        type='int'),
    completion_notice_reject_reason=dict(
        required= False,
        type='str'),
    name=dict(
        required= False,
        type='str'),
    carrier_name=dict(
        required= False,
        type='str'),
    type=dict(
        required= False,
        type='str'),
    resource_group=dict(
        required= False,
        type='str'),
    link_status=dict(
        required= False,
        type='str'),
    resource_controller_url=dict(
        required= False,
        type='str'),
    resource_crn=dict(
        required= False,
        type='str'),
    global=dict(
        required= False,
        type='bool'),
    customer_name=dict(
        required= False,
        type='str'),
    bgp_cer_cidr=dict(
        required= False,
        type='str'),
    operational_status=dict(
        required= False,
        type='str'),
    created_at=dict(
        required= False,
        type='str'),
    resource_status=dict(
        required= False,
        type='str'),
    resource_name=dict(
        required= False,
        type='str'),
    bgp_base_cidr=dict(
        required= False,
        type='str'),
    cross_connect_router=dict(
        required= False,
        type='str'),
    loa_reject_reason=dict(
        required= False,
        type='str'),
    bgp_ibm_cidr=dict(
        required= False,
        type='str'),
    vlan=dict(
        required= False,
        type='int'),
    crn=dict(
        required= False,
        type='str'),
    location_display_name=dict(
        required= False,
        type='str'),
    tags=dict(
        required= False,
        elements='',
        type='list'),
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
