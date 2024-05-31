#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_is_vpn_server
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_vpn_server

short_description: Configure IBM Cloud 'ibm_is_vpn_server' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_is_vpn_server' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.65.1
    - Terraform v1.5.5

options:
    client_authentication:
        description:
            - (Required for new resource) The methods used to authenticate VPN clients to this VPN server. VPN clients must authenticate against all provided methods.
        required: True
        type: list
        elements: dict
    client_dns_server_ips:
        description:
            - The DNS server addresses that will be provided to VPN clients connected to this VPN server. The IP address. This property may add support for IPv6 addresses in the future. When processing a value in this property, verify that the address is in an expected format. If it is not, log an error. Optionally halt processing and surface the error, or bypass the resource on which the unexpected IP address format was encountered.
        required: False
        type: list
        elements: str
    port:
        description:
            - The port number to use for this VPN server.
        required: False
        type: int
        default: 443
    resource_group:
        description:
            - The unique identifier for this resource group. The resource group to use. If unspecified, the account's [default resourcegroup](https://cloud.ibm.com/apidocs/resource-manager#introduction) is used.
        required: False
        type: str
    access_tags:
        description:
            - List of access management tags
        required: False
        type: list
        elements: str
    client_ip_pool:
        description:
            - (Required for new resource) The VPN client IPv4 address pool, expressed in CIDR format. The request must not overlap with any existing address prefixes in the VPC or any of the following reserved address ranges:  - `127.0.0.0/8` (IPv4 loopback addresses)  - `161.26.0.0/16` (IBM services)  - `166.8.0.0/14` (Cloud Service Endpoints)  - `169.254.0.0/16` (IPv4 link-local addresses)  - `224.0.0.0/4` (IPv4 multicast addresses)The prefix length of the client IP address pool's CIDR must be between`/9` (8,388,608 addresses) and `/22` (1024 addresses). A CIDR block that contains twice the number of IP addresses that are required to enable the maximum number of concurrent connections is recommended.
        required: True
        type: str
    security_groups:
        description:
            - The unique identifier for this security group. The security groups to use for this VPN server. If unspecified, the VPC's default security group is used.
        required: False
        type: list
        elements: str
    subnets:
        description:
            - (Required for new resource) The unique identifier for this subnet. The subnets to provision this VPN server in.  Use subnets in different zones for high availability.
        required: True
        type: list
        elements: str
    name:
        description:
            - The user-defined name for this VPN server. If unspecified, the name will be a hyphenated list of randomly-selected words. Names must be unique within the VPC this VPN server is serving.
        required: False
        type: str
    enable_split_tunneling:
        description:
            - Indicates whether the split tunneling is enabled on this VPN server.
        required: False
        type: bool
        default: False
    protocol:
        description:
            - The transport protocol to use for this VPN server.
        required: False
        type: str
        default: udp
    resource_type:
        description:
            - The type of resource referenced.
        required: False
        type: str
        default: vpn_server
    client_idle_timeout:
        description:
            - The seconds a VPN client can be idle before this VPN server will disconnect it.   Specify `0` to prevent the server from disconnecting idle clients.
        required: False
        type: int
        default: 600
    certificate_crn:
        description:
            - (Required for new resource) The crn of certificate instance for this VPN server.
        required: True
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
    generation:
        description:
            - The generation of Virtual Private Cloud infrastructure
              that you want to use. Supported values are 1 for VPC
              generation 1, and 2 for VPC generation 2 infrastructure.
              If this value is not specified, 2 is used by default. This
              can also be provided via the environment variable
              'IC_GENERATION'.
        default: 2
        required: False
        type: int
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
    ('client_authentication', 'list'),
    ('client_ip_pool', 'str'),
    ('subnets', 'list'),
    ('certificate_crn', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'client_authentication',
    'client_dns_server_ips',
    'port',
    'resource_group',
    'access_tags',
    'client_ip_pool',
    'security_groups',
    'subnets',
    'name',
    'enable_split_tunneling',
    'protocol',
    'resource_type',
    'client_idle_timeout',
    'certificate_crn',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
    'name',
    'identifier',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    client_authentication=dict(
        required=False,
        elements='',
        type='list'),
    client_dns_server_ips=dict(
        required=False,
        elements='',
        type='list'),
    port=dict(
        required=False,
        type='int'),
    resource_group=dict(
        required=False,
        type='str'),
    access_tags=dict(
        required=False,
        elements='',
        type='list'),
    client_ip_pool=dict(
        required=False,
        type='str'),
    security_groups=dict(
        required=False,
        elements='',
        type='list'),
    subnets=dict(
        required=False,
        elements='',
        type='list'),
    name=dict(
        required=False,
        type='str'),
    enable_split_tunneling=dict(
        required=False,
        type='bool'),
    protocol=dict(
        required=False,
        type='str'),
    resource_type=dict(
        required=False,
        type='str'),
    client_idle_timeout=dict(
        required=False,
        type='int'),
    certificate_crn=dict(
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
    generation=dict(
        type='int',
        required=False,
        fallback=(env_fallback, ['IC_GENERATION']),
        default=2),
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
        resource_type='ibm_is_vpn_server',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.65.1',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_is_vpn_server',
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
