#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cis_range_app
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cis_range_app

short_description: Configure IBM Cloud 'ibm_cis_range_app' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cis_range_app' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.71.2
    - Terraform v1.5.5

options:
    edge_ips_connectivity:
        description:
            - Specifies the IP version.
        required: False
        type: str
        default: all
    tls:
        description:
            - Configure if and how TLS connections are terminated at the edge.
        required: False
        type: str
        default: off
    protocol:
        description:
            - (Required for new resource) Defines the protocol and port for this application
        required: True
        type: str
    dns:
        description:
            - (Required for new resource) Name of the DNS record for this application
        required: True
        type: str
    origin_direct:
        description:
            - IP address and port of the origin for this Range application.
        required: False
        type: list
        elements: str
    traffic_type:
        description:
            - Configure how traffic is handled at the edge.
        required: False
        type: str
        default: direct
    cis_id:
        description:
            - (Required for new resource) CIS Intance CRN
        required: True
        type: str
    dns_type:
        description:
            - (Required for new resource) Type of the DNS record for this application
        required: True
        type: str
    ip_firewall:
        description:
            - Enables the IP Firewall for this application. Only available for TCP applications.
        required: False
        type: bool
    proxy_protocol:
        description:
            - Allows for the true client IP to be passed to the service.
        required: False
        type: str
    domain_id:
        description:
            - (Required for new resource) CIS Domain ID
        required: True
        type: str
    origin_port:
        description:
            - Port at the origin that listens to traffic
        required: False
        type: int
    edge_ips_type:
        description:
            - The type of edge IP configuration.
        required: False
        type: str
        default: dynamic
    origin_dns:
        description:
            - DNS record pointing to the origin for this Range application.
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
    ('protocol', 'str'),
    ('dns', 'str'),
    ('cis_id', 'str'),
    ('dns_type', 'str'),
    ('domain_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'edge_ips_connectivity',
    'tls',
    'protocol',
    'dns',
    'origin_direct',
    'traffic_type',
    'cis_id',
    'dns_type',
    'ip_firewall',
    'proxy_protocol',
    'domain_id',
    'origin_port',
    'edge_ips_type',
    'origin_dns',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
    'origin_port': ['origin_direct'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    edge_ips_connectivity=dict(
        required=False,
        type='str'),
    tls=dict(
        required=False,
        type='str'),
    protocol=dict(
        required=False,
        type='str'),
    dns=dict(
        required=False,
        type='str'),
    origin_direct=dict(
        required=False,
        elements='',
        type='list'),
    traffic_type=dict(
        required=False,
        type='str'),
    cis_id=dict(
        required=False,
        type='str'),
    dns_type=dict(
        required=False,
        type='str'),
    ip_firewall=dict(
        required=False,
        type='bool'),
    proxy_protocol=dict(
        required=False,
        type='str'),
    domain_id=dict(
        required=False,
        type='str'),
    origin_port=dict(
        required=False,
        type='int'),
    edge_ips_type=dict(
        required=False,
        type='str'),
    origin_dns=dict(
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
        resource_type='ibm_cis_range_app',
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
