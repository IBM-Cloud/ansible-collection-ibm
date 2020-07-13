#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_dl_gateway_info
short_description: Retrieve IBM Cloud 'ibm_dl_gateway' resource

version_added: "2.8"

description:
    - Retrieve an IBM Cloud 'ibm_dl_gateway' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.8.1
    - Terraform v0.12.20

options:
    created_at:
        description:
            - The date and time resource was created
        required: False
        type: str
    cross_connect_router:
        description:
            - Cross connect router
        required: False
        type: str
    dedicated_hosting_id:
        description:
            - Dedicated host id
        required: False
        type: str
    port:
        description:
            - Gateway port
        required: False
        type: str
    name:
        description:
            - The unique user-defined name for this gateway
        required: True
        type: str
    bgp_base_cidr:
        description:
            - BGP base CIDR
        required: False
        type: str
    bgp_cer_cidr:
        description:
            - BGP customer edge router CIDR
        required: False
        type: str
    bgp_status:
        description:
            - Gateway BGP status
        required: False
        type: str
    type:
        description:
            - Gateway type
        required: False
        type: str
    provider_api_managed:
        description:
            - Indicates whether gateway was created through a provider portal
        required: False
        type: bool
    vlan:
        description:
            - VLAN allocated for this gateway
        required: False
        type: int
    bgp_ibm_cidr:
        description:
            - BGP IBM CIDR
        required: False
        type: str
    completion_notice_reject_reason:
        description:
            - Reason for completion notice rejection
        required: False
        type: str
    link_status:
        description:
            - Gateway link status
        required: False
        type: str
    operational_status:
        description:
            - Gateway operational status
        required: False
        type: str
    location_display_name:
        description:
            - Gateway location long name
        required: False
        type: str
    gateway_vcs:
        description:
            - Collection of direct link gateway virtual connections
        required: False
        type: list
        elements: dict
    bgp_ibm_asn:
        description:
            - IBM BGP ASN
        required: False
        type: int
    crn:
        description:
            - The CRN (Cloud Resource Name) of this gateway
        required: False
        type: str
    global:
        description:
            - Gateways with global routing (true) can connect to networks outside their associated region
        required: False
        type: bool
    speed_mbps:
        description:
            - Gateway speed in megabits per second
        required: False
        type: int
    bgp_asn:
        description:
            - BGP ASN
        required: False
        type: int
    location_name:
        description:
            - Gateway location
        required: False
        type: str
    metered:
        description:
            - Metered billing option
        required: False
        type: bool
    resource_group:
        description:
            - Gateway resource group
        required: False
        type: str
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
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'created_at',
    'cross_connect_router',
    'dedicated_hosting_id',
    'port',
    'name',
    'bgp_base_cidr',
    'bgp_cer_cidr',
    'bgp_status',
    'type',
    'provider_api_managed',
    'vlan',
    'bgp_ibm_cidr',
    'completion_notice_reject_reason',
    'link_status',
    'operational_status',
    'location_display_name',
    'gateway_vcs',
    'bgp_ibm_asn',
    'crn',
    'global',
    'speed_mbps',
    'bgp_asn',
    'location_name',
    'metered',
    'resource_group',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    created_at=dict(
        required=False,
        type='str'),
    cross_connect_router=dict(
        required=False,
        type='str'),
    dedicated_hosting_id=dict(
        required=False,
        type='str'),
    port=dict(
        required=False,
        type='str'),
    name=dict(
        required=True,
        type='str'),
    bgp_base_cidr=dict(
        required=False,
        type='str'),
    bgp_cer_cidr=dict(
        required=False,
        type='str'),
    bgp_status=dict(
        required=False,
        type='str'),
    type=dict(
        required=False,
        type='str'),
    provider_api_managed=dict(
        required=False,
        type='bool'),
    vlan=dict(
        required=False,
        type='int'),
    bgp_ibm_cidr=dict(
        required=False,
        type='str'),
    completion_notice_reject_reason=dict(
        required=False,
        type='str'),
    link_status=dict(
        required=False,
        type='str'),
    operational_status=dict(
        required=False,
        type='str'),
    location_display_name=dict(
        required=False,
        type='str'),
    gateway_vcs=dict(
        required=False,
        elements='',
        type='list'),
    bgp_ibm_asn=dict(
        required=False,
        type='int'),
    crn=dict(
        required=False,
        type='str'),
    global=dict(
        required=False,
        type='bool'),
    speed_mbps=dict(
        required=False,
        type='int'),
    bgp_asn=dict(
        required=False,
        type='int'),
    location_name=dict(
        required=False,
        type='str'),
    metered=dict(
        required=False,
        type='bool'),
    resource_group=dict(
        required=False,
        type='str'),
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

    result = ibmcloud_terraform(
        resource_type='ibm_dl_gateway',
        tf_type='data',
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
